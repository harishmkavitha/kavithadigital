"""
Kavitha Digital — site_config.py — V1
Single source of truth for business details, domain and site-wide settings.
Edit here, then run:  python3 tools/build.py
"""

# --------------------------------------------------------------------------
# !!! DOMAIN PLACEHOLDER — REPLACE BEFORE LAUNCH !!!
# Every canonical URL, Open Graph URL, JSON-LD @id, sitemap.xml and robots.txt
# entry is built from this one value. example.com must never go live.
#   Custom domain:          "https://www.kavithadigital.in"
#   GitHub project page:    "https://harishmkavitha.github.io/kavitha-digital"
# No trailing slash.
# --------------------------------------------------------------------------
SITE_URL = "https://www.example.com"

# Bump after editing CSS/JS so browsers fetch the new files (?v=2, ?v=3 …)
ASSET_VERSION = "1"

BUSINESS = {
    "name": "Kavitha Digital",
    "owner": "Harish",
    "phone_display": "+91 94459 78150",   # formatted for reading
    "phone_short": "94459 78150",         # used in buttons ("Call 94459 78150")
    "phone_e164": "+919445978150",        # tel: links and schema
    "whatsapp": "919445978150",           # wa.me — digits only
    "locality": "Pallikaranai",
    "city": "Chennai",
    "postal_code": "600100",
    "region": "Tamil Nadu",
    "country": "India",
    "country_code": "IN",
    # PLACEHOLDER — add the business email, e.g. "hello@kavithadigital.in".
    # While empty, the site shows "coming soon" instead of a broken mailto link.
    "email": "",
}

# Address exactly as it should appear everywhere (keep identical to Google Business Profile)
ADDRESS_LINE = "Pallikaranai, Chennai – 600100"
ADDRESS_FULL = "Pallikaranai, Chennai – 600100, Tamil Nadu, India"

# --------------------------------------------------------------------------
# Contact form
# Empty  → the form hands the enquiry to WhatsApp (works on GitHub Pages as-is).
# Filled → the form POSTs to this endpoint. Works with:
#   Formspree   "https://formspree.io/f/your-form-id"
#   Web3Forms   "https://api.web3forms.com/submit"  (also set WEB3FORMS_ACCESS_KEY)
#   Netlify / custom API — any endpoint that accepts multipart form data
# --------------------------------------------------------------------------
FORM_ENDPOINT = ""
WEB3FORMS_ACCESS_KEY = ""

# --------------------------------------------------------------------------
# Social profiles — PLACEHOLDERS. Leave empty until the real profiles exist;
# empty entries are not rendered and are not added to schema (no fake sameAs).
# --------------------------------------------------------------------------
SOCIAL = {
    "facebook": "",
    "instagram": "",
    "linkedin": "",
    "youtube": "",
    "x": "",
}

# Default social-share image (1200×630) relative to the site root
OG_IMAGE = "assets/images/og/kavitha-digital-og.jpg"

# Areas served — shown on the home page, location hub and in schema areaServed.
# "key" links the chip to an existing page; add keys as new location pages go live.
AREAS = [
    {"name": "Pallikaranai", "key": "loc-pallikaranai"},
    {"name": "Velachery", "key": None},
    {"name": "Medavakkam", "key": None},
    {"name": "Perungudi", "key": None},
    {"name": "Thoraipakkam", "key": None},
    {"name": "OMR", "key": None},
    {"name": "Sholinganallur", "key": None},
    {"name": "Madipakkam", "key": None},
    {"name": "Tambaram", "key": None},
    {"name": "Chennai", "key": "loc-chennai-digital-marketing"},
]
