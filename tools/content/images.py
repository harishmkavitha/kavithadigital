"""
Kavitha Digital — content/images.py — V1
Image registry: every image the site uses, with its folder, full-size
dimensions and default ALT text. build.py writes <picture> markup with
AVIF + WebP sources at 640px and full width from these entries.

Files live at  assets/images/<folder>/<name>.webp  (+ .avif, -640.webp, -640.avif).
To replace an illustration with a real photo, export the new image at the same
size and filenames, then update the ALT text here and rebuild.
"""

_SVC = "services"
_LOC = "locations"
_GEN = "general"
_BLOG = "blog"
_PORT = "portfolio"

IMAGES = {
    # --- General --------------------------------------------------------
    "website-design-seo-digital-marketing-chennai": {
        "folder": _GEN, "w": 1200, "h": 960,
        "alt": "Illustration of a business website in a browser with a Google search result, an enquiry notification and a growth chart"},
    "about-kavitha-digital-pallikaranai-chennai": {
        "folder": _GEN, "w": 1200, "h": 900,
        "alt": "Illustration of a project planning board with discovery, design, build and launch stages"},
    "web-design-digital-marketing-services-chennai": {
        "folder": _GEN, "w": 1200, "h": 900,
        "alt": "Illustration of connected tiles for website design, SEO, advertising and social media services"},
    "chennai-areas-served-map": {
        "folder": _GEN, "w": 1200, "h": 900,
        "alt": "Stylised map of South Chennai showing Pallikaranai and nearby areas including Velachery, Medavakkam and OMR"},

    # --- Services -------------------------------------------------------
    "website-design-company-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a business website layout in a browser window with colour and typography panels"},
    "web-development-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a code editor beside a website preview and a page speed indicator"},
    "responsive-web-design-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of one website layout adapting across a desktop monitor, tablet and smartphone"},
    "ecommerce-website-development-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of an online store with a product grid, shopping cart and order confirmation"},
    "seo-services-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a search results page with a highlighted listing and an SEO audit checklist"},
    "local-seo-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a map with location pins beside a list of local business results"},
    "google-ads-management-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of an advertising campaign dashboard with bar charts and a sponsored search result"},
    "social-media-marketing-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a smartphone showing a social media post next to a content calendar"},
    "content-marketing-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of an article being written in an editor with a content outline checklist"},
    "website-maintenance-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a website health dashboard showing backups, updates, SSL and security checks"},
    "graphic-design-logo-design-chennai": {
        "folder": _SVC, "w": 1200, "h": 900,
        "alt": "Illustration of a brand kit with a logo, colour palette, typography and social media templates"},

    # --- Locations ------------------------------------------------------
    "digital-marketing-company-chennai": {
        "folder": _LOC, "w": 1200, "h": 900,
        "alt": "Illustration of a marketing dashboard connecting search, ads and social media channels to enquiries"},
    "business-website-design-chennai": {
        "folder": _LOC, "w": 1200, "h": 900,
        "alt": "Illustration of a business website shown on a laptop and a smartphone with a call button"},
    "seo-company-chennai": {
        "folder": _LOC, "w": 1200, "h": 900,
        "alt": "Illustration of Chennai area search keywords connected to a rising visibility graph"},
    "website-designer-pallikaranai": {
        "folder": _LOC, "w": 1200, "h": 900,
        "alt": "Stylised map with a pin on Pallikaranai and nearby Velachery, Medavakkam, Perungudi and Thoraipakkam labelled"},

    # --- Blog -----------------------------------------------------------
    "local-seo-checklist-chennai-business": {
        "folder": _BLOG, "w": 1200, "h": 675,
        "alt": "Local SEO checklist illustration with a map pin, a business profile card and ticked items"},
    "website-cost-factors-chennai": {
        "folder": _BLOG, "w": 1200, "h": 675,
        "alt": "Illustration of website building blocks such as pages, content and features stacked beside a rupee symbol"},
    "seo-vs-google-ads-small-business": {
        "folder": _BLOG, "w": 1200, "h": 675,
        "alt": "Illustration comparing an organic search result and a sponsored ad side by side"},

    # --- Portfolio concepts (replace with real client work) -------------
    "interior-design-studio-website-concept": {
        "folder": _PORT, "w": 1200, "h": 900,
        "alt": "Concept design of an interior design studio website with a large project gallery"},
    "dental-clinic-website-concept": {
        "folder": _PORT, "w": 1200, "h": 900,
        "alt": "Concept design of a dental clinic website with treatments and an appointment button"},
    "residential-project-website-concept": {
        "folder": _PORT, "w": 1200, "h": 900,
        "alt": "Concept design of a residential apartment project website with floor plans and a site-visit form"},
}
