"""
Kavitha Digital — content/home.py — V1
Home page copy. Sections render in the order set in build.py → render_home().
"""

HOME = {
    "hero": {
        "eyebrow": "Website design · SEO · Digital marketing — Pallikaranai, Chennai",
        # Raw HTML (escaped ampersand) so part of the headline can carry the gradient
        "h1": 'Website Design, SEO &amp; <span class="text-gradient">Digital Marketing</span> Services in Chennai',
        "lead": "Kavitha Digital helps Chennai businesses build fast, professional websites and win more customers through SEO, Google Ads and social media — planned and delivered by Harish from our base in Pallikaranai.",
        "trust": [
            "Based in Pallikaranai, Chennai",
            "Mobile-first, SEO-ready websites",
            "Work directly with the owner",
            "Free first consultation",
        ],
        "image": "website-design-seo-digital-marketing-chennai",
    },
    "services": {
        "h2": "Everything your business needs to grow online",
        "lead": "Websites, search and marketing — planned together, so each one supports the others.",
        "keys": ["svc-website-design", "svc-website-development", "svc-seo", "svc-local-seo",
                 "svc-google-ads", "svc-social-media", "svc-ecommerce", "svc-maintenance"],
    },
    "why": {
        "h2": "Why businesses choose Kavitha Digital",
        "paras": [
            "Kavitha Digital is a Pallikaranai-based website design and digital marketing business run by Harish. You get one accountable contact who understands both how websites are built and how customers find them.",
            "Our focus is simple: websites that load fast and explain your business clearly, and marketing that brings measurable enquiries — without jargon, inflated promises or unnecessary extras.",
        ],
        "items": [
            ("user", "One point of contact", "Talk directly to Harish, from the first call to launch and beyond."),
            ("layers", "Design and marketing together", "Websites planned with SEO, ads and social media in mind from day one."),
            ("zap", "Fast, modern websites", "Lightweight builds that load quickly on mobile data."),
            ("search", "SEO foundations included", "Every website launches with clean structure, page titles and schema."),
            ("rupee", "Clear, written quotes", "Know the scope, timeline and cost before any work starts."),
            ("map-pin", "Local to South Chennai", "Based in Pallikaranai and familiar with how local customers search."),
        ],
    },
    "process": {
        "h2": "A simple, transparent web design process",
        "lead": "Five clear steps from first conversation to a website that works for your business.",
        "steps": [
            ("Free consultation", "We discuss your business, customers, goals and budget."),
            ("Plan", "A sitemap, page outline and written quote with timelines."),
            ("Design", "Home page and key pages designed for your feedback."),
            ("Build and test", "Development, device testing, speed checks and SEO setup."),
            ("Launch and grow", "Go live, connect Google tools and plan your marketing."),
        ],
    },
    "seo_dm": {
        "h2": "Get found on Google and turn searches into enquiries",
        "paras": [
            "A great website is only half the job — customers still need to find it. Our [SEO services](@svc-seo) improve your visibility in organic search, while [local SEO](@svc-local-seo) puts you on Google Maps for nearby customers.",
            "When you need enquiries quickly, [Google Ads](@svc-google-ads) and [social media marketing](@svc-social-media) put you in front of the right people today. See how it fits together on our [digital marketing company in Chennai](@loc-chennai-digital-marketing) page.",
        ],
        "channels": [
            ("svc-seo", "SEO", "Technical, on-page and off-page SEO for lasting visibility."),
            ("svc-local-seo", "Local SEO", "Google Business Profile and map pack visibility."),
            ("svc-google-ads", "Google Ads", "Search and call campaigns measured by cost per enquiry."),
            ("svc-social-media", "Social media", "Facebook and Instagram content and lead ads."),
        ],
    },
    "industries": {
        "h2": "Industries we build for",
        "lead": "Every sector has its own customers and search habits. Our approach adapts to yours.",
        "items": [
            ("home", "Real estate & builders"),
            ("pen-tool", "Interior designers"),
            ("heart-pulse", "Clinics & healthcare"),
            ("graduation", "Schools & coaching"),
            ("utensils", "Restaurants & caterers"),
            ("shopping-bag", "Retail & e-commerce"),
            ("car", "Automobile dealers & service"),
            ("factory", "Manufacturers & suppliers"),
            ("briefcase", "Professional services"),
            ("printer", "Printing & local services"),
            ("sparkles", "Salons & wellness"),
            ("truck", "Logistics & transport"),
        ],
    },
    # PLACEHOLDER: replace these illustrative concepts with real, client-approved projects.
    "portfolio": {
        "h2": "The kind of websites we create",
        "lead": "Illustrative concepts showing our design approach. Completed client projects will be added here as case studies, with permission.",
        "items": [
            {"image": "interior-design-studio-website-concept", "title": "Interior design studio",
             "text": "A gallery-led layout that lets finished projects sell the service, with a simple consultation form."},
            {"image": "dental-clinic-website-concept", "title": "Neighbourhood dental clinic",
             "text": "Treatments, timings and doctors explained clearly, with one-tap calling and directions."},
            {"image": "residential-project-website-concept", "title": "Residential apartment project",
             "text": "Floor plans, amenities and location highlights with a site-visit enquiry flow."},
        ],
    },
    # Only factual figures. Add verified numbers (projects delivered, years in business) when available.
    "stats": {
        "h2": "What you can expect",
        "items": [
            (11, "", "Digital services under one roof"),
            (10, "", "Chennai areas served from Pallikaranai"),
            (100, "%", "Of our websites designed mobile-first"),
            (1, "", "Direct point of contact — Harish"),
        ],
    },
    "locations": {
        "h2": "Serving Pallikaranai and businesses across Chennai",
        "lead": "Based in Pallikaranai – 600100, we work with businesses throughout South Chennai and the wider city.",
    },
    # PLACEHOLDER: replace each slot with a genuine, permission-granted client review.
    "testimonials": {
        "h2": "What clients say",
        "lead": "Genuine reviews from Kavitha Digital clients will be published here with their permission. We never use invented testimonials.",
        "slots": [
            "Reserved for a verified review from a website design client.",
            "Reserved for a verified review from an SEO or local SEO client.",
            "Reserved for a verified review from a digital marketing client.",
        ],
    },
    "faq_h2": "Questions businesses ask us",
    "faqs": [
        ("How much does website design cost in Chennai?", "It depends on the number of pages, content, features and design work involved. After a short consultation we provide a written quote with a clear scope. Our guide to [website design cost in Chennai](@post-website-cost) explains the main factors."),
        ("How long does it take to build a website?", "A focused business website typically takes a few weeks from approved plan to launch; larger or e-commerce sites take longer. We agree a timeline before starting."),
        ("Will my website be mobile friendly?", "Yes. Every website we build is [responsive](@svc-responsive), designed mobile-first and tested on phones, tablets and desktops."),
        ("Do you provide SEO after website development?", "Yes. Every site launches with SEO foundations, and our [SEO services](@svc-seo) and [local SEO](@svc-local-seo) help you keep growing in Google."),
        ("Do you manage Google Ads?", "Yes. We set up and manage [Google Ads campaigns](@svc-google-ads) with conversion tracking, so you can see what each enquiry costs."),
        ("Can you maintain my website after launch?", "Yes. Our [website maintenance](@svc-maintenance) service covers updates, backups, security checks and content changes."),
    ],
    "cta": {
        "h2": "Let's grow your business online",
        "text": "Tell Harish about your business and goals. You'll get honest advice and a clear plan — whether you need a new website, better Google visibility or more enquiries.",
    },
}
