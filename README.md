# Kavitha Digital — website (V1)

Static website for **Kavitha Digital**, Pallikaranai, Chennai – 600100 (owner: Harish, +91 94459 78150).
Plain HTML5, CSS3 and vanilla JavaScript. No frameworks, no build step on the server, no database —
upload to GitHub, switch on GitHub Pages, done.

---

## File versions

| File | Version | What it is |
|---|---|---|
| `assets/css/style.css` | V1 | Design system: variables, Helvetica type scale, components |
| `assets/css/responsive.css` | V1 | Every breakpoint, 320px phones → 4K screens |
| `assets/js/main.js` | V1 | Menu, dropdowns, scroll reveal, counters, FAQ, form, back-to-top |
| `tools/build.py` | V1 | Page generator: header, footer, breadcrumbs, schema, sitemap, robots |
| `tools/site_config.py` | V1 | Business details, domain, form endpoint, social links |
| `tools/icons.py` | V1 | Inline SVG icon set |
| `tools/check_site.py` | V1 | Pre-launch audit (links, titles, H1s, schema, phone numbers…) |
| `tools/content/*.py` | V1 | All page copy (home, services, locations, blog, pages, images) |
| All `.html` pages | V1 | Generated — edit `tools/content/`, then rebuild |

When you change a file, bump its version in the header comment (V2, V3 …) and in this table.

---

## Before going live — checklist

1. **Domain** — set `SITE_URL` in `tools/site_config.py` (e.g. `https://www.kavithadigital.in`), then run
   `python3 tools/build.py`. Canonicals, Open Graph, schema, `sitemap.xml` and `robots.txt` all update.
   *example.com must never go live.* For a custom domain also add a `CNAME` file containing the bare domain.
2. **Email** — set `BUSINESS["email"]`. Until then the site shows "Email address coming soon".
3. **Contact form** — works today by handing the enquiry to WhatsApp. To receive emails instead, set
   `FORM_ENDPOINT` (Formspree `https://formspree.io/f/…`, or Web3Forms with `WEB3FORMS_ACCESS_KEY`).
4. **Social profiles** — fill `SOCIAL` in `site_config.py`; empty ones are never shown or added to schema.
5. **Real proof** — replace the placeholders marked `PLACEHOLDER` in `tools/content/home.py` and
   `pages.py`: testimonials (genuine, with permission), portfolio concepts → real projects,
   Harish's background and verified years in business.
6. **Photos** — the images are brand illustrations. Replace any with real photos at the same size and file
   name (see *Images*). Update the ALT text in `tools/content/images.py`.
7. **Legal** — `legal/privacy-policy.html` and `legal/terms-of-use.html` are starting drafts. Have them
   reviewed; add the grievance email once `BUSINESS["email"]` is set.
8. **Business commitments** — check statements such as "accounts set up in your business's name" and
   "ad spend and management fees kept separate" match how you actually work. Edit in `tools/content/`.
9. **Google** — make the name, address and phone identical to the Google Business Profile, then submit
   `sitemap.xml` in Google Search Console.
10. Run `python3 tools/check_site.py` — it must report **0 errors**.

---

## Publish on GitHub Pages

1. Create a repository (e.g. `harishmkavitha/kavitha-digital`) and upload **everything in this folder**,
   including the hidden `.nojekyll` file.
2. Settings → Pages → *Deploy from a branch* → `main` / `(root)` → Save.
3. The site appears at `https://harishmkavitha.github.io/kavitha-digital/` within a minute or two.
4. After changing CSS or JS, bump `ASSET_VERSION` in `site_config.py` and rebuild so browsers fetch the new files.

All links are relative, so the site works on a project URL, a custom domain, or opened straight from disk.
`404.html` uses a `<base>` tag derived from `SITE_URL`, so it also works at any depth.

---

## Editing content

```bash
python3 tools/build.py        # regenerate every page, sitemap.xml and robots.txt
python3 tools/check_site.py   # audit — run before every upload
```

Python 3.8+ only, no packages to install. **Never edit the generated `.html` files directly** — the next
build overwrites them. Page copy lives in:

| File | Pages |
|---|---|
| `tools/content/home.py` | Home page |
| `tools/content/services.py` | 11 service pages |
| `tools/content/locations.py` | 4 location pages |
| `tools/content/blog.py` | Blog posts |
| `tools/content/pages.py` | About, services hub, locations hub, blog index, FAQ, contact, legal, 404 — plus titles and descriptions |
| `tools/content/images.py` | Image sizes and ALT text |
| `tools/site_config.py` | Phone, address, domain, form, social links, areas served |

**Internal links in content:** write `[anchor text](@page-key)` — the build turns it into the correct
relative link for each folder depth. An unknown key stops the build, so broken links can't be published.
`{PHONE}` inserts the clickable phone number.

### Page keys

| Key | Page |
|---|---|
| `home`, `about`, `contact`, `faq`, `blog`, `privacy`, `terms` | Core pages |
| `services`, `locations` | Hub pages |
| `svc-website-design`, `svc-website-development`, `svc-responsive`, `svc-ecommerce` | Build services |
| `svc-seo`, `svc-local-seo`, `svc-google-ads`, `svc-social-media`, `svc-content` | Grow services |
| `svc-maintenance`, `svc-graphic-design` | Support services |
| `loc-chennai-digital-marketing`, `loc-chennai-website-design`, `loc-chennai-seo`, `loc-pallikaranai` | Locations |
| `post-local-seo`, `post-website-cost`, `post-seo-vs-ads` | Blog posts |

---

## Growing to 300+ pages

The structure is ready for these clusters:

```
/services/<service>.html                         service pages
/locations/<area>/<service>-<area>.html          e.g. locations/velachery/website-design-velachery.html
/industries/<industry>-digital-marketing.html    e.g. industries/real-estate-digital-marketing.html
/blog/<article>.html                             articles (index: /resources/blog.html)
/guides/<guide>.html                             long-form guides
/case-studies/<client-project>.html              real projects, with permission
```

- **New service** — copy a dictionary in `services.py`, rewrite every field, add its key to
  `SERVICE_GROUPS` in `build.py`.
- **New location** — copy a dictionary in `locations.py`, rewrite **every** field with genuinely local
  information (never swap the area name in copied text — that creates doorway pages Google penalises).
  Add the key to `LOCATION_GROUPS` in `build.py` and to `AREAS` in `site_config.py`.
- **New blog post** — append to `POSTS` in `blog.py` and add its key to `ORDER`.
- **New cluster (industries, guides, case studies)** — create `tools/content/industries.py` using the
  service template fields, add `"parent": ("Industries", "industries")` to each page, add a hub page to
  `pages.py`, and register the list in `build.py` next to `SERVICES`. Header, footer, breadcrumbs,
  schema and sitemap entries are generated automatically.

Every new page automatically gets: unique title/description checks, canonical, Open Graph, Twitter tags,
BreadcrumbList + Service/FAQPage/BlogPosting schema, the shared navigation, and a sitemap entry.

---

## Typography — Helvetica only

`--font: "Helvetica Neue", Helvetica, "Nimbus Sans", "Nimbus Sans L", Arial, sans-serif`

No web fonts are downloaded, so text appears instantly with no layout shift. Helvetica is built into
iPhones, iPads and Macs. Windows and Android don't include Helvetica and it can't be self-hosted for free
(it is a licensed font), so those devices use the closest match: Windows substitutes Arial (designed with
Helvetica's proportions), Android uses its system sans-serif.

Readability rules built into `style.css`:
body text 16–18px (never below 16px), line height 1.65, lines capped at ~68 characters, only regular (400)
and bold (700) weights (no thin weights that fade on low-resolution screens), body text contrast 15:1 (never below 4.5:1),
44px+ touch targets, inputs at 16px so iPhones don't zoom, and type that scales up on 1920px and 4K screens.

---

## Images

`assets/images/<folder>/<name>.webp` + `.avif`, each at 1200px and 640px wide (`-640`). The build writes
`<picture>` markup with AVIF and WebP, width/height, `loading="lazy"` below the fold, and
`fetchpriority="high"` + preload for the hero image.

To swap in a photo: export at the same pixel size (1200×900, or 1200×675 for blog covers), save as
`name.webp`, `name.avif`, `name-640.webp`, `name-640.avif`, keep the descriptive file name, update ALT text.
Social share image: `assets/images/og/kavitha-digital-og.jpg` (1200×630).

---

## Accessibility and performance

Skip link, semantic landmarks, keyboard-operable menus (Escape closes, focus is trapped in the mobile menu),
visible focus rings, `<details>` FAQs that work without JavaScript, `prefers-reduced-motion` respected,
no content hidden when JavaScript is off. One deferred script (~5 KB gzipped), two stylesheets (~14 KB
gzipped), no libraries, no web fonts.
