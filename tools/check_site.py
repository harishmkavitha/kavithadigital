#!/usr/bin/env python3
"""
Kavitha Digital — check_site.py — V1
Consistency audit for the built site. Standard library only.

    python3 tools/check_site.py

Checks every HTML page for: unique titles and descriptions, exactly one H1,
heading order, canonical/OG/Twitter/robots tags, valid JSON-LD, breadcrumbs,
broken internal links and anchors, '#' placeholder links, duplicate IDs,
image alt/width/height, phone and WhatsApp numbers, orphan pages, links back
to the home page, sitemap coverage and unbalanced tags.
Exit code 1 if any error is found — run it before every deploy.
"""

import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_config as C  # noqa: E402

TEL = "tel:" + C.BUSINESS["phone_e164"]
WA = "https://wa.me/" + C.BUSINESS["whatsapp"]
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SVG_INNER = {"path", "circle", "rect", "ellipse", "line", "polyline", "polygon", "stop", "use", "g", "defs",
             "lineargradient", "radialgradient", "text"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.links = []          # (tag, attr, value)
        self.ids = []
        self.headings = []       # (level, text)
        self._h = None
        self.imgs = []
        self.jsonld = []
        self._in_ld = False
        self._buf = ""
        self.stack = []
        self.errors = []
        self.canonical = None
        self.base = None
        self.breadcrumb = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID and tag not in SVG_INNER:
            self.stack.append(tag)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content", "")
        elif tag == "link":
            if a.get("rel") == "canonical":
                self.canonical = a.get("href")
            if a.get("href"):
                self.links.append(("link", "href", a["href"]))
        elif tag == "base":
            self.base = a.get("href")
        elif tag == "a":
            self.links.append(("a", "href", a.get("href", "")))
        elif tag in ("script",) and a.get("src"):
            self.links.append(("script", "src", a["src"]))
        elif tag == "img":
            self.imgs.append(a)
            self.links.append(("img", "src", a.get("src", "")))
            for part in (a.get("srcset") or "").split(","):
                if part.strip():
                    self.links.append(("img", "srcset", part.strip().split(" ")[0]))
        elif tag == "source":
            for part in (a.get("srcset") or "").split(","):
                if part.strip():
                    self.links.append(("source", "srcset", part.strip().split(" ")[0]))
        elif tag == "form" and a.get("action", "").startswith(("http", "/")) is False and a.get("action"):
            self.links.append(("form", "action", a["action"]))
        elif tag == "nav" and a.get("aria-label") == "Breadcrumb":
            self.breadcrumb = True
        if re.fullmatch(r"h[1-6]", tag):
            self._h = [int(tag[1]), ""]
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self._buf = ""

    def handle_startendtag(self, tag, attrs):
        # self-closing (<path/>): never pushed
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if self._h and tag == f"h{self._h[0]}":
            self.headings.append((self._h[0], self._h[1].strip()))
            self._h = None
        if tag == "script" and self._in_ld:
            self._in_ld = False
            self.jsonld.append(self._buf)
        if tag in VOID or tag in SVG_INNER:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.errors.append(f"unclosed <{self.stack.pop()}> before </{tag}>")
            self.stack.pop()
        else:
            self.errors.append(f"stray </{tag}>")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._h:
            self._h[1] += data
        if self._in_ld:
            self._buf += data


def main():
    pages = sorted(p for p in ROOT.rglob("*.html") if "tools" not in p.relative_to(ROOT).parts)
    parsed = {}
    errors, warnings = [], []

    def err(page, msg):
        errors.append(f"{page}: {msg}")

    def warn(page, msg):
        warnings.append(f"{page}: {msg}")

    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8")
        pg = Page()
        pg.feed(text)
        pg.close()
        parsed[rel] = pg
        if re.search(r"lorem ipsum", text, re.I):
            err(rel, "contains lorem ipsum")
        for e in pg.errors[:5]:
            err(rel, f"markup: {e}")
        if pg.stack:
            err(rel, f"unclosed tags at end: {pg.stack[-5:]}")

    titles, descs = defaultdict(list), defaultdict(list)
    inbound = defaultdict(set)
    ids_by_page = {rel: set(pg.ids) for rel, pg in parsed.items()}

    for rel, pg in parsed.items():
        is404 = rel == "404.html"
        titles[pg.title.strip()].append(rel)
        desc = pg.meta.get("description", "")
        descs[desc].append(rel)
        if not (30 <= len(pg.title) <= 65):
            warn(rel, f"title length {len(pg.title)}: {pg.title}")
        if not (120 <= len(desc) <= 165):
            warn(rel, f"description length {len(desc)}")
        h1s = [h for h in pg.headings if h[0] == 1]
        if len(h1s) != 1:
            err(rel, f"{len(h1s)} H1 headings")
        prev = 1
        for lvl, txt in pg.headings:
            if lvl > prev + 1:
                err(rel, f"heading jumps h{prev}→h{lvl} at '{txt[:40]}'")
            prev = lvl
        for k in ("description", "robots", "og:title", "og:description", "og:url", "og:image",
                  "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
            if not pg.meta.get(k):
                err(rel, f"missing meta {k}")
        if not pg.canonical or not pg.canonical.startswith(C.SITE_URL.rstrip("/")):
            err(rel, f"canonical missing or off-domain: {pg.canonical}")
        if rel != "index.html" and not is404 and not pg.breadcrumb:
            err(rel, "no breadcrumb")
        for block in pg.jsonld:
            try:
                data = json.loads(block)
                graph = data.get("@graph", [data])
                types = {n.get("@type") if isinstance(n.get("@type"), str) else "/".join(n["@type"]) for n in graph}
                if rel != "index.html" and not is404 and "BreadcrumbList" not in types:
                    err(rel, "JSON-LD has no BreadcrumbList")
                blob = json.dumps(data)
                for bad in ("aggregateRating", "review", "priceRange", "openingHours", "geo"):
                    if f'"{bad}"' in blob:
                        err(rel, f"JSON-LD contains unsupported claim field '{bad}'")
            except json.JSONDecodeError as e:
                err(rel, f"invalid JSON-LD: {e}")
        if len(pg.ids) != len(set(pg.ids)):
            dupes = sorted({i for i in pg.ids if pg.ids.count(i) > 1})
            err(rel, f"duplicate ids: {dupes}")
        for im in pg.imgs:
            if "alt" not in im:
                err(rel, f"img without alt: {im.get('src')}")
            if not im.get("width") or not im.get("height"):
                err(rel, f"img without width/height: {im.get('src')}")
            if im.get("loading") != "lazy" and im.get("fetchpriority") != "high":
                warn(rel, f"below-fold image not lazy? {im.get('src')}")

        base_dir = "" if pg.base else str(Path(rel).parent)
        links_home = False
        for tag, attr, href in pg.links:
            if tag == "a" and (href == "" or href == "#"):
                err(rel, "empty or '#' link")
                continue
            if href.startswith("tel:"):
                if href != TEL:
                    err(rel, f"wrong phone link {href}")
                continue
            if "wa.me/" in href:
                if not href.startswith(WA):
                    err(rel, f"wrong WhatsApp link {href}")
                continue
            if href.startswith(("mailto:", "http://", "https://", "data:")):
                continue
            path, _, frag = href.partition("#")
            path = path.split("?")[0]
            if not path:  # same-page anchor
                if frag and frag not in ids_by_page[rel]:
                    err(rel, f"missing anchor #{frag}")
                continue
            target = (Path(base_dir) / path) if base_dir not in ("", ".") else Path(path)
            target = Path(*[x for x in target.parts])  # normalise
            resolved = (ROOT / target).resolve()
            try:
                trel = resolved.relative_to(ROOT).as_posix()
            except ValueError:
                err(rel, f"link escapes site root: {href}")
                continue
            if not resolved.exists():
                err(rel, f"broken {tag} {attr}: {href}")
                continue
            if trel.endswith(".html"):
                if trel != rel:
                    inbound[trel].add(rel)
                if trel == "index.html":
                    links_home = True
                if frag and frag not in ids_by_page.get(trel, set()):
                    err(rel, f"missing anchor {href}")
        if not links_home and rel != "index.html":
            err(rel, "does not link to the home page")

    for t, where in titles.items():
        if len(where) > 1:
            err(", ".join(where), f"duplicate title '{t}'")
    for d, where in descs.items():
        if len(where) > 1:
            err(", ".join(where), "duplicate meta description")
    for rel in parsed:
        if rel not in ("index.html", "404.html") and not inbound[rel]:
            err(rel, "orphan page (no inbound links)")

    # sitemap coverage
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    site = C.SITE_URL.rstrip("/")
    for loc in locs:
        path = urlparse(loc).path[len(urlparse(site).path):].lstrip("/") or "index.html"
        if path.endswith("/"):
            path += "index.html"
        if not (ROOT / path).exists():
            err("sitemap.xml", f"URL has no file: {loc}")
    indexable = [r for r in parsed if r != "404.html"]
    if len(locs) != len(indexable):
        err("sitemap.xml", f"{len(locs)} URLs but {len(indexable)} indexable pages")

    print(f"Checked {len(parsed)} pages.")
    for w in warnings:
        print("  warn ", w)
    for e in errors:
        print("  ERROR", e)
    print(f"{len(errors)} errors, {len(warnings)} warnings.")
    if "example.com" in C.SITE_URL:
        print("Reminder: SITE_URL is still the example.com placeholder.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
