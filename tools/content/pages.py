"""
Kavitha Digital — content/pages.py — V1
Core pages (home, about, hubs, blog index, FAQ, contact, legal, 404):
registry entries plus page copy.
"""

# --------------------------------------------------------------------------
# Registry — key, file path, short label, unique <title> and meta description
# --------------------------------------------------------------------------
CORE = [
    {"key": "home", "path": "index.html", "label": "Home",
     "title": "Website Design & Digital Marketing Chennai | Kavitha Digital",
     "description": "Kavitha Digital builds fast, mobile-friendly websites and grows Chennai businesses with SEO, Google Ads and social media. Based in Pallikaranai. Call 94459 78150."},
    {"key": "about", "path": "about/about-us.html", "label": "About Us",
     "title": "About Kavitha Digital | Web Design & SEO in Pallikaranai",
     "description": "Meet Kavitha Digital, run by Harish in Pallikaranai, Chennai. We design websites and run SEO and digital marketing focused on enquiries and business growth."},
    {"key": "services", "path": "services/index.html", "label": "Services",
     "title": "Our Services: Web Design, SEO & Marketing | Kavitha Digital",
     "description": "Website design and development, e-commerce, SEO, local SEO, Google Ads, social media, content, maintenance and graphic design for Chennai businesses."},
    {"key": "locations", "path": "locations/index.html", "label": "Locations",
     "title": "Areas We Serve: Pallikaranai & Chennai | Kavitha Digital",
     "description": "Kavitha Digital works with businesses in Pallikaranai, Velachery, Medavakkam, OMR, Tambaram and across Chennai. Find website design and SEO help near you."},
    {"key": "blog", "path": "resources/blog.html", "label": "Blog",
     "title": "Website & SEO Tips for Chennai Businesses | Kavitha Digital",
     "description": "Practical guides on website design, SEO, local SEO, Google Ads and digital marketing for Chennai small businesses, from Kavitha Digital in Pallikaranai."},
    {"key": "faq", "path": "resources/faq.html", "label": "FAQ",
     "title": "Website Design & SEO FAQs | Kavitha Digital, Chennai",
     "description": "Answers to common questions about website design costs, timelines, SEO, local SEO, Google Ads and maintenance for businesses in Chennai and Pallikaranai."},
    {"key": "contact", "path": "contact/contact.html", "label": "Contact",
     "title": "Contact Kavitha Digital | Call 94459 78150, Pallikaranai",
     "description": "Contact Kavitha Digital in Pallikaranai, Chennai. Call or WhatsApp Harish on 94459 78150, or send an enquiry about your website, SEO or digital marketing."},
    {"key": "privacy", "path": "legal/privacy-policy.html", "label": "Privacy Policy",
     "title": "Privacy Policy | Kavitha Digital",
     "description": "How Kavitha Digital collects, uses and protects the personal details you share through this website, phone calls and WhatsApp, and how to use your rights."},
    {"key": "terms", "path": "legal/terms-of-use.html", "label": "Terms of Use",
     "title": "Terms of Use | Kavitha Digital",
     "description": "The terms that apply when you use the Kavitha Digital website, covering information accuracy, results, intellectual property, external links and governing law."},
    {"key": "404", "path": "404.html", "label": "Page not found", "noindex": True,
     "title": "Page Not Found | Kavitha Digital",
     "description": "The page you were looking for could not be found. Explore Kavitha Digital's website design, SEO and digital marketing services, or contact Harish."},
]


# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------
ABOUT = {
    "eyebrow": "About Kavitha Digital",
    "h1": "About Kavitha Digital: Website Design and Digital Marketing from Pallikaranai",
    "lead": "Kavitha Digital is a website design, SEO and digital marketing business in Pallikaranai, Chennai, run by Harish. We help businesses build a stronger online presence — and turn it into enquiries.",
    "image": "about-kavitha-digital-pallikaranai-chennai",
    "image_alt": "Illustration of a project planning board with discovery, design, build and launch stages",
    "who": {
        "h2": "Who we are",
        "paras": [
            "Kavitha Digital is owned and run by Harish from Pallikaranai, Chennai – 600100. We design and develop websites, and we help businesses get found and chosen online through search engine optimisation, local SEO, Google Ads, social media and content.",
            "Many businesses end up with one company for their website, another for SEO and someone else for social media — and nobody takes responsibility for the overall result. Kavitha Digital brings these together, so your website and marketing are planned as one system with one accountable person.",
            "We work with small and growing businesses in Pallikaranai and across Chennai: service providers, shops, clinics, schools, builders, manufacturers and professional firms. What they share is the need for a professional online presence that brings in real enquiries.",
        ],
    },
    "focus": {
        "h2": "What we focus on",
        "lead": "Everything we do comes back to helping customers find you, trust you and contact you.",
        "items": [
            ("layout", "Website design", "Professional, [custom website design](@svc-website-design) planned around your customers and what they need to know."),
            ("code", "Website development", "[Fast, secure development](@svc-website-development) with clean code, working forms and analytics."),
            ("search", "SEO", "[Search engine optimisation](@svc-seo) that grows your Google visibility with ethical methods."),
            ("megaphone", "Digital marketing", "[Google Ads](@svc-google-ads) and [social media](@svc-social-media) campaigns measured by enquiries."),
            ("users", "Lead generation", "Call, WhatsApp and enquiry-form journeys designed to turn visitors into conversations."),
            ("trending-up", "Online visibility and growth", "A consistent presence across your website, [Google Maps](@svc-local-seo) and social media."),
        ],
    },
    "how": {
        "h2": "How we work",
        "paras": [
            "Clear communication matters as much as good design. You'll know what we're doing, why we're doing it and what it will cost before work begins.",
        ],
        "items": [
            ("Plain language, no jargon", "Options and trade-offs explained in terms that make sense for your business."),
            ("Honest recommendations", "If something won't help — or isn't worth the cost yet — we'll say so."),
            ("Written scope and quote", "Agreed deliverables and timelines before any work starts."),
            ("No invented results", "No guaranteed rankings, fake reviews or made-up statistics — ever."),
            ("Your accounts, your control", "Domains, Business Profiles and ad accounts set up in your business's name wherever possible."),
        ],
    },
    "process": {
        "h2": "From first call to launch",
        "lead": "The same clear steps for every project, large or small.",
        "steps": [
            ("Listen", "We learn about your business, customers, competitors and goals."),
            ("Recommend", "An honest view of what to do first, with a written scope and quote."),
            ("Create", "Design, content, development or campaigns — shared with you at each stage."),
            ("Launch", "Go live with tracking in place so results can be measured."),
            ("Improve", "Review the numbers and keep improving what works."),
        ],
    },
    "clients": {
        "h2": "Who we work with",
        "paras": [
            "Our clients are mostly small and medium businesses selling to local customers — in Pallikaranai, across South Chennai and throughout the city. Some need their first website; others have outgrown an old one or want more enquiries from the site they have.",
            "If that sounds like you, [get in touch](@contact) or explore our [services](@services).",
        ],
        "note": "Kavitha Digital operates from Pallikaranai only. We serve other parts of Chennai without branch offices, working over phone, WhatsApp and video calls.",
    },
    "cta": {
        "h2": "Let's talk about your business",
        "text": "A short conversation is the best way to see whether we're the right fit. Call, WhatsApp or send an enquiry.",
    },
}


# --------------------------------------------------------------------------
# Services hub  (/services/)
# --------------------------------------------------------------------------
SERVICES_HUB = {
    "eyebrow": "Services",
    "h1": "Website Design, SEO &amp; Digital Marketing Services",
    "lead": "Eleven services with one goal: helping Chennai businesses build a strong online presence and turn it into enquiries. Choose a single service or combine them into a complete plan.",
    "image": "web-design-digital-marketing-services-chennai",
    "image_alt": "Illustration of connected tiles for website design, SEO, advertising and social media services",
    # (h2, lead) for each group in build.SERVICE_GROUPS order: Build, Grow, Support
    "groups": [
        ("Build a website that works", "Design, development and e-commerce — the foundation everything else depends on."),
        ("Grow your visibility and enquiries", "Search, advertising, social media and content that bring the right people to your website."),
        ("Support and brand", "Keep your website healthy and your brand consistent everywhere."),
    ],
    "choose": {
        "h2": "Not sure which services you need?",
        "paras": [
            "Most businesses don't need everything at once. A new business may start with a website and a Google Business Profile; an established one may need SEO to reduce its reliance on ads. We'll recommend a sensible order based on your goals and budget.",
        ],
        "items": [
            ("Need credibility?", "Start with website design and a consistent brand."),
            ("Need enquiries fast?", "Google Ads and a focused landing page, alongside SEO."),
            ("Serve a local area?", "Local SEO and a complete Google Business Profile."),
            ("Selling products?", "An e-commerce website plus SEO and ads."),
        ],
    },
    "faqs": [
        ("Can I hire you for just one service?", "Yes. Many clients start with a single service, such as a new website or local SEO, and add others later if they need them."),
        ("Do you offer packages?", "We put together a proposal based on what your business needs rather than forcing a fixed package. It can combine several services, with clear pricing for each."),
        ("Which service should I start with?", "It depends on where you are today. If your website is outdated or not mobile friendly, start there. If your site is good but nobody finds it, focus on SEO or Google Ads. A [free consultation](@contact) is the quickest way to decide."),
        ("Do you work with businesses outside Chennai?", "Our focus is Chennai and most of our clients are local, but we're happy to discuss projects elsewhere in Tamil Nadu."),
    ],
    "cta": {
        "h2": "Let's find the right mix for your business",
        "text": "Tell us where you are today and where you want to be. We'll recommend the services worth starting with.",
    },
}


# --------------------------------------------------------------------------
# Locations hub  (/locations/)
# --------------------------------------------------------------------------
LOCATIONS_HUB = {
    "eyebrow": "Locations",
    "h1": "Areas We Serve: Pallikaranai and Across Chennai",
    "lead": "Kavitha Digital is based in Pallikaranai, Chennai – 600100. We design websites and run SEO and digital marketing for businesses across South Chennai and the wider city.",
    "image": "chennai-areas-served-map",
    "image_alt": "Stylised map of South Chennai showing Pallikaranai and nearby areas including Velachery, Medavakkam and OMR",
    # (h2, lead) for each group in build.LOCATION_GROUPS order: Chennai, Pallikaranai
    "groups": [
        ("Digital services for Chennai businesses", "Website design, SEO and digital marketing for businesses anywhere in Chennai."),
        ("Your local contact in Pallikaranai", "Our home base, and the neighbourhoods closest to us."),
    ],
    "areas": {
        "h2": "Neighbourhoods we work with",
        "paras": [
            "From our base in Pallikaranai we work with businesses in Velachery, Medavakkam, Perungudi, Thoraipakkam, OMR, Sholinganallur, Madipakkam, Tambaram and across Chennai.",
            "We don't have branch offices in these areas. Pages for more neighbourhoods will be added only when we can publish genuinely useful local information for each one.",
        ],
    },
    "faqs": [
        ("Do I need to be in Pallikaranai to work with you?", "No. We work with businesses across Chennai. Being local helps, but most projects run smoothly over phone, WhatsApp and video calls."),
        ("Do you have offices in other areas?", "No. Kavitha Digital is based in Pallikaranai only. Our location pages describe how we serve businesses in each area — they are not branch offices."),
        ("Can you help my business rank in my area?", "Yes. [Local SEO](@svc-local-seo) focuses on the areas you genuinely serve, using your Google Business Profile, reviews and useful local content."),
    ],
    "cta": {
        "h2": "Wherever you are in Chennai, let's talk",
        "text": "Call or WhatsApp Harish to discuss your website, SEO or digital marketing.",
    },
}


# --------------------------------------------------------------------------
# Blog index  (/resources/blog.html)
# --------------------------------------------------------------------------
BLOG_INDEX = {
    "eyebrow": "Resources",
    "h1": "Website, SEO &amp; Digital Marketing Blog",
    "lead": "Practical, jargon-free guides for Chennai business owners on websites, SEO, local SEO, Google Ads and digital marketing.",
    "topics": {
        "h2": "Topics we write about",
        "paras": [
            "More articles will be added across these topics. Each one aims to answer a real question business owners ask — and links to the service pages where you can go deeper.",
        ],
        "list": ["Website Design", "SEO", "Local SEO", "Digital Marketing", "Google Ads",
                 "Social Media Marketing", "E-commerce", "Website Development", "Business Growth"],
    },
    "cta": {
        "h2": "Have a question we haven't covered?",
        "text": "Ask Harish directly — about your website, your Google visibility or where to spend your marketing budget.",
    },
}


# --------------------------------------------------------------------------
# FAQ page  (/resources/faq.html)
# --------------------------------------------------------------------------
FAQ_PAGE = {
    "eyebrow": "Frequently asked questions",
    "h1": "Website Design, SEO &amp; Digital Marketing FAQs",
    "lead": "Straight answers to the questions Chennai business owners ask most about websites, SEO, Google Ads and working with Kavitha Digital.",
    "groups": [
        {"id": "websites", "title": "Website design and development", "items": [
            ("How much does website design cost in Chennai?", "It depends on the number of pages, custom design, content writing and features such as booking or e-commerce. We provide a written quote after a short consultation. Our guide to [website design cost in Chennai](@post-website-cost) explains the main factors."),
            ("How long does it take to build a website?", "A focused business website typically takes a few weeks from approved plan to launch. Larger websites, online stores and projects waiting on content take longer. We agree a timeline at the start."),
            ("Will my website be mobile friendly?", "Yes. Every site is designed mobile-first and tested on phones, tablets and desktops. See [responsive web design](@svc-responsive)."),
            ("Can you redesign an existing website?", "Yes. We keep what works, improve what doesn't and protect your existing search visibility where possible. See [website design](@svc-website-design)."),
            ("Who owns the domain and website?", "We recommend registering your domain and hosting in your business's name, and set things up that way wherever possible so you stay in control."),
            ("Can you build an online store?", "Yes. See [e-commerce website development](@svc-ecommerce) for platforms, payments and delivery options."),
        ]},
        {"id": "seo", "title": "SEO and local SEO", "items": [
            ("How long does SEO normally take?", "Most websites see meaningful movement within three to six months, depending on competition and how much needs fixing. SEO is an ongoing investment. See our [SEO services](@svc-seo)."),
            ("What is local SEO?", "Local SEO improves how your business appears in location-based searches and on Google Maps, through your Google Business Profile, consistent listings, reviews and local website content. See [local SEO](@svc-local-seo)."),
            ("Can SEO help businesses in Pallikaranai?", "Yes. Searches like “clinic in Pallikaranai” or “website designer near me” are local by nature, and a well-optimised profile and website help you appear in them. See our [Pallikaranai page](@loc-pallikaranai)."),
            ("Do you guarantee first-page rankings?", "No. Nobody controls Google's results, so guarantees are a warning sign. We commit to transparent, ethical work and clear reporting."),
            ("Do you provide SEO after website development?", "Yes. Every website launches with SEO foundations, and ongoing SEO is available as a separate service."),
        ]},
        {"id": "marketing", "title": "Google Ads and social media", "items": [
            ("Do you manage Google Ads?", "Yes — account setup, keywords, ads, landing pages, conversion tracking and monthly optimisation. See [Google Ads management](@svc-google-ads)."),
            ("How much should I spend on ads?", "It depends on competition, the areas you target and the value of a customer. We recommend a starting budget after research and adjust it based on results. Ad spend is separate from management fees."),
            ("Do you run Facebook and Instagram ads?", "Yes, for awareness, website traffic, messages and lead generation. See [social media marketing](@svc-social-media)."),
            ("Should I choose SEO or Google Ads?", "Ads are fast; SEO lasts. Many small businesses use both. Our article on [SEO vs Google Ads](@post-seo-vs-ads) explains how to decide."),
        ]},
        {"id": "working-together", "title": "Working with Kavitha Digital", "items": [
            ("Where is Kavitha Digital based?", "In Pallikaranai, Chennai – 600100. The business is run by Harish."),
            ("Who will I be working with?", "Harish, the owner, is your main point of contact throughout your project."),
            ("How do I get a quote?", "[Contact us](@contact) by phone, WhatsApp or the enquiry form. After a short conversation about your needs, you'll receive a written quote."),
            ("Can you maintain my website after launch?", "Yes. See [website maintenance](@svc-maintenance) for updates, backups, security checks and content changes."),
            ("Do you work with businesses outside Pallikaranai?", "Yes, across Chennai. See the [areas we serve](@locations)."),
        ]},
    ],
    "cta": {
        "h2": "Didn't find your answer?",
        "text": "Call or WhatsApp Harish with your question — there's no obligation.",
    },
}


# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------
CONTACT = {
    "eyebrow": "Contact",
    "h1": "Contact Kavitha Digital",
    "lead": "Talk to Harish about your website, SEO or digital marketing. Call or WhatsApp {PHONE}, or send an enquiry below — you'll get a straightforward answer and honest advice.",
    "next": [
        ("We reply", "Harish reviews your enquiry and gets back to you, usually by phone or WhatsApp."),
        ("Free consultation", "A short conversation about your business, goals and current website."),
        ("Clear proposal", "A written scope, timeline and quote for the work you need."),
    ],
    "faqs": [
        ("Is the first consultation free?", "Yes. The first conversation about your business and goals is free and comes with no obligation."),
        ("What should I prepare before we talk?", "Your current website address if you have one, examples of websites you like, and a rough idea of your goals and budget. Don't worry if you don't have all of this — we'll guide you."),
        ("Do you work with businesses outside Pallikaranai?", "Yes. We're based in Pallikaranai and work with businesses across Chennai."),
        ("How will my details be used?", "Only to respond to your enquiry and discuss your project. See our [privacy policy](@privacy)."),
    ],
}


# --------------------------------------------------------------------------
# Legal pages — DRAFTS: have them reviewed before launch
# --------------------------------------------------------------------------
LEGAL = {
    "privacy": {
        "h1": "Privacy Policy",
        "lead": "How Kavitha Digital collects, uses and protects your personal data.",
        "updated": "2026-09-21",
        "body": [
            ("p", "This privacy policy explains how Kavitha Digital (“we”, “us”), run by Harish from Pallikaranai, Chennai – 600100, Tamil Nadu, collects and uses personal data when you use this website or contact us. We collect only what we need and explain clearly how it is used."),
            ("h2", "What we collect"),
            ("ul", [
                "**Enquiry details** you choose to share through the contact form, phone, WhatsApp or email — such as your name, phone number, email address, business name and message.",
                "**Technical data** that website hosting providers routinely record, such as IP address and browser type, for security and reliability.",
            ]),
            ("p", "This website does not currently use analytics or advertising cookies. If we add them in future, we will update this policy and ask for your consent where required."),
            ("h2", "How we use your information"),
            ("ul", [
                "To respond to your enquiry and discuss the services you asked about.",
                "To prepare quotes and deliver services you engage us for.",
                "To keep records required for accounting and legal purposes.",
            ]),
            ("p", "We do not sell your personal data, and we do not use it for unrelated marketing without your consent."),
            ("h2", "Consent and legal basis"),
            ("p", "We process your personal data on the basis of the consent you give when you contact us, and where necessary to provide services you request, in line with the Digital Personal Data Protection Act, 2023. You may withdraw consent at any time by contacting us."),
            ("h2", "Third-party services"),
            ("p", "If you contact us through WhatsApp, your messages are handled by WhatsApp under its own privacy policy. If the contact form is connected to a form service, your enquiry is transmitted to and stored by that service in order to reach us. This website is hosted on GitHub Pages, whose servers may process technical data such as IP addresses."),
            ("h2", "How long we keep data"),
            ("p", "We keep enquiry details only as long as needed to respond to you and, if you become a client, for the duration of our work together and any period required by law."),
            ("h2", "Your rights"),
            ("p", "Subject to applicable law, you can ask us to:"),
            ("ul", [
                "give you access to the personal data we hold about you;",
                "correct or update inaccurate data;",
                "erase data we no longer need;",
                "stop processing based on your consent (withdraw consent);",
                "record a nominee to exercise your rights in the event of death or incapacity; and",
                "address any grievance about how your data has been handled.",
            ]),
            ("h2", "Grievance contact"),
            ("p", "For privacy questions, requests or grievances, contact Harish, Kavitha Digital, Pallikaranai, Chennai – 600100, on {PHONE}. We will respond within a reasonable time."),
            ("h2", "Changes to this policy"),
            ("p", "We may update this policy from time to time. The latest version will always be on this page, with the date it was last updated."),
        ],
    },
    "terms": {
        "h1": "Terms of Use",
        "lead": "The terms that apply when you use the Kavitha Digital website.",
        "updated": "2026-09-21",
        "body": [
            ("p", "These terms apply to your use of the Kavitha Digital website. By using the site, you agree to them. If you do not agree, please do not use the website."),
            ("h2", "About us"),
            ("p", "This website is operated by Kavitha Digital, run by Harish, Pallikaranai, Chennai – 600100, Tamil Nadu, India. Phone: {PHONE}."),
            ("h2", "Information on this website"),
            ("p", "We aim to keep the information on this website accurate and up to date, but it is provided for general information only and is not professional advice for your specific situation. Service descriptions are not an offer; the scope, timeline and price of any work are confirmed in a written quote."),
            ("h2", "No guarantee of results"),
            ("p", "Search rankings, advertising performance and social media results depend on many factors outside our control, including search engine algorithms and competition. We do not guarantee specific rankings, traffic, enquiries or sales."),
            ("h2", "Intellectual property"),
            ("p", "The content, design and graphics on this website belong to Kavitha Digital unless otherwise stated. You may view pages and share links to them, but you may not copy or republish substantial parts of the website without permission. Illustrations labelled as concepts show our design approach and do not represent client projects."),
            ("h2", "Links to other websites"),
            ("p", "This website links to external services such as WhatsApp. We are not responsible for the content or privacy practices of those websites."),
            ("h2", "Limitation of liability"),
            ("p", "To the extent permitted by law, Kavitha Digital is not liable for any loss arising from the use of this website or reliance on its content."),
            ("h2", "Governing law"),
            ("p", "These terms are governed by the laws of India. Any disputes are subject to the jurisdiction of the courts in Chennai, Tamil Nadu."),
            ("h2", "Changes"),
            ("p", "We may update these terms from time to time. Please check this page for the latest version."),
        ],
    },
}


# --------------------------------------------------------------------------
# 404
# --------------------------------------------------------------------------
NOT_FOUND = {
    "h1": "Sorry, we couldn't find that page",
    "lead": "The page may have moved, or the link may be mistyped. Try one of the pages below, or call Harish on {PHONE}.",
    "links": [("home", "Home"), ("services", "Services"), ("blog", "Blog"), ("contact", "Contact"),
              ("faq", "FAQ"), ("locations", "Locations")],
}
