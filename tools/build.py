#!/usr/bin/env python3
"""
Kavitha Digital — build.py — V1
Static site generator. Renders every HTML page, sitemap.xml and robots.txt
from the content files in tools/content/. Python 3.8+, standard library only.

    python3 tools/build.py

Why a generator: the site will grow to 300+ pages. Header, footer, breadcrumbs,
schema and metadata are written once here, so every new page gets them right
automatically. Page copy lives in tools/content/*.py.

Internal links inside content use  [anchor text](@page-key)  and are resolved to
correct relative paths for each folder depth. An unknown key stops the build,
so broken internal links cannot be published.
"""

import html
import json
import posixpath
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlparse

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import site_config as C                          # noqa: E402
from icons import icon, logo_mark                # noqa: E402
from content import images as IMG                # noqa: E402
from content import home as HOME                 # noqa: E402
from content import services as SERVICES         # noqa: E402
from content import locations as LOCATIONS       # noqa: E402
from content import blog as BLOG                 # noqa: E402
from content import pages as PAGES               # noqa: E402

B = C.BUSINESS
SITE = C.SITE_URL.rstrip("/")
TODAY = date.today().isoformat()


# ==========================================================================
# Page registry — every page, keyed. Content links use these keys.
# ==========================================================================
REG = {}


def register(page):
    key = page["key"]
    if key in REG:
        sys.exit(f"Duplicate page key: {key}")
    REG[key] = page


for _p in PAGES.CORE:
    register(_p)
for _p in SERVICES.SERVICES:
    _p.setdefault("type", "service")
    register(_p)
for _p in LOCATIONS.LOCATIONS:
    _p.setdefault("type", "location")
    register(_p)
for _p in BLOG.POSTS:
    _p.setdefault("type", "post")
    register(_p)


# ==========================================================================
# Render context + helpers
# ==========================================================================
class Ctx:
    path = "index.html"   # current page, relative to site root
    section = ""          # top-level nav section of the current page
    base_mode = False     # True for 404.html (served from any depth → uses <base>)
    sec = 0               # section counter for eyebrow numbers


def esc(s):
    return html.escape(str(s), quote=True)


def rel(target):
    """Site-root-relative path → path relative to the page being rendered."""
    if re.match(r"^(https?:|tel:|mailto:|#)", target):
        return target
    anchor = ""
    if "#" in target:
        target, frag = target.split("#", 1)
        anchor = "#" + frag
    if Ctx.base_mode:
        return target + anchor
    cur_dir = posixpath.dirname(Ctx.path) or "."
    return posixpath.relpath(target, cur_dir) + anchor


def url_of(key):
    if key not in REG:
        sys.exit(f"Unknown page key '@{key}' used on {Ctx.path}")
    return rel(REG[key]["path"])


def canonical(path):
    """Clean absolute URL: folder index pages end in '/', others keep .html."""
    if path == "index.html":
        return SITE + "/"
    if path.endswith("/index.html"):
        return f"{SITE}/{path[:-len('index.html')]}"
    return f"{SITE}/{path}"


def asset(path):
    return rel(path) + (f"?v={C.ASSET_VERSION}" if path.endswith((".css", ".js")) else "")


LINK_RE = re.compile(r"\[([^\]]+)\]\(@([\w-]+)(#[\w-]+)?\)")


def md(s):
    """Tiny inline markup: [text](@key), [text](@key#anchor), **bold**."""
    s = re.sub(r"&(?!#?\w+;)", "&amp;", s)

    def repl(m):
        key, frag = m.group(2), m.group(3) or ""
        if key not in REG:
            sys.exit(f"Unknown link key '@{key}' in content for {Ctx.path}")
        return f'<a href="{rel(REG[key]["path"] + frag)}">{m.group(1)}</a>'

    s = LINK_RE.sub(repl, s)
    s = s.replace("{PHONE}", f'<a href="{tel()}">{B["phone_display"]}</a>')
    s = s.replace("{PHONE_SHORT}", B["phone_short"])
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


def plain(s):
    s = LINK_RE.sub(lambda m: m.group(1), s)
    s = s.replace("{PHONE}", B["phone_display"]).replace("{PHONE_SHORT}", B["phone_short"])
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def paras(items, cls=""):
    klass = f' class="{cls}"' if cls else ""
    return "\n".join(f"<p{klass}>{md(p)}</p>" for p in items)


def num():
    Ctx.sec += 1
    return f"{Ctx.sec:02d}"


def wa_link(topic=None):
    text = f"Hi Harish, I found Kavitha Digital online and I'd like to discuss {topic or 'my website and online marketing'}."
    return f"https://wa.me/{B['whatsapp']}?text={quote(text)}"


def tel():
    return f"tel:{B['phone_e164']}"


# ==========================================================================
# Components
# ==========================================================================
def picture(name, sizes, eager=False, alt=None, cls=""):
    """<picture> with AVIF + WebP at 640w and full width. Width/height always set."""
    im = IMG.IMAGES[name]
    folder, w, h = im["folder"], im["w"], im["h"]
    base = f"assets/images/{folder}/{name}"
    alt_text = alt if alt is not None else im["alt"]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    klass = f' class="{cls}"' if cls else ""
    return (
        f'<picture{klass}>'
        f'<source type="image/avif" srcset="{rel(base + "-640.avif")} 640w, {rel(base + ".avif")} {w}w" sizes="{sizes}">'
        f'<img src="{rel(base + ".webp")}" srcset="{rel(base + "-640.webp")} 640w, {rel(base + ".webp")} {w}w" '
        f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt_text)}" {load} decoding="async">'
        f'</picture>'
    )


def preload_image(name, sizes):
    base = f"assets/images/{IMG.IMAGES[name]['folder']}/{name}"
    w = IMG.IMAGES[name]["w"]
    return (f'<link rel="preload" as="image" type="image/avif" '
            f'imagesrcset="{rel(base + "-640.avif")} 640w, {rel(base + ".avif")} {w}w" imagesizes="{sizes}" fetchpriority="high">')


def eyebrow(text, numbered=True):
    n = f'<span class="eyebrow__num">{num()}</span>' if numbered else ""
    return f'<p class="eyebrow">{n}{esc(text)}</p>'


def section_head(eyebrow_text, h2, lead=None, center=False, h2_id=None, numbered=True):
    cls = "section-head section-head--center" if center else "section-head"
    hid = f' id="{h2_id}"' if h2_id else ""
    lead_html = f'<p class="lead">{md(lead)}</p>' if lead else ""
    return f'<div class="{cls}" data-reveal>{eyebrow(eyebrow_text, numbered)}<h2{hid}>{md(h2)}</h2>{lead_html}</div>'


def btn(label, href, kind="primary", icon_name=None, extra="", icon_after=None):
    ic = icon(icon_name) if icon_name else ""
    ia = icon(icon_after) if icon_after else ""
    return f'<a class="btn btn--{kind}" href="{href}"{extra}>{ic}<span>{esc(label)}</span>{ia}</a>'


def wa_btn(label="WhatsApp us", topic=None, kind="whatsapp"):
    return btn(label, wa_link(topic), kind, "whatsapp", ' target="_blank" rel="noopener"')


def call_btn(label=None, kind="ghost"):
    return btn(label or f"Call {B['phone_short']}", tel(), kind, "phone")


def breadcrumb(trail):
    """trail: list of (label, key or None). Last item is the current page."""
    items = []
    for i, (label, key) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li><span aria-current="page">{esc(label)}</span></li>')
        else:
            items.append(f'<li><a href="{url_of(key)}">{esc(label)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def service_card(key, heading="h3"):
    s = REG[key]
    return (
        f'<article class="card card--link service-card" data-reveal>'
        f'<span class="icon-box">{icon(s["icon"])}</span>'
        f'<{heading}><a class="card__link" href="{url_of(key)}">{esc(s["label"])}</a></{heading}>'
        f'<p>{md(s["card_text"])}</p>'
        f'<span class="card__more link-arrow" aria-hidden="true">Learn more {icon("arrow-right")}</span>'
        f'</article>'
    )


def location_card(key):
    p = REG[key]
    return (
        f'<article class="card card--link location-card" data-reveal>'
        f'<span class="tag">{icon("map-pin")}{esc(p["area_tag"])}</span>'
        f'<h3><a class="card__link" href="{url_of(key)}">{esc(p["label"])}</a></h3>'
        f'<p>{md(p["card_text"])}</p>'
        f'<span class="card__more link-arrow" aria-hidden="true">View page {icon("arrow-right")}</span>'
        f'</article>'
    )


def blog_card(key, heading="h3"):
    p = REG[key]
    return (
        f'<article class="card card--link card--media blog-card" data-reveal data-category="{p["cat_slug"]}">'
        f'<div class="card__media">{picture(p["image"], "(min-width: 2560px) 500px, (min-width: 1920px) 440px, (min-width: 900px) 380px, (min-width: 640px) 45vw, 92vw")}</div>'
        f'<div class="card__body"><span class="tag">{esc(p["category"])}</span>'
        f'<{heading}><a class="card__link" href="{url_of(key)}">{esc(p["h1"])}</a></{heading}>'
        f'<p>{md(p["excerpt"])}</p>'
        f'<p class="card__meta"><span>{fmt_date(p["date"])}</span><span>{esc(p["read"])}</span></p>'
        f'</div></article>'
    )


def feature(ic, title, text, heading="h3"):
    return (f'<div class="feature" data-reveal><span class="icon-box">{icon(ic)}</span>'
            f'<div><{heading}>{md(title)}</{heading}><p>{md(text)}</p></div></div>')


def problem(title, text):
    return f'<div class="problem" data-reveal><h3>{md(title)}</h3><p>{md(text)}</p></div>'


def checklist(items):
    lis = "".join(f'<li>{icon("check")}<div><strong>{md(t)}</strong><span>{md(d)}</span></div></li>' for t, d in items)
    return f'<ul class="checklist">{lis}</ul>'


def process(steps, stack=False):
    """Numbered steps. stack=True keeps them vertical at every width (for narrow columns)."""
    lis = "".join(f'<li class="process__step" data-reveal><h3>{md(t)}</h3><p>{md(d)}</p></li>' for t, d in steps)
    extra = " process--stack" if stack else ""
    return f'<ol class="process process--{len(steps)}{extra}" data-reveal-stagger>{lis}</ol>'


def faq_list(items, center=False):
    cls = "faq faq--center" if center else "faq"
    out = []
    for q, a in items:
        answer = a if isinstance(a, list) else [a]
        out.append(f'<details class="faq__item"><summary><span>{esc(q)}</span><span class="faq__icon" aria-hidden="true"></span></summary>'
                   f'<div class="faq__answer">{paras(answer)}</div></details>')
    return f'<div class="{cls}">{"".join(out)}</div>'


def chips(areas, linked=True):
    out = []
    for a in areas:
        name, key = (a["name"], a.get("key")) if isinstance(a, dict) else (a, None)
        if linked and key and REG[key]["path"] != Ctx.path:
            out.append(f'<li><a class="chip" href="{url_of(key)}">{icon("map-pin")}{esc(name)}</a></li>')
        else:
            out.append(f'<li><span class="chip">{icon("map-pin")}{esc(name)}</span></li>')
    return f'<ul class="chips">{"".join(out)}</ul>'


def cta_band(h2, text, button="Get a Free Consultation", topic=None):
    return f'''
<section class="section section--tight" aria-labelledby="cta-heading">
  <div class="container">
    <div class="cta-band" data-reveal="scale">
      <div class="cta-band__grid">
        <div>
          <h2 id="cta-heading">{md(h2)}</h2>
          <p>{md(text)}</p>
          <p class="cta-band__contact">Or call Harish directly on <a href="{tel()}">{B["phone_display"]}</a></p>
        </div>
        <div class="cta-band__actions">
          {btn(button, url_of("contact"), "light", None, "", "arrow-right")}
          {wa_btn("WhatsApp", topic, "outline-light")}
        </div>
      </div>
    </div>
  </div>
</section>'''


def contact_cards(heading="h3"):
    email = B["email"]
    email_card = (
        f'<p><a href="mailto:{email}">{email}</a></p>' if email else
        '<p>Email address coming soon — please call or WhatsApp for now.</p><!-- PLACEHOLDER: set BUSINESS["email"] in tools/site_config.py -->'
    )
    cards = [
        ("phone", "Call", f'<p><a href="{tel()}">{B["phone_display"]}</a></p><p>Speak to Harish, the owner.</p>'),
        ("whatsapp", "WhatsApp", f'<p><a href="{wa_link()}" target="_blank" rel="noopener">Chat on WhatsApp</a></p><p>Send a message, screenshots or your current website link.</p>'),
        ("mail", "Email", email_card),
        ("map-pin", "Location", f'<p><strong>{esc(C.ADDRESS_LINE)}</strong></p><p>Tamil Nadu, India. Serving businesses across Chennai.</p>'),
    ]
    return "".join(
        f'<div class="card contact-card" data-reveal><span class="icon-box">{icon(ic)}</span>'
        f'<div><{heading}>{t}</{heading}>{body}</div></div>' for ic, t, body in cards
    )


def fmt_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    return f"{d} {months[m - 1]} {y}"


# ==========================================================================
# Navigation data (keys into REG) — add future pages here once
# ==========================================================================
SERVICE_GROUPS = [
    ("Build", ["svc-website-design", "svc-website-development", "svc-responsive", "svc-ecommerce"]),
    ("Grow", ["svc-seo", "svc-local-seo", "svc-google-ads", "svc-social-media", "svc-content"]),
    ("Support", ["svc-maintenance", "svc-graphic-design"]),
]
SEO_MENU = ["svc-seo", "svc-local-seo", "loc-chennai-seo"]
DM_MENU = ["loc-chennai-digital-marketing", "svc-google-ads", "svc-social-media", "svc-content"]
LOCATION_GROUPS = [
    ("Chennai", ["loc-chennai-digital-marketing", "loc-chennai-website-design", "loc-chennai-seo"]),
    ("Pallikaranai", ["loc-pallikaranai"]),
]
FOOTER_SERVICES = ["svc-website-design", "svc-website-development", "svc-seo", "svc-local-seo",
                   "svc-google-ads", "svc-social-media", "svc-ecommerce", "svc-maintenance"]


def section_of(page):
    k, t = page["key"], page.get("type")
    if k in ("svc-seo", "svc-local-seo", "loc-chennai-seo"):
        return "seo"
    if k in ("loc-chennai-digital-marketing", "svc-google-ads", "svc-social-media", "svc-content"):
        return "dm"
    if t == "service" or k == "services":
        return "services"
    if t == "location" or k == "locations":
        return "locations"
    if t == "post" or k == "blog":
        return "blog"
    return k


def menu_link(key, show_desc=False):
    p = REG[key]
    cur = ' aria-current="page"' if p["path"] == Ctx.path else ""
    label = p.get("menu_label", p["label"])
    desc = f'<span class="submenu__desc">{esc(p["menu_desc"])}</span>' if show_desc and p.get("menu_desc") else ""
    return (f'<li><a class="submenu__link" href="{url_of(key)}"{cur}>'
            f'<span class="submenu__icon">{icon(p["icon"])}</span>'
            f'<span><span class="submenu__label">{esc(label)}</span>{desc}</span></a></li>')


def nav_item(label, key, section, sub=None, sub_id=None, mega=False):
    p = REG[key]
    cur_page = ' aria-current="page"' if p["path"] == Ctx.path else ""
    classes = ["nav-item"]
    if sub:
        classes.append("has-sub")
    if mega:
        classes.append("nav-item--mega")
    if section and section == Ctx.section:
        classes.append("is-current")
    toggle = ""
    if sub:
        toggle = (f'<button class="sub-toggle" type="button" aria-expanded="false" aria-controls="{sub_id}">'
                  f'<span class="visually-hidden">{esc(label)} menu</span>{icon("chevron-down")}</button>')
    return (f'<li class="{" ".join(classes)}"><div class="nav-item__row">'
            f'<a class="nav-link" href="{url_of(key)}"{cur_page}>{esc(label)}</a>{toggle}</div>{sub or ""}</li>')


def header():
    groups = "".join(
        f'<div class="submenu__group"><p class="submenu__title">{g}</p><ul class="submenu__list">'
        + "".join(menu_link(k, True) for k in keys) + '</ul></div>'
        for g, keys in SERVICE_GROUPS
    )
    services_sub = (
        f'<div class="submenu submenu--mega" id="sub-services">{groups}'
        f'<div class="submenu__promo"><div><strong>Not sure where to start?</strong>'
        f'Tell Harish about your business and get an honest recommendation on what to do first.</div>'
        f'{btn("Get a free consultation", url_of("contact"), "light")}'
        f'<a class="submenu__all submenu__all--light" href="{url_of("services")}">All services {icon("arrow-right")}</a></div></div>'
    )
    seo_sub = f'<div class="submenu" id="sub-seo"><ul class="submenu__list">{"".join(menu_link(k) for k in SEO_MENU)}</ul></div>'
    dm_sub = f'<div class="submenu" id="sub-dm"><ul class="submenu__list">{"".join(menu_link(k) for k in DM_MENU)}</ul></div>'
    loc_groups = "".join(
        f'<div class="submenu__group"><p class="submenu__title">{g}</p><ul class="submenu__list">'
        + "".join(menu_link(k) for k in keys) + '</ul></div>' for g, keys in LOCATION_GROUPS
    )
    loc_sub = (f'<div class="submenu" id="sub-locations">{loc_groups}'
               f'<a class="submenu__all" href="{url_of("locations")}">All areas we serve {icon("arrow-right")}</a></div>')

    items = "".join([
        nav_item("Home", "home", "home"),
        nav_item("About", "about", "about"),
        nav_item("Services", "services", "services", services_sub, "sub-services", mega=True),
        nav_item("SEO", "svc-seo", "seo", seo_sub, "sub-seo"),
        nav_item("Digital Marketing", "loc-chennai-digital-marketing", "dm", dm_sub, "sub-dm"),
        nav_item("Locations", "locations", "locations", loc_sub, "sub-locations"),
        nav_item("Blog", "blog", "blog"),
        nav_item("Contact", "contact", "contact"),
    ])
    return f'''
<a class="skip-link" href="#main">Skip to main content</a>
<!-- ===== Header (generated by tools/build.py — edit there, not here) ===== -->
<header class="site-header">
  <div class="site-header__bar">
    <a class="logo" href="{url_of("home")}" aria-label="Kavitha Digital home page">{logo_mark("h")}<span class="logo__text">Kavitha <span>Digital</span></span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
      <span class="nav-toggle__text">Menu</span><span class="nav-toggle__icon" aria-hidden="true"><span></span><span></span><span></span></span>
    </button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul class="nav-list">{items}</ul>
      <div class="nav-cta">
        {btn("Get a Free Consultation", url_of("contact"), "primary", None, "", "arrow-right")}
        {call_btn()}
        {wa_btn("WhatsApp Harish")}
      </div>
    </nav>
    <a class="btn btn--primary btn--sm header-cta" href="{url_of("contact")}"><span>Free Consultation</span></a>
  </div>
</header>'''


def footer():
    svc = "".join(f'<li><a href="{url_of(k)}">{esc(REG[k]["label"])}</a></li>' for k in FOOTER_SERVICES)
    svc += f'<li><a href="{url_of("services")}">All services</a></li>'
    loc = ""
    for g, keys in LOCATION_GROUPS:
        loc += f'<p class="footer__sub">{g}</p><ul class="footer__list">'
        loc += "".join(f'<li><a href="{url_of(k)}">{esc(REG[k].get("footer_label", REG[k]["label"]))}</a></li>' for k in keys)
        loc += "</ul>"
    loc += f'<ul class="footer__list"><li><a href="{url_of("locations")}">All areas we serve</a></li></ul>'
    quick = "".join(f'<li><a href="{url_of(k)}">{esc(t)}</a></li>' for k, t in [
        ("home", "Home"), ("about", "About Kavitha Digital"), ("blog", "Blog"), ("faq", "FAQ"),
        ("contact", "Contact"), ("privacy", "Privacy Policy"), ("terms", "Terms of Use")])
    email_line = (f'<div>{icon("mail")}<span><strong>Email</strong><a href="mailto:{B["email"]}">{B["email"]}</a></span></div>'
                  if B["email"] else "")
    socials = [(n, u) for n, u in C.SOCIAL.items() if u]
    social_html = ""
    if socials:
        social_html = '<ul class="footer__list">' + "".join(
            f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{n.title()}</a></li>' for n, u in socials) + "</ul>"
    return f'''
<!-- ===== Footer (generated by tools/build.py — edit there, not here) ===== -->
<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="logo" href="{url_of("home")}" aria-label="Kavitha Digital home page">{logo_mark("f")}<span class="logo__text">Kavitha <span>Digital</span></span></a>
        <p>Website design, website development, SEO and digital marketing for businesses in Pallikaranai and across Chennai. Run by Harish — one accountable point of contact from first call to launch and beyond.</p>
        <div class="footer__actions">{call_btn(f"Call {B['phone_short']}", "light")}{wa_btn("WhatsApp", None, "outline-light")}</div>
        {social_html}
      </div>
      <div>
        <p class="footer__title">Services</p>
        <ul class="footer__list">{svc}</ul>
      </div>
      <div>
        <p class="footer__title">Locations</p>
        {loc}
      </div>
      <div>
        <p class="footer__title">Quick links</p>
        <ul class="footer__list">{quick}</ul>
      </div>
      <div>
        <p class="footer__title">Contact</p>
        <address class="footer__contact">
          <div>{icon("user")}<span><strong>{esc(B["name"])}</strong>Owner: {esc(B["owner"])}</span></div>
          <div>{icon("phone")}<span><strong>Phone / WhatsApp</strong><a href="{tel()}">{B["phone_display"]}</a></span></div>
          {email_line}
          <div>{icon("map-pin")}<span><strong>Location</strong>{esc(C.ADDRESS_LINE)}<br>Tamil Nadu, India</span></div>
        </address>
      </div>
    </div>
    <div class="footer__bottom">
      <p>&copy; <span data-year>{date.today().year}</span> Kavitha Digital. All rights reserved.</p>
      <p>Website design · SEO · Digital marketing — {esc(C.ADDRESS_LINE)}</p>
    </div>
  </div>
</footer>'''


def floating(topic=None):
    return f'''
<!-- ===== Floating contact buttons ===== -->
<div class="fab-stack">
  <a class="fab fab--whatsapp" href="{wa_link(topic)}" target="_blank" rel="noopener" aria-label="Chat with Kavitha Digital on WhatsApp">{icon("whatsapp")}<span class="fab__label" aria-hidden="true">WhatsApp</span></a>
  <a class="fab fab--call" href="{tel()}" aria-label="Call Kavitha Digital on {B["phone_display"]}">{icon("phone")}<span class="fab__label" aria-hidden="true">Call<span class="fab__num"> {B["phone_short"]}</span></span></a>
</div>
<button class="to-top" type="button" aria-label="Back to top">{icon("arrow-up")}</button>'''


# ==========================================================================
# Structured data (JSON-LD) — factual fields only. No ratings, reviews,
# prices, hours, geo or social profiles until real values are supplied.
# ==========================================================================
BUSINESS_ID = f"{SITE}/#business"
WEBSITE_ID = f"{SITE}/#website"


def area_served():
    places = [{"@type": "City", "name": "Chennai"}]
    places += [{"@type": "Place", "name": f"{a['name']}, Chennai"} for a in C.AREAS if a["name"] != "Chennai"]
    return places


def business_node():
    node = {
        "@type": "ProfessionalService",
        "@id": BUSINESS_ID,
        "name": B["name"],
        "url": SITE + "/",
        "description": "Website design, website development, SEO and digital marketing services for businesses in Pallikaranai and across Chennai.",
        "telephone": B["phone_e164"],
        "image": f"{SITE}/{C.OG_IMAGE}",
        "logo": f"{SITE}/assets/icons/logo-512.png",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": f"{B['locality']}, {B['city']}",
            "addressRegion": B["region"],
            "postalCode": B["postal_code"],
            "addressCountry": B["country_code"],
        },
        "areaServed": area_served(),
        "employee": {"@type": "Person", "name": B["owner"], "jobTitle": "Owner"},
        "knowsAbout": ["Website design", "Website development", "Search engine optimisation", "Local SEO",
                       "Google Ads", "Social media marketing", "Content marketing", "E-commerce websites"],
    }
    if B["email"]:
        node["email"] = B["email"]
    same = [u for u in C.SOCIAL.values() if u]
    if same:
        node["sameAs"] = same
    return node


def website_node():
    return {"@type": "WebSite", "@id": WEBSITE_ID, "url": SITE + "/", "name": B["name"],
            "inLanguage": "en-IN", "publisher": {"@id": BUSINESS_ID}}


def webpage_node(page, kind="WebPage"):
    node = {"@type": kind, "@id": canonical(page["path"]) + "#webpage", "url": canonical(page["path"]),
            "name": page["title"], "description": page["description"], "inLanguage": "en-IN",
            "isPartOf": {"@id": WEBSITE_ID}}
    if page["key"] != "home":
        node["breadcrumb"] = {"@id": canonical(page["path"]) + "#breadcrumb"}
    return node


def breadcrumb_node(page, trail):
    items = []
    for i, (label, key) in enumerate(trail, 1):
        item = {"@type": "ListItem", "position": i, "name": label}
        item["item"] = canonical(REG[key]["path"]) if key else canonical(page["path"])
        items.append(item)
    return {"@type": "BreadcrumbList", "@id": canonical(page["path"]) + "#breadcrumb", "itemListElement": items}


def service_node(page, area=None):
    return {"@type": "Service", "@id": canonical(page["path"]) + "#service", "name": page["h1_plain"],
            "serviceType": page["service_type"], "description": page["description"],
            "url": canonical(page["path"]), "provider": {"@id": BUSINESS_ID},
            "areaServed": area or area_served()}


def faq_node(page, faqs):
    return {"@type": "FAQPage", "@id": canonical(page["path"]) + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer",
                                               "text": " ".join(plain(x) for x in (a if isinstance(a, list) else [a]))}}
                           for q, a in faqs]}


def jsonld(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/") + "\n</script>")


# ==========================================================================
# Page shell
# ==========================================================================
def page_shell(page, main_html, schema_nodes, preload="", topic=None, og_type="website", robots=None, base=None):
    title, desc = page["title"], page["description"]
    canon = canonical(page["path"])
    og_img = f"{SITE}/{C.OG_IMAGE}"
    robots = robots or "index, follow, max-image-preview:large, max-snippet:-1"
    base_tag = f'<base href="{base}">\n  ' if base else ""
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <!-- Kavitha Digital · page template V1 · generated by tools/build.py — edit copy in tools/content/, not here -->
  {base_tag}<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="{robots}">
  <!-- CANONICAL / OG / SCHEMA DOMAIN: set SITE_URL in tools/site_config.py, then rebuild. Currently: {SITE} -->
  <link rel="canonical" href="{canon}">
  <meta name="author" content="Kavitha Digital">
  <meta name="theme-color" content="#ffffff">
  <meta name="color-scheme" content="light">
  <meta name="format-detection" content="telephone=no">

  <!-- Open Graph -->
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Kavitha Digital">
  <meta property="og:locale" content="en_IN">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Kavitha Digital — website design, SEO and digital marketing in Pallikaranai, Chennai">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og_img}">

  <link rel="icon" href="{rel("assets/icons/favicon.svg")}" type="image/svg+xml">
  <link rel="icon" href="{rel("assets/icons/favicon-32.png")}" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="{rel("assets/icons/apple-touch-icon.png")}">
  {preload}
  <link rel="stylesheet" href="{asset("assets/css/style.css")}">
  <link rel="stylesheet" href="{asset("assets/css/responsive.css")}">
  <script>document.documentElement.classList.add('js')</script>
  <script src="{asset("assets/js/main.js")}" defer></script>
  {jsonld(schema_nodes)}
</head>
<body>
{header()}

<main id="main" tabindex="-1">
{main_html}
</main>
{footer()}
{floating(topic)}
</body>
</html>
'''


def page_hero(trail, eyebrow_text, h1, lead, actions="", image=None, image_alt=None, simple=False, extra=""):
    visual = ""
    grid_cls = "page-hero__grid"
    if image:
        grid_cls += " page-hero__grid--media"
        visual = (f'<div class="page-hero__visual">'
                  f'{picture(image, HERO_SIZES, eager=True, alt=image_alt)}</div>')
    cls = "page-hero page-hero--simple" if simple or not image else "page-hero"
    act = f'<div class="hero__actions">{actions}</div>' if actions else ""
    return f'''
<section class="{cls}">
  <div class="container">
    {breadcrumb(trail)}
    <div class="{grid_cls}">
      <div class="page-hero__content">
        <p class="eyebrow">{esc(eyebrow_text)}</p>
        <h1>{md(h1)}</h1>
        <p class="lead">{md(lead)}</p>
        {act}
        {extra}
      </div>
      {visual}
    </div>
  </div>
</section>'''


HOME_HERO_SIZES = "(min-width: 2560px) 760px, (min-width: 1920px) 660px, (min-width: 1240px) 560px, (min-width: 900px) 44vw, 92vw"
HERO_SIZES = "(min-width: 2560px) 700px, (min-width: 1920px) 620px, (min-width: 1240px) 520px, (min-width: 900px) 42vw, 92vw"


# ==========================================================================
# Templates
# ==========================================================================
def render_service(s):
    Ctx.sec = 0
    s["h1_plain"] = plain(s["h1"])
    # "parent" lets future clusters (e.g. /industries/) reuse this template with their own hub
    trail = [("Home", "home"), tuple(s.get("parent", ("Services", "services"))), (s["label"], None)]
    hero = page_hero(
        trail, s["eyebrow"], s["h1"], s["lead"],
        btn(s["cta"]["button"], url_of("contact"), "primary", None, "", "arrow-right") + call_btn(),
        s["image"], s["image_alt"])

    i = s["intro"]
    intro = f'''
<section class="section" aria-labelledby="intro-h">
  <div class="container split split--top">
    <div class="stack">
      {section_head("Overview", i["h2"], h2_id="intro-h")}
      {paras(i["paras"])}
    </div>
    <aside class="card sticky-col" data-reveal aria-label="{esc(i["audience_title"])}">
      <h3>{esc(i["audience_title"])}</h3>
      {checklist(i["audience"])}
    </aside>
  </div>
</section>'''

    pr = s["problems"]
    problems = f'''
<section class="section section--tint" aria-labelledby="problems-h">
  <div class="container">
    {section_head("Problems we solve", pr["h2"], pr.get("lead"), h2_id="problems-h")}
    <div class="grid grid--2" data-reveal-stagger>{"".join(problem(t, d) for t, d in pr["items"])}</div>
  </div>
</section>'''

    fe = s["features"]
    features = f'''
<section class="section" aria-labelledby="features-h">
  <div class="container">
    {section_head("What's included", fe["h2"], fe.get("lead"), h2_id="features-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(feature(ic, t, d) for ic, t, d in fe["items"])}</div>
  </div>
</section>'''

    be = s["benefits"]
    benefits = f'''
<section class="section section--dark" aria-labelledby="benefits-h">
  <div class="container split">
    <div class="stack">
      {section_head("Benefits", be["h2"], h2_id="benefits-h")}
      {paras(be["paras"])}
    </div>
    <div data-reveal>{checklist(be["items"])}</div>
  </div>
</section>'''

    p = s["process"]
    proc = f'''
<section class="section" aria-labelledby="process-h">
  <div class="container">
    {section_head("Our process", p["h2"], p.get("lead"), h2_id="process-h")}
    {process(p["steps"])}
  </div>
</section>'''

    w, lo = s["why"], s["local"]
    loc_links = "".join(f'<li><a class="chip" href="{url_of(k)}">{icon("map-pin")}{esc(REG[k]["short"])}</a></li>'
                        for k in lo["links"])
    why = f'''
<section class="section section--tint" aria-labelledby="why-h">
  <div class="container split split--top">
    <div class="stack">
      {section_head("Why Kavitha Digital", w["h2"], h2_id="why-h")}
      <div data-reveal>{checklist(w["items"])}</div>
    </div>
    <div class="card" data-reveal>
      <span class="icon-box">{icon("map-pin")}</span>
      <h3>{md(lo["h2"])}</h3>
      {paras(lo["paras"])}
      <ul class="chips">{loc_links}</ul>
    </div>
  </div>
</section>'''

    related = f'''
<section class="section" aria-labelledby="related-h">
  <div class="container">
    {section_head("Related services", s.get("related_h2", "Services that work well together"), h2_id="related-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(service_card(k) for k in s["related"])}</div>
  </div>
</section>'''

    faqs = f'''
<section class="section section--tint" aria-labelledby="faq-h">
  <div class="container">
    {section_head("FAQs", s.get("faq_h2", f"{s['label']} questions, answered"), h2_id="faq-h")}
    {faq_list(s["faqs"])}
  </div>
</section>'''

    cta = cta_band(s["cta"]["h2"], s["cta"]["text"], s["cta"]["button"], s["wa_text"])
    main = hero + intro + problems + features + benefits + proc + why + related + faqs + cta
    nodes = [business_node(), website_node(), webpage_node(s), breadcrumb_node(s, trail),
             service_node(s), faq_node(s, s["faqs"])]
    return page_shell(s, main, nodes, preload_image(s["image"], HERO_SIZES), s["wa_text"])


def render_location(l):
    Ctx.sec = 0
    l["h1_plain"] = plain(l["h1"])
    trail = [("Home", "home"), tuple(l.get("parent", ("Locations", "locations"))), (l["label"], None)]
    hero = page_hero(
        trail, l["eyebrow"], l["h1"], l["lead"],
        btn(l["cta"]["button"], url_of("contact"), "primary", None, "", "arrow-right") + call_btn(),
        l["image"], l["image_alt"])

    o = l["overview"]
    glance = "".join(f'<div><dt>{esc(k)}</dt><dd>{md(v)}</dd></div>' for k, v in o["glance"])
    overview = f'''
<section class="section" aria-labelledby="overview-h">
  <div class="container split split--top split--wide-left">
    <div class="stack">
      {section_head("Overview", o["h2"], h2_id="overview-h")}
      {paras(o["paras"])}
    </div>
    <aside class="profile sticky-col" data-reveal aria-label="At a glance">
      <h3>At a glance</h3>
      <dl>{glance}</dl>
      {btn("Discuss your project", url_of("contact"), "light", None, "", "arrow-right")}
    </aside>
  </div>
</section>'''

    bz = l["businesses"]
    businesses = f'''
<section class="section section--tint" aria-labelledby="biz-h">
  <div class="container">
    {section_head("Businesses we work with", bz["h2"], bz.get("lead"), h2_id="biz-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(feature(ic, t, d) for ic, t, d in bz["items"])}</div>
  </div>
</section>'''

    sv = l["services"]
    svc_cards = "".join(
        f'<article class="card card--link" data-reveal><span class="icon-box">{icon(REG[k]["icon"])}</span>'
        f'<h3><a class="card__link" href="{url_of(k)}">{esc(t)}</a></h3>{paras(d if isinstance(d, list) else [d])}'
        f'<span class="card__more link-arrow" aria-hidden="true">{esc(REG[k]["label"])} {icon("arrow-right")}</span></article>'
        for k, t, d in sv["items"])
    services = f'''
<section class="section" aria-labelledby="svc-h">
  <div class="container">
    {section_head("Services", sv["h2"], sv.get("lead"), h2_id="svc-h")}
    <div class="grid grid--3" data-reveal-stagger>{svc_cards}</div>
  </div>
</section>'''

    nb = l["nearby"]
    nearby = f'''
<section class="section section--dark" aria-labelledby="nearby-h">
  <div class="container split">
    <div class="stack">
      {section_head("Nearby areas", nb["h2"], h2_id="nearby-h")}
      {paras(nb["paras"])}
    </div>
    <div data-reveal>{chips(nb["areas"])}</div>
  </div>
</section>'''

    ap = l["approach"]
    approach = f'''
<section class="section" aria-labelledby="approach-h">
  <div class="container">
    {section_head("How we work", ap["h2"], ap.get("lead"), h2_id="approach-h")}
    {process(ap["steps"])}
  </div>
</section>'''

    faqs = f'''
<section class="section section--tint" aria-labelledby="faq-h">
  <div class="container">
    {section_head("FAQs", l.get("faq_h2", "Frequently asked questions"), h2_id="faq-h")}
    {faq_list(l["faqs"])}
  </div>
</section>'''

    related = f'''
<section class="section" aria-labelledby="rel-loc-h">
  <div class="container">
    {section_head("Related locations", "Other pages for businesses nearby", h2_id="rel-loc-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(location_card(k) for k in l["related_locations"])}</div>
    <div class="section-head mt-7" data-reveal>{eyebrow("Related services")}<h2 id="rel-svc-h">Services you may need next</h2></div>
    <div class="grid grid--3" data-reveal-stagger>{"".join(service_card(k) for k in l["related_services"])}</div>
  </div>
</section>'''

    cta = cta_band(l["cta"]["h2"], l["cta"]["text"], l["cta"]["button"], l["wa_text"])
    main = hero + overview + businesses + services + nearby + approach + faqs + related + cta
    nodes = [business_node(), website_node(), webpage_node(l), breadcrumb_node(l, trail),
             service_node(l, l["area_served"]), faq_node(l, l["faqs"])]
    return page_shell(l, main, nodes, preload_image(l["image"], HERO_SIZES), l["wa_text"])


def render_post_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{md(val)}</p>")
        elif kind in ("h2", "h3"):
            hid = re.sub(r"[^a-z0-9]+", "-", plain(val).lower()).strip("-")
            out.append(f'<{kind} id="{hid}">{md(val)}</{kind}>')
        elif kind in ("ul", "ol"):
            out.append(f"<{kind}>" + "".join(f"<li>{md(x)}</li>" for x in val) + f"</{kind}>")
        elif kind == "quote":
            out.append(f"<blockquote><p>{md(val)}</p></blockquote>")
        elif kind == "note":
            out.append(f'<div class="note">{icon("info")}<p>{md(val)}</p></div>')
    return "\n".join(out)


def render_post(p):
    Ctx.sec = 0
    trail = [("Home", "home"), ("Blog", "blog"), (p["label"], None)]
    meta = (f'<p class="post-meta"><span>By Kavitha Digital</span><span>Published {fmt_date(p["date"])}</span>'
            f'<span>{esc(p["read"])}</span></p>')
    hero = page_hero(trail, p["category"], p["h1"], p["excerpt"], "", None, None, True, meta)
    svc_links = "".join(f'<li><a href="{url_of(k)}">{esc(REG[k]["label"])}</a></li>' for k in p["related_services"])
    body = f'''
<section class="section section--flush-top">
  <div class="container">
    <div class="post-cover" data-reveal="fade">{picture(p["image"], "(min-width: 2560px) 1500px, (min-width: 1920px) 1340px, (min-width: 1240px) 1180px, 94vw", eager=True)}</div>
    <div class="post-layout mt-7">
      <article class="prose">
        {render_post_body(p["body"])}
      </article>
      <aside class="post-aside" aria-label="Related services">
        <div class="card aside-card">
          <h2>Related services</h2>
          <ul>{svc_links}</ul>
        </div>
        <div class="profile">
          <h2 class="h3">Talk to Harish</h2>
          <p>Questions about your own website or Google visibility? Call or WhatsApp for a free first conversation.</p>
          {btn(f"Call {B['phone_short']}", tel(), "light", "phone")}
          {wa_btn("WhatsApp", p["category"].lower(), "outline-light")}
        </div>
      </aside>
    </div>
  </div>
</section>'''
    more = [k for k in BLOG.ORDER if k != p["key"]][:2]
    related = f'''
<section class="section section--tint" aria-labelledby="more-h">
  <div class="container">
    {section_head("Keep reading", "More from the Kavitha Digital blog", h2_id="more-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(blog_card(k) for k in more)}{service_card(p["related_services"][0])}</div>
  </div>
</section>'''
    cta = cta_band(p["cta"]["h2"], p["cta"]["text"], p["cta"]["button"], p["category"].lower())
    posting = {"@type": "BlogPosting", "@id": canonical(p["path"]) + "#article", "headline": plain(p["h1"]),
               "description": p["description"], "datePublished": p["date"], "dateModified": p.get("modified", p["date"]),
               "image": f'{SITE}/assets/images/blog/{p["image"]}.webp', "inLanguage": "en-IN",
               "author": {"@id": BUSINESS_ID}, "publisher": {"@id": BUSINESS_ID},
               "mainEntityOfPage": {"@id": canonical(p["path"]) + "#webpage"}, "articleSection": p["category"]}
    nodes = [business_node(), website_node(), webpage_node(p), breadcrumb_node(p, trail), posting]
    pre = preload_image(p["image"], "(min-width: 2560px) 1500px, (min-width: 1920px) 1340px, (min-width: 1240px) 1180px, 94vw")
    return page_shell(p, hero + body + related + cta, nodes, pre, p["category"].lower(), "article")


# ---- Custom pages -----------------------------------------------------------
def render_home(page):
    Ctx.sec = 0
    h = HOME.HOME
    hero = f'''
<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <p class="eyebrow">{esc(h["hero"]["eyebrow"])}</p>
      <h1>{h["hero"]["h1"]}</h1>
      <p class="hero__lead">{md(h["hero"]["lead"])}</p>
      <div class="hero__actions">
        {btn("Get a Free Consultation", url_of("contact"), "primary", None, "", "arrow-right")}
        {call_btn()}
      </div>
      <ul class="trust-list">{"".join(f"<li>{icon('badge-check')}<span>{esc(t)}</span></li>" for t in h["hero"]["trust"])}</ul>
    </div>
    <div class="hero__visual">
      {picture(h["hero"]["image"], HOME_HERO_SIZES, eager=True)}
      <div class="hero__badge">{icon("user")}<span><strong>Work directly with Harish</strong><br>Owner, Kavitha Digital</span></div>
    </div>
  </div>
</section>'''

    sv = h["services"]
    services = f'''
<section class="section" id="services" aria-labelledby="services-h">
  <div class="container">
    {section_head("Services", sv["h2"], sv["lead"], h2_id="services-h")}
    <div class="grid grid--4" data-reveal-stagger>{"".join(service_card(k) for k in sv["keys"])}</div>
    <p class="mt-6" data-reveal><a class="link-arrow" href="{url_of("services")}">See all 11 services, including content marketing and graphic design {icon("arrow-right")}</a></p>
  </div>
</section>'''

    wy = h["why"]
    why = f'''
<section class="section section--tint" aria-labelledby="why-h">
  <div class="container split split--top split--wide-right">
    <div class="stack">
      {section_head("Why Kavitha Digital", wy["h2"], h2_id="why-h")}
      {paras(wy["paras"])}
      <p data-reveal>{btn("About Kavitha Digital", url_of("about"), "ghost", None, "", "arrow-right")}</p>
    </div>
    <div class="grid grid--2" data-reveal-stagger>{"".join(feature(ic, t, d) for ic, t, d in wy["items"])}</div>
  </div>
</section>'''

    pr = h["process"]
    proc = f'''
<section class="section" aria-labelledby="process-h">
  <div class="container">
    {section_head("Web design process", pr["h2"], pr["lead"], h2_id="process-h")}
    {process(pr["steps"])}
  </div>
</section>'''

    dm = h["seo_dm"]
    channel_cards = "".join(
        f'<article class="card card--link card--glass" data-reveal><span class="icon-box icon-box--solid">{icon(REG[k]["icon"])}</span>'
        f'<h3><a class="card__link" href="{url_of(k)}">{esc(t)}</a></h3><p>{md(d)}</p></article>'
        for k, t, d in dm["channels"])
    seo_dm = f'''
<section class="section section--dark" aria-labelledby="seo-dm-h">
  <div class="container">
    <div class="split split--top">
      <div class="stack">
        {section_head("SEO & digital marketing", dm["h2"], h2_id="seo-dm-h")}
        {paras(dm["paras"])}
        <p data-reveal>{btn("Improve your Google visibility", url_of("svc-seo"), "light", None, "", "arrow-right")}</p>
      </div>
      <div class="grid grid--2" data-reveal-stagger>{channel_cards}</div>
    </div>
  </div>
</section>'''

    ind = h["industries"]
    industries = f'''
<section class="section" aria-labelledby="industries-h">
  <div class="container">
    {section_head("Industries", ind["h2"], ind["lead"], h2_id="industries-h")}
    <ul class="grid grid--4 industries" data-reveal-stagger role="list">{"".join(f'<li class="industry" data-reveal>{icon(ic)}<span>{esc(t)}</span></li>' for ic, t in ind["items"])}</ul>
  </div>
</section>'''

    pf = h["portfolio"]
    port_cards = "".join(
        f'<article class="card card--media portfolio-card" data-reveal>'
        f'<div class="card__media">{picture(it["image"], "(min-width: 2560px) 500px, (min-width: 1920px) 440px, (min-width: 900px) 380px, (min-width: 640px) 45vw, 92vw")}</div>'
        f'<div class="card__body"><span class="tag tag--muted">Illustrative concept</span><h3>{esc(it["title"])}</h3>'
        f'<p>{md(it["text"])}</p></div></article><!-- PLACEHOLDER: replace with a real, client-approved project -->'
        for it in pf["items"])
    portfolio = f'''
<section class="section section--tint" aria-labelledby="work-h">
  <div class="container">
    {section_head("Recent work", pf["h2"], pf["lead"], h2_id="work-h")}
    <div class="grid grid--3" data-reveal-stagger>{port_cards}</div>
  </div>
</section>'''

    st = h["stats"]
    stats_html = "".join(
        f'<div class="stat" data-reveal><span class="stat__value" data-count="{v}" data-suffix="{sfx}">{v}{sfx}</span>'
        f'<span class="stat__label">{esc(lbl)}</span></div>' for v, sfx, lbl in st["items"])
    stats = f'''
<section class="section section--dark section--tight" aria-labelledby="stats-h">
  <div class="container">
    {section_head("At a glance", st["h2"], h2_id="stats-h")}
    <div class="stats" data-reveal-stagger>{stats_html}</div>
    <!-- PLACEHOLDER: when verified figures exist (projects delivered, years in business), add them in tools/content/home.py -->
  </div>
</section>'''

    lc = h["locations"]
    locations = f'''
<section class="section" aria-labelledby="locations-h">
  <div class="container">
    {section_head("Locations served", lc["h2"], lc["lead"], h2_id="locations-h")}
    <div data-reveal>{chips(C.AREAS)}</div>
    <div class="grid grid--2 mt-6" data-reveal-stagger>{location_card("loc-pallikaranai")}{location_card("loc-chennai-digital-marketing")}</div>
  </div>
</section>'''

    ts = h["testimonials"]
    t_cards = "".join(
        f'<figure class="card testimonial testimonial--placeholder" data-reveal>{icon("quote", "quote-mark")}'
        f'<blockquote><p>{esc(t)}</p></blockquote>'
        f'<figcaption class="testimonial__who"><span class="testimonial__avatar" aria-hidden="true">{icon("user")}</span>'
        f'<span><span class="testimonial__name">Client review slot</span><br><span class="testimonial__role">Name, business and area</span></span></figcaption></figure>'
        f'<!-- PLACEHOLDER: replace with a genuine, permission-granted client review -->' for t in ts["slots"])
    testimonials = f'''
<section class="section section--tint" aria-labelledby="reviews-h">
  <div class="container">
    {section_head("Client feedback", ts["h2"], ts["lead"], h2_id="reviews-h")}
    <div class="grid grid--3" data-reveal-stagger>{t_cards}</div>
  </div>
</section>'''

    faq = f'''
<section class="section" aria-labelledby="faq-h">
  <div class="container split split--top split--wide-right">
    <div class="stack">
      {section_head("FAQs", h["faq_h2"], h2_id="faq-h")}
      <p data-reveal>More answers on our <a href="{url_of("faq")}">frequently asked questions page</a>, or ask Harish directly.</p>
      <p data-reveal>{call_btn()}</p>
    </div>
    {faq_list(h["faqs"])}
  </div>
</section>'''

    cta = cta_band(h["cta"]["h2"], h["cta"]["text"], "Get a Free Consultation")

    contact = f'''
<section class="section section--flush-top" aria-labelledby="contact-h">
  <div class="container">
    {section_head("Contact", "Talk to Kavitha Digital", "Based in Pallikaranai, Chennai. Call, WhatsApp or send an enquiry — you will speak to Harish.", h2_id="contact-h")}
    <div class="grid grid--4" data-reveal-stagger>{contact_cards()}</div>
  </div>
</section>'''

    main = hero + services + why + proc + seo_dm + industries + portfolio + stats + locations + testimonials + faq + cta + contact
    nodes = [business_node(), website_node(), webpage_node(page), faq_node(page, h["faqs"])]
    pre = preload_image(h["hero"]["image"], HOME_HERO_SIZES)
    return page_shell(page, main, nodes, pre)


def render_about(page):
    Ctx.sec = 0
    a = PAGES.ABOUT
    trail = [("Home", "home"), ("About Us", None)]
    hero = page_hero(trail, a["eyebrow"], a["h1"], a["lead"],
                     btn("Talk to Harish", url_of("contact"), "primary", None, "", "arrow-right") + call_btn(),
                     a["image"], a["image_alt"])
    profile = f'''
<section class="section" aria-labelledby="who-h">
  <div class="container split split--top split--wide-left">
    <div class="stack">
      {section_head("Who we are", a["who"]["h2"], h2_id="who-h")}
      {paras(a["who"]["paras"])}
      <!-- PLACEHOLDER: add Harish's background, qualifications and verified years of experience here -->
    </div>
    <aside class="profile sticky-col" data-reveal aria-label="Business details">
      <span class="profile__monogram" aria-hidden="true">H</span>
      <h3>Harish</h3>
      <dl>
        <div><dt>Role</dt><dd>Owner, Kavitha Digital</dd></div>
        <div><dt>Based in</dt><dd>{esc(C.ADDRESS_LINE)}</dd></div>
        <div><dt>Phone / WhatsApp</dt><dd><a href="{tel()}">{B["phone_display"]}</a></dd></div>
        <div><dt>Works with</dt><dd>Businesses in Pallikaranai and across Chennai</dd></div>
      </dl>
    </aside>
  </div>
</section>'''
    focus = f'''
<section class="section section--tint" aria-labelledby="focus-h">
  <div class="container">
    {section_head("What we focus on", a["focus"]["h2"], a["focus"]["lead"], h2_id="focus-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(feature(ic, t, d) for ic, t, d in a["focus"]["items"])}</div>
  </div>
</section>'''
    how = f'''
<section class="section section--dark" aria-labelledby="how-h">
  <div class="container split">
    <div class="stack">
      {section_head("How we work", a["how"]["h2"], h2_id="how-h")}
      {paras(a["how"]["paras"])}
    </div>
    <div data-reveal>{checklist(a["how"]["items"])}</div>
  </div>
</section>'''
    proc = f'''
<section class="section" aria-labelledby="process-h">
  <div class="container">
    {section_head("Our process", a["process"]["h2"], a["process"]["lead"], h2_id="process-h")}
    {process(a["process"]["steps"])}
  </div>
</section>'''
    who_for = f'''
<section class="section section--tint" aria-labelledby="clients-h">
  <div class="container split split--top">
    <div class="stack">
      {section_head("Who we work with", a["clients"]["h2"], h2_id="clients-h")}
      {paras(a["clients"]["paras"])}
    </div>
    <div class="stack" data-reveal>{chips(C.AREAS)}
      <div class="note">{icon("info")}<p>{md(a["clients"]["note"])}</p></div>
    </div>
  </div>
</section>'''
    cta = cta_band(a["cta"]["h2"], a["cta"]["text"], "Get a Free Consultation")
    main = hero + profile + focus + how + proc + who_for + cta
    nodes = [business_node(), website_node(), webpage_node(page, "AboutPage"), breadcrumb_node(page, trail)]
    return page_shell(page, main, nodes, preload_image(a["image"], HERO_SIZES))


def render_services_hub(page):
    Ctx.sec = 0
    d = PAGES.SERVICES_HUB
    trail = [("Home", "home"), ("Services", None)]
    hero = page_hero(trail, d["eyebrow"], d["h1"], d["lead"],
                     btn("Get a Website Quote", url_of("contact"), "primary", None, "", "arrow-right") + call_btn(),
                     d["image"], d["image_alt"])
    groups = ""
    for (gname, keys), (gh2, glead) in zip(SERVICE_GROUPS, d["groups"]):
        slug = gname.lower()
        groups += f'''
<section class="section{' section--tint' if slug == 'grow' else ''}" aria-labelledby="{slug}-h">
  <div class="container">
    {section_head(gname, gh2, glead, h2_id=f"{slug}-h")}
    <div class="grid grid--{ {2: 2, 4: 4}.get(len(keys), 3) }" data-reveal-stagger>{"".join(service_card(k) for k in keys)}</div>
  </div>
</section>'''
    how = f'''
<section class="section section--dark" aria-labelledby="choose-h">
  <div class="container split">
    <div class="stack">
      {section_head("Choosing services", d["choose"]["h2"], h2_id="choose-h")}
      {paras(d["choose"]["paras"])}
    </div>
    <div data-reveal>{checklist(d["choose"]["items"])}</div>
  </div>
</section>'''
    faqs = f'''
<section class="section" aria-labelledby="faq-h">
  <div class="container">
    {section_head("FAQs", "Questions about our services", h2_id="faq-h")}
    {faq_list(d["faqs"])}
  </div>
</section>'''
    cta = cta_band(d["cta"]["h2"], d["cta"]["text"], "Discuss Your Website")
    item_list = {"@type": "ItemList", "@id": canonical(page["path"]) + "#services",
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": canonical(REG[k]["path"]),
                                      "name": REG[k]["label"]}
                                     for i, k in enumerate([k for _, ks in SERVICE_GROUPS for k in ks])]}
    nodes = [business_node(), website_node(), webpage_node(page, "CollectionPage"), breadcrumb_node(page, trail),
             item_list, faq_node(page, d["faqs"])]
    return page_shell(page, hero + groups + how + faqs + cta, nodes, preload_image(d["image"], HERO_SIZES))


def render_locations_hub(page):
    Ctx.sec = 0
    d = PAGES.LOCATIONS_HUB
    trail = [("Home", "home"), ("Locations", None)]
    hero = page_hero(trail, d["eyebrow"], d["h1"], d["lead"],
                     btn("Talk to a Website Expert", url_of("contact"), "primary", None, "", "arrow-right") + call_btn(),
                     d["image"], d["image_alt"])
    groups = ""
    for (gname, keys), (gh2, glead) in zip(LOCATION_GROUPS, d["groups"]):
        slug = gname.lower()
        groups += f'''
<section class="section{' section--tint' if slug != 'chennai' else ''}" id="{slug}" aria-labelledby="{slug}-h">
  <div class="container">
    {section_head(gname, gh2, glead, h2_id=f"{slug}-h")}
    <div class="grid grid--3" data-reveal-stagger>{"".join(location_card(k) for k in keys)}</div>
  </div>
</section>'''
    areas = f'''
<section class="section section--dark" aria-labelledby="areas-h">
  <div class="container split">
    <div class="stack">
      {section_head("Areas we serve", d["areas"]["h2"], h2_id="areas-h")}
      {paras(d["areas"]["paras"])}
    </div>
    <div data-reveal>{chips(C.AREAS)}</div>
  </div>
</section>'''
    faqs = f'''
<section class="section" aria-labelledby="faq-h">
  <div class="container">
    {section_head("FAQs", "Working with a Pallikaranai-based agency", h2_id="faq-h")}
    {faq_list(d["faqs"])}
  </div>
</section>'''
    cta = cta_band(d["cta"]["h2"], d["cta"]["text"], "Get a Free Consultation")
    nodes = [business_node(), website_node(), webpage_node(page, "CollectionPage"), breadcrumb_node(page, trail),
             faq_node(page, d["faqs"])]
    return page_shell(page, hero + groups + areas + faqs + cta, nodes, preload_image(d["image"], HERO_SIZES))


def render_blog(page):
    Ctx.sec = 0
    d = PAGES.BLOG_INDEX
    trail = [("Home", "home"), ("Blog", None)]
    hero = page_hero(trail, d["eyebrow"], d["h1"], d["lead"], "", None, None, True)
    cats = sorted({(REG[k]["cat_slug"], REG[k]["category"]) for k in BLOG.ORDER}, key=lambda x: x[1])
    filters = ('<div class="filter-bar" data-filter-bar hidden><p class="visually-hidden" id="filter-label">Filter articles by topic</p>'
               '<ul class="chips" aria-labelledby="filter-label"><li><button class="chip" type="button" data-filter="all" aria-pressed="true">All articles</button></li>'
               + "".join(f'<li><button class="chip" type="button" data-filter="{s}" aria-pressed="false">{esc(n)}</button></li>' for s, n in cats)
               + '</ul><p class="visually-hidden" data-filter-status aria-live="polite"></p></div>')
    posts = f'''
<section class="section section--flush-top" aria-labelledby="latest-h">
  <div class="container">
    <h2 class="visually-hidden" id="latest-h">Latest articles</h2>
    {filters}
    <div class="grid grid--3" data-reveal-stagger>{"".join(blog_card(k) for k in BLOG.ORDER)}</div>
  </div>
</section>'''
    topics = f'''
<section class="section section--tint" aria-labelledby="topics-h">
  <div class="container split split--top">
    <div class="stack">
      {section_head("Topics", d["topics"]["h2"], h2_id="topics-h")}
      {paras(d["topics"]["paras"])}
    </div>
    <div data-reveal><ul class="chips">{"".join(f'<li><span class="chip">{esc(t)}</span></li>' for t in d["topics"]["list"])}</ul></div>
  </div>
</section>'''
    cta = cta_band(d["cta"]["h2"], d["cta"]["text"], "Talk to a Website Expert")
    blog_node = {"@type": "Blog", "@id": canonical(page["path"]) + "#blog", "name": "Kavitha Digital Blog",
                 "url": canonical(page["path"]), "publisher": {"@id": BUSINESS_ID}, "inLanguage": "en-IN",
                 "blogPost": [{"@id": canonical(REG[k]["path"]) + "#article"} for k in BLOG.ORDER]}
    nodes = [business_node(), website_node(), webpage_node(page, "CollectionPage"), breadcrumb_node(page, trail), blog_node]
    return page_shell(page, hero + posts + topics + cta, nodes)


def render_faq(page):
    Ctx.sec = 0
    d = PAGES.FAQ_PAGE
    trail = [("Home", "home"), ("FAQ", None)]
    jump = "".join(f'<li><a class="chip" href="#{g["id"]}">{esc(g["title"])}</a></li>' for g in d["groups"])
    hero = page_hero(trail, d["eyebrow"], d["h1"], d["lead"], "", None, None, True,
                     f'<nav aria-label="FAQ topics"><ul class="chips">{jump}</ul></nav>')
    groups = "".join(
        f'<div class="faq-group" id="{g["id"]}"><h2>{esc(g["title"])}</h2>{faq_list(g["items"])}</div>'
        for g in d["groups"])
    body = f'''
<section class="section section--flush-top">
  <div class="container split split--top split--wide-left">
    <div>{groups}</div>
    <aside class="profile sticky-col" aria-label="Still have a question?">
      <h2 class="h3">Still have a question?</h2>
      <p>Harish answers every enquiry personally. Share a little about your business and what you want to achieve.</p>
      {btn(f"Call {B['phone_short']}", tel(), "light", "phone")}
      {wa_btn("WhatsApp", "a question I have", "outline-light")}
      <a class="link-arrow link-arrow--light" href="{url_of("contact")}">Send an enquiry {icon("arrow-right")}</a>
    </aside>
  </div>
</section>'''
    cta = cta_band(d["cta"]["h2"], d["cta"]["text"], "Get a Free Consultation")
    all_faqs = [x for g in d["groups"] for x in g["items"]]
    nodes = [business_node(), website_node(), webpage_node(page), breadcrumb_node(page, trail), faq_node(page, all_faqs)]
    return page_shell(page, hero + body + cta, nodes)


def render_contact(page):
    Ctx.sec = 0
    d = PAGES.CONTACT
    trail = [("Home", "home"), ("Contact", None)]
    hero = page_hero(trail, d["eyebrow"], d["h1"], d["lead"],
                     call_btn(f"Call {B['phone_short']}", "primary") + wa_btn("WhatsApp Harish"), None, None, True)
    endpoint = C.FORM_ENDPOINT.strip()
    if endpoint:
        form_attrs = f'action="{esc(endpoint)}" method="post"'
        msg_name = "message"
        submit_label = "Send enquiry"
        hint = "Your details are sent securely to Kavitha Digital and used only to reply to this enquiry."
    else:
        form_attrs = f'action="https://wa.me/{B["whatsapp"]}" method="get" target="_blank"'
        msg_name = "text"
        submit_label = "Send enquiry via WhatsApp"
        hint = "Pressing send opens WhatsApp with your enquiry filled in — just tap Send. Your details go only to Harish."
    access_key = (f'<input type="hidden" name="access_key" value="{esc(C.WEB3FORMS_ACCESS_KEY)}">'
                  if C.WEB3FORMS_ACCESS_KEY else "")
    options = "".join(f'<option value="{esc(REG[k]["label"])}">{esc(REG[k]["label"])}</option>'
                      for _, ks in SERVICE_GROUPS for k in ks)
    form = f'''
<form class="form" {form_attrs} data-contact-form data-endpoint="{esc(endpoint)}" data-whatsapp="{B["whatsapp"]}" data-phone="{B["phone_short"]}" aria-describedby="form-hint">
  <!-- FORM SERVICE: set FORM_ENDPOINT in tools/site_config.py (Formspree, Web3Forms, Netlify Forms or your API) and rebuild -->
  {access_key}
  <input type="hidden" name="subject" value="New enquiry from the Kavitha Digital website">
  <div class="visually-hidden" aria-hidden="true"><label for="f-gotcha">Leave this field empty</label><input id="f-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="form__row">
    <div class="field">
      <label for="f-name">Your name</label>
      <input id="f-name" name="name" type="text" autocomplete="name" required maxlength="80">
      <p class="field__error" id="f-name-err">Please enter your name.</p>
    </div>
    <div class="field">
      <label for="f-phone">Phone / WhatsApp number</label>
      <input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required pattern="[0-9+()\\s-]{{10,16}}" maxlength="16">
      <p class="field__error" id="f-phone-err">Please enter a valid phone number (10 digits or with +91).</p>
    </div>
  </div>
  <div class="form__row">
    <div class="field">
      <label for="f-email">Email <span class="optional">(optional)</span></label>
      <input id="f-email" name="email" type="email" autocomplete="email" maxlength="120">
      <p class="field__error" id="f-email-err">Please check your email address.</p>
    </div>
    <div class="field">
      <label for="f-business">Business name <span class="optional">(optional)</span></label>
      <input id="f-business" name="business" type="text" autocomplete="organization" maxlength="100">
    </div>
  </div>
  <div class="field">
    <label for="f-service">What do you need help with?</label>
    <select id="f-service" name="service" required>
      <option value="">Choose a service</option>
      {options}
      <option value="Not sure yet">Not sure yet — I'd like advice</option>
    </select>
    <p class="field__error" id="f-service-err">Please choose an option.</p>
  </div>
  <div class="field">
    <label for="f-message">Tell us about your project</label>
    <textarea id="f-message" name="{msg_name}" required minlength="10" maxlength="2000" placeholder="For example: we are a clinic in Velachery and need a new website that brings in appointment calls."></textarea>
    <p class="field__error" id="f-message-err">Please add a few words about your project.</p>
  </div>
  <label class="checkbox"><input type="checkbox" name="consent" value="yes" required> <span>I agree that Kavitha Digital may contact me about this enquiry. See the <a href="{url_of("privacy")}">privacy policy</a>.</span></label>
  <p class="field__hint" id="form-hint">{hint}</p>
  <button class="btn btn--primary btn--block" type="submit">{icon("whatsapp") if not endpoint else ""}<span>{submit_label}</span></button>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>'''
    next_steps = process(d["next"], stack=True)
    body = f'''
<section class="section section--flush-top" aria-labelledby="form-h">
  <div class="container contact-layout">
    <div class="stack-lg">
      <div class="grid grid--2" data-reveal-stagger>{contact_cards("h2")}</div>
      <div class="card" data-reveal>
        <h2 class="h3">What happens after you get in touch</h2>
        {next_steps}
      </div>
    </div>
    <div class="form-card" data-reveal>
      <h2 id="form-h">Send an enquiry</h2>
      <p class="text-muted mt-4">Share a few details and Harish will get back to you. Prefer to talk? Call <a href="{tel()}">{B["phone_display"]}</a>.</p>
      <div class="mt-6">{form}</div>
    </div>
  </div>
</section>'''
    faqs = f'''
<section class="section section--tint" aria-labelledby="faq-h">
  <div class="container">
    {section_head("Before you call", "Common questions about getting started", h2_id="faq-h", numbered=False)}
    {faq_list(d["faqs"])}
  </div>
</section>'''
    contact_node = {"@type": "ContactPage", "@id": canonical(page["path"]) + "#webpage", "url": canonical(page["path"]),
                    "name": page["title"], "description": page["description"], "inLanguage": "en-IN",
                    "isPartOf": {"@id": WEBSITE_ID}, "about": {"@id": BUSINESS_ID},
                    "breadcrumb": {"@id": canonical(page["path"]) + "#breadcrumb"}}
    nodes = [business_node(), website_node(), contact_node, breadcrumb_node(page, trail), faq_node(page, d["faqs"])]
    return page_shell(page, hero + body + faqs, nodes)


def render_legal(page):
    Ctx.sec = 0
    d = PAGES.LEGAL[page["key"]]
    trail = [("Home", "home"), (page["label"], None)]
    hero = page_hero(trail, "Legal", d["h1"], d["lead"], "", None, None, True,
                     f'<p class="post-meta"><span>Last updated {fmt_date(d["updated"])}</span></p>')
    body = f'''
<section class="section section--flush-top">
  <div class="container">
    <article class="prose">{render_post_body(d["body"])}</article>
  </div>
</section>'''
    nodes = [business_node(), website_node(), webpage_node(page), breadcrumb_node(page, trail)]
    return page_shell(page, hero + body, nodes)


def render_404(page):
    Ctx.sec = 0
    Ctx.base_mode = True
    base = (urlparse(SITE).path.rstrip("/") + "/") or "/"
    d = PAGES.NOT_FOUND
    links = "".join(f'<li><a class="chip" href="{url_of(k)}">{esc(t)}</a></li>' for k, t in d["links"])
    main = f'''
<section class="page-hero page-hero--simple">
  <div class="container">
    <div class="page-hero__grid">
      <div class="page-hero__content">
        <p class="error-code text-gradient" aria-hidden="true">404</p>
        <h1>{esc(d["h1"])}</h1>
        <p class="lead">{md(d["lead"])}</p>
        <div class="hero__actions">{btn("Back to the home page", url_of("home"), "primary", None, "", "arrow-right")}{call_btn()}</div>
      </div>
    </div>
  </div>
</section>
<section class="section section--flush-top" aria-labelledby="popular-h">
  <div class="container">
    <h2 id="popular-h" class="h3">Popular pages</h2>
    <ul class="chips mt-5">{links}</ul>
    <div class="grid grid--4 mt-7">{"".join(service_card(k) for k in ["svc-website-design", "svc-seo", "svc-google-ads", "svc-local-seo"])}</div>
  </div>
</section>'''
    html_out = page_shell(page, main, [website_node()], robots="noindex, follow", base=base)
    Ctx.base_mode = False
    return html_out


CUSTOM = {
    "home": render_home, "about": render_about, "services": render_services_hub,
    "locations": render_locations_hub, "blog": render_blog, "faq": render_faq,
    "contact": render_contact, "privacy": render_legal, "terms": render_legal, "404": render_404,
}


# ==========================================================================
# Build
# ==========================================================================
def render(page):
    Ctx.path = page["path"]
    Ctx.section = section_of(page)
    t = page.get("type")
    if t == "service":
        return render_service(page)
    if t == "location":
        return render_location(page)
    if t == "post":
        return render_post(page)
    return CUSTOM[page["key"]](page)


def write_sitemap(pages):
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        urls.append(f"  <url>\n    <loc>{canonical(p['path'])}</loc>\n    <lastmod>{p.get('modified', TODAY)}</lastmod>\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<!-- Generated by tools/build.py on {TODAY}. Domain comes from SITE_URL in tools/site_config.py -->\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    return len(urls)


def write_robots():
    (ROOT / "robots.txt").write_text(
        "# Kavitha Digital — robots.txt (generated by tools/build.py)\n"
        "User-agent: *\nAllow: /\nDisallow: /tools/\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


def main():
    pages = list(REG.values())
    for page in pages:
        out = ROOT / page["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page), encoding="utf-8")
    n = write_sitemap(pages)
    write_robots()
    print(f"Built {len(pages)} pages, sitemap with {n} URLs.")
    if "example.com" in SITE:
        print("\n  WARNING: SITE_URL is still the example.com placeholder.\n"
              "  Set the real domain in tools/site_config.py and rebuild before launch.\n")


if __name__ == "__main__":
    main()
