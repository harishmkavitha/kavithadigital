"""
Kavitha Digital — content/locations.py — V1
Location landing pages. Each must be genuinely different: local context,
businesses served, nearby areas and FAQs written for that place.
Never duplicate a page and swap the area name — that creates doorway pages.

To add a location later (e.g. Velachery):
  1. Copy one dictionary below and rewrite EVERY field for the new area.
  2. Use a path such as "locations/velachery/website-design-velachery.html".
  3. Add the key to LOCATION_GROUPS in build.py and to AREAS in site_config.py.
  4. Run: python3 tools/build.py
"""

LOCATIONS = [
    # =====================================================================
    # DIGITAL MARKETING COMPANY — CHENNAI
    # =====================================================================
    {
        "key": "loc-chennai-digital-marketing",
        "path": "locations/digital-marketing-company-chennai.html",
        "label": "Digital Marketing Company Chennai",
        "short": "Chennai – Digital Marketing",
        "area_tag": "Chennai",
        "icon": "trending-up",
        "menu_desc": "SEO, ads and social media as one plan",
        "card_text": "SEO, Google Ads, social media and lead generation planned as one strategy for businesses across Chennai.",
        "title": "Digital Marketing Company in Chennai | Kavitha Digital",
        "description": "Digital marketing company in Chennai for SEO, Google Ads, social media and lead generation, with plans built around your area, customers and budget.",
        "eyebrow": "Digital marketing · Chennai",
        "h1": "Digital Marketing Company in Chennai for Growing Local Businesses",
        "lead": "Kavitha Digital plans and runs digital marketing for Chennai businesses — combining SEO, Google Ads, social media and a website that converts, so every rupee of your budget works towards more enquiries.",
        "image": "digital-marketing-company-chennai",
        "image_alt": "Illustration of a marketing dashboard connecting search, ads and social media channels to enquiries",
        "wa_text": "digital marketing for my business",
        "service_type": "Digital marketing",
        "area_served": [{"@type": "City", "name": "Chennai"}],
        "overview": {
            "h2": "Digital marketing services in Chennai, planned as one strategy",
            "paras": [
                "Chennai is a city of distinct business districts and neighbourhoods. The IT corridor along OMR, the retail streets of T. Nagar, the industrial estates in Guindy and Ambattur and the fast-growing residential suburbs in the south each have different customers, competitors and search habits. A digital marketing plan that works for one rarely fits another without changes.",
                "As a digital marketing company based in Pallikaranai, we start with your customers: where they are, how they search and what convinces them. Then we combine the channels that suit your goals — [SEO](@svc-seo) and [local SEO](@svc-local-seo) for lasting visibility, [Google Ads](@svc-google-ads) for immediate enquiries, [social media marketing](@svc-social-media) for awareness and trust, and a [website](@svc-website-design) that turns visits into calls.",
                "Many Chennai customers would rather call or send a WhatsApp message than fill in a form, so our campaigns are built around click-to-call and click-to-WhatsApp journeys, with tracking that shows which channel produced each enquiry. That's the difference between online marketing that looks busy and performance marketing you can measure.",
            ],
            "glance": [
                ("Based in", "Pallikaranai, Chennai – 600100"),
                ("Serving", "Businesses across Chennai"),
                ("Channels", "SEO, local SEO, Google Ads, social media, content and websites"),
                ("Phone / WhatsApp", "{PHONE}"),
            ],
        },
        "businesses": {
            "h2": "Chennai businesses we help with digital marketing",
            "lead": "Every sector markets differently. These are some of the businesses our approach suits.",
            "items": [
                ("home", "Real estate and builders", "Project launches need qualified site-visit enquiries from buyers with genuine budgets — not just clicks. Landing pages, ads and lead forms are planned around that."),
                ("heart-pulse", "Clinics and healthcare", "Patients search by speciality and area. Local SEO, clear treatment pages and careful, policy-compliant advertising help them find and trust you."),
                ("graduation", "Schools, colleges and coaching", "Admission seasons are short and competitive. Campaigns are timed to enquiry peaks and reach parents and students in the right areas."),
                ("store", "Retail and showrooms", "Footfall and online orders both matter. Google Business Profile, local ads and social media work together to drive visits and sales."),
                ("factory", "Manufacturers and B2B suppliers", "Buyers research carefully. Detailed product pages, SEO and LinkedIn visibility support longer sales cycles."),
                ("utensils", "Restaurants, caterers and food brands", "Visual content, local search and delivery-app visibility combine to bring in orders."),
            ],
        },
        "services": {
            "h2": "How our core services work for Chennai businesses",
            "lead": "The three pillars most Chennai businesses need, adapted to your market.",
            "items": [
                ("svc-website-design", "Website design for Chennai customers", "Mobile-first sites with call and WhatsApp buttons, clear service information and pages for the areas you serve. See our [website design company in Chennai](@loc-chennai-website-design) page."),
                ("svc-seo", "SEO for competitive Chennai searches", "Technical fixes, focused service pages and local SEO, so you appear for “service + area” and “near me” searches. More on our [SEO company in Chennai](@loc-chennai-seo) page."),
                ("svc-google-ads", "Performance marketing and lead generation", "Google Ads and social campaigns targeted by area and intent, measured by cost per enquiry rather than clicks or impressions."),
            ],
        },
        "nearby": {
            "h2": "Serving businesses across Chennai",
            "paras": [
                "Our office is in Pallikaranai, a short distance from Velachery, Medavakkam, Perungudi, Thoraipakkam, Sholinganallur, OMR, Madipakkam and Tambaram. We also work with businesses elsewhere in the city — most of the work runs smoothly over phone, WhatsApp and video calls.",
                "We don't have branch offices in these areas, and we don't pretend to. You'll always deal directly with Harish in Pallikaranai.",
            ],
            "areas": [
                {"name": "Pallikaranai", "key": "loc-pallikaranai"}, "Velachery", "Medavakkam", "Perungudi",
                "Thoraipakkam", "OMR", "Sholinganallur", "Madipakkam", "Tambaram",
            ],
        },
        "approach": {
            "h2": "How we work with Chennai businesses",
            "lead": "A practical, measurable approach, whatever your size.",
            "steps": [
                ("Free consultation", "We discuss your business, customers, current marketing and goals."),
                ("Audit and plan", "A review of your website, search visibility, ads and social media, with a prioritised plan and budget options."),
                ("Build the foundations", "Fix the website, set up tracking and complete your Google Business Profile."),
                ("Launch campaigns", "SEO, ads and social media rolled out in the agreed order."),
                ("Report and improve", "Monthly reporting on enquiries and costs, with adjustments based on results."),
            ],
        },
        "faq_h2": "Digital marketing in Chennai: FAQs",
        "faqs": [
            ("What does a digital marketing company do?", "A digital marketing company helps businesses attract and convert customers online — through search engine optimisation, paid advertising such as Google Ads, social media marketing, content and websites. The right mix depends on your goals, market and budget."),
            ("How much does digital marketing cost in Chennai?", "It depends on the channels you need, how competitive your market is and your advertising budget, which is separate from management fees. After a consultation we share a clear proposal with options, so you can choose what fits."),
            ("Which is better for my business: SEO, Google Ads or social media?", "Each does a different job. Google Ads brings quick enquiries, SEO builds lasting visibility and social media builds awareness and trust. Most businesses benefit from a combination — our guide to [SEO vs Google Ads](@post-seo-vs-ads) is a good starting point."),
            ("Do you work with businesses outside South Chennai?", "Yes. We're based in Pallikaranai and work with businesses across Chennai. Most work happens over phone, WhatsApp and video calls."),
            ("How do you measure results?", "We track the actions that matter — calls, WhatsApp clicks, form enquiries and sales where possible — and report on cost per enquiry alongside traffic and rankings."),
            ("Can you work with our existing website?", "Usually, yes. We review your current website first. If it's holding your marketing back, we'll recommend specific improvements or a rebuild through our [website design](@svc-website-design) service."),
        ],
        "related_locations": ["loc-chennai-website-design", "loc-chennai-seo", "loc-pallikaranai"],
        "related_services": ["svc-seo", "svc-google-ads", "svc-social-media"],
        "cta": {"h2": "Looking for a digital marketing partner in Chennai?",
                "text": "Book a free consultation and get a clear, prioritised plan for your business.",
                "button": "Get a Free Consultation"},
    },

    # =====================================================================
    # WEBSITE DESIGN COMPANY — CHENNAI
    # =====================================================================
    {
        "key": "loc-chennai-website-design",
        "path": "locations/website-design-company-chennai.html",
        "label": "Website Design Company Chennai",
        "short": "Chennai – Website Design",
        "area_tag": "Chennai",
        "icon": "layout",
        "menu_desc": "Business websites for Chennai companies",
        "card_text": "Professional, mobile-first business websites for Chennai companies — from small business sites to corporate websites.",
        "title": "Website Design Company in Chennai | Kavitha Digital",
        "description": "Website design company in Chennai building mobile-first business, corporate and small business websites. Work directly with owner Harish. Free consultation.",
        "eyebrow": "Website design · Chennai",
        "h1": "Website Design Company in Chennai",
        "lead": "Looking for a website designer in Chennai you can actually talk to? Kavitha Digital designs and builds professional, mobile-friendly websites for Chennai businesses, with the owner, Harish, involved from the first call to launch.",
        "image": "business-website-design-chennai",
        "image_alt": "Illustration of a business website shown on a laptop and a smartphone with a call button",
        "wa_text": "a website for my Chennai business",
        "service_type": "Website design",
        "area_served": [{"@type": "City", "name": "Chennai"}],
        "overview": {
            "h2": "Website designing for Chennai businesses of every size",
            "paras": [
                "There's no shortage of web designers in Chennai. What's harder to find is a website design company that takes time to understand your business, explains its choices in plain language and builds a site that brings in enquiries — not just one that looks good in a presentation.",
                "We design small business websites, corporate websites, landing pages and online stores. Each project starts with the same questions: who are your customers, where in Chennai are they, what do they need to know and what should they do next? The answers shape the page structure, the words and the design.",
                "Chennai customers mostly browse on phones, often on the move, and many prefer to call or WhatsApp rather than type long messages. So every site we build is [responsive](@svc-responsive), loads quickly on mobile data and keeps contact options within easy reach. For everything that's included, see our [website design services](@svc-website-design).",
            ],
            "glance": [
                ("Based in", "Pallikaranai, Chennai – 600100"),
                ("Website types", "Small business, corporate, landing pages and e-commerce"),
                ("Every site includes", "Mobile-first design, SEO basics, call and WhatsApp buttons"),
                ("Phone / WhatsApp", "{PHONE}"),
            ],
        },
        "businesses": {
            "h2": "Websites for Chennai's different kinds of businesses",
            "lead": "A few examples of the websites we plan and build.",
            "items": [
                ("briefcase", "Corporate and professional firms", "CA firms, consultants and B2B companies need credible corporate website design that explains services clearly and supports longer decisions."),
                ("store", "Small and local businesses", "Affordable, focused small business websites that present your services, areas covered and contact options without unnecessary extras."),
                ("building", "Real estate and interiors", "Project showcases, galleries and enquiry forms that let the quality of the work speak for itself."),
                ("heart-pulse", "Clinics and wellness", "Clear information on treatments, doctors and timings, with appointment calls and directions one tap away."),
                ("shopping-bag", "Retail and D2C brands", "Online catalogues and [e-commerce websites](@svc-ecommerce) with secure payments and WhatsApp ordering."),
                ("graduation", "Education and training", "Course pages, admissions information and enquiry forms for schools, colleges and coaching centres."),
            ],
        },
        "services": {
            "h2": "What you get from a Chennai website design project",
            "items": [
                ("svc-website-design", "Custom website design", "Layouts designed for your brand and customers, with clear calls to action on every page."),
                ("svc-website-development", "Fast, reliable development", "Clean code, working forms, WhatsApp integration and analytics — all tested before launch."),
                ("svc-seo", "SEO-ready from launch", "Page titles, headings, structured data and a sitemap in place, ready for ongoing SEO."),
            ],
        },
        "nearby": {
            "h2": "Web designers for every part of Chennai",
            "paras": [
                "We're based in Pallikaranai in South Chennai, a short drive from Velachery, Medavakkam, Perungudi, Thoraipakkam, Sholinganallur and OMR. Businesses in other parts of the city work with us just as easily over phone, WhatsApp and video calls.",
                "If your business is close to us, our [Pallikaranai website designer](@loc-pallikaranai) page explains how we work with local businesses in more detail.",
            ],
            "areas": [
                {"name": "Pallikaranai", "key": "loc-pallikaranai"}, "Velachery", "Medavakkam", "Perungudi",
                "Thoraipakkam", "Sholinganallur", "OMR", "Madipakkam", "Tambaram",
            ],
        },
        "approach": {
            "h2": "How we plan the right website for your business",
            "steps": [
                ("Understand the goal", "Leads, sales, credibility or recruitment — the goal decides the structure."),
                ("Plan the pages", "A sitemap and content outline agreed before design begins."),
                ("Design and review", "Designs presented for your feedback, then refined."),
                ("Build, test and launch", "Development, device testing, speed checks and launch."),
            ],
        },
        "faq_h2": "Choosing a website design company in Chennai",
        "faqs": [
            ("How much does a website cost in Chennai?", "Website prices in Chennai vary widely because projects vary widely — from a few pages to large corporate or e-commerce sites. The main factors are the number of pages, custom design, content writing and features. We provide a written quote after understanding your needs; our article on [website design cost in Chennai](@post-website-cost) explains the factors in detail."),
            ("Do you design affordable websites for small businesses?", "Yes. For small businesses we focus the budget on what brings enquiries — a clear home page, service pages, contact options and a link to your Google Business Profile — and leave optional extras for later."),
            ("What makes a good website design company in Chennai?", "Look for real examples of work, clear communication, a defined process, mobile-first design, SEO basics included and honest answers about cost and timelines. Ask who will actually work on your site and who owns the domain and hosting."),
            ("Can you redesign my existing website?", "Yes. We review your current site's content, structure and search visibility first, so the redesign improves results rather than losing what already works."),
            ("Will you help my website rank on Google?", "Every site includes SEO foundations. For ongoing rankings in Chennai, our [SEO services](@svc-seo) and [local SEO](@svc-local-seo) build on that base."),
        ],
        "related_locations": ["loc-chennai-digital-marketing", "loc-chennai-seo", "loc-pallikaranai"],
        "related_services": ["svc-website-design", "svc-website-development", "svc-responsive"],
        "cta": {"h2": "Planning a new website for your Chennai business?",
                "text": "Talk to Harish about your goals and get a clear plan and written quote.",
                "button": "Talk to a Website Expert"},
    },

    # =====================================================================
    # SEO COMPANY — CHENNAI
    # =====================================================================
    {
        "key": "loc-chennai-seo",
        "path": "locations/seo-company-chennai.html",
        "label": "SEO Company Chennai",
        "short": "Chennai – SEO",
        "area_tag": "Chennai",
        "icon": "search",
        "menu_desc": "Ethical SEO for Chennai search results",
        "card_text": "Ethical SEO for Chennai businesses competing for local and city-wide searches — technical, on-page, off-page and local.",
        "title": "SEO Company in Chennai for Local Businesses | Kavitha Digital",
        "description": "Pallikaranai-based SEO company helping Chennai businesses rank with technical, on-page, off-page and local SEO. Transparent methods and plain-English reports.",
        "eyebrow": "SEO · Chennai",
        "h1": "SEO Company in Chennai Focused on Local Results",
        "lead": "Kavitha Digital is a Pallikaranai-based SEO company helping Chennai businesses rank for the searches their customers make — with transparent methods, realistic timelines and reporting you can understand.",
        "image": "seo-company-chennai",
        "image_alt": "Illustration of Chennai area search keywords connected to a rising visibility graph",
        "wa_text": "SEO for my Chennai business",
        "service_type": "Search engine optimisation",
        "area_served": [{"@type": "City", "name": "Chennai"}],
        "overview": {
            "h2": "Search engine optimisation for the Chennai market",
            "paras": [
                "Search results in Chennai are shaped by location. Someone in Velachery searching for a “physiotherapy clinic” sees different businesses from someone in Anna Nagar. Many people add the area to their search — “interior designer OMR”, “CA firm Tambaram” — and many type in a mix of Tamil and English. Effective SEO in Chennai has to reflect all of this.",
                "Our SEO service combines [technical, on-page and off-page SEO](@svc-seo) with [local SEO](@svc-local-seo) for Google Maps. We research how your customers search in the areas you serve, make sure your site is technically sound, build focused service and area pages, and strengthen your presence on Google Business Profile and trusted Indian directories.",
                "Working as an SEO consultant for small and medium businesses, Harish handles your account personally — so the person reviewing your site is the person explaining what's changing and why.",
            ],
            "glance": [
                ("Based in", "Pallikaranai, Chennai – 600100"),
                ("Approach", "Ethical, white-hat SEO with plain-English reports"),
                ("Covers", "Technical, on-page, off-page and local SEO"),
                ("Phone / WhatsApp", "{PHONE}"),
            ],
        },
        "businesses": {
            "h2": "Chennai businesses that gain most from SEO",
            "items": [
                ("heart-pulse", "Clinics and specialists", "Patients search by treatment and area — ranking for those searches brings appointment calls."),
                ("building", "Builders, interiors and property services", "High-value services researched online over weeks, where visibility and trust decide the shortlist."),
                ("briefcase", "Professional services", "Lawyers, accountants and consultants competing on expertise and reputation."),
                ("car", "Automobile dealers and service centres", "Searches for servicing, spares and showrooms by area and brand."),
                ("graduation", "Education providers", "Course and admissions searches that peak by season."),
                ("factory", "Industrial and B2B companies", "Product-specific searches from buyers across Tamil Nadu and India."),
            ],
        },
        "services": {
            "h2": "SEO services we provide in Chennai",
            "items": [
                ("svc-seo", "Technical and on-page SEO", "Site speed, crawlability, structured data, titles, headings and content improvements for each key page."),
                ("svc-local-seo", "Local SEO and Google Maps", "Business Profile optimisation, NAP consistency, reviews and genuinely useful area pages."),
                ("svc-content", "Content and off-page SEO", "Helpful articles, ethical link building and citations on reputable Indian directories."),
            ],
        },
        "nearby": {
            "h2": "Local SEO for South Chennai and beyond",
            "paras": [
                "Businesses in fast-growing areas such as Pallikaranai, Medavakkam, Sholinganallur and Thoraipakkam see new competitors appear as these neighbourhoods expand. Consistent local SEO keeps you visible as the market grows.",
                "Near our base? See how we help businesses on our [Pallikaranai](@loc-pallikaranai) page.",
            ],
            "areas": [
                {"name": "Pallikaranai", "key": "loc-pallikaranai"}, "Medavakkam", "Sholinganallur", "Thoraipakkam",
                "Velachery", "Perungudi", "OMR", "Madipakkam", "Tambaram",
            ],
        },
        "approach": {
            "h2": "Our SEO approach for Chennai businesses",
            "steps": [
                ("Audit", "Technical health, content, links, local listings and competitors in your area."),
                ("Keyword map", "The searches your customers make, grouped by service and area and assigned to specific pages."),
                ("Fix and build", "Technical fixes, page improvements and new service or area pages."),
                ("Grow authority", "Reviews, citations and ethical links from relevant sources."),
                ("Report monthly", "Visibility, traffic, enquiries and the work completed."),
            ],
        },
        "faq_h2": "SEO in Chennai: FAQs",
        "faqs": [
            ("How do I choose an SEO company in Chennai?", "Ask how they will improve your site specifically, what they'll report on and how they build links. Be wary of guaranteed rankings, very cheap link packages or vague monthly reports. A good SEO partner explains the work and focuses on enquiries, not just rankings."),
            ("Do you offer SEO services for small businesses in Chennai?", "Yes. We tailor the scope to your budget and focus first on the changes most likely to bring enquiries — often local SEO and improving key service pages."),
            ("How long before we see SEO results in Chennai?", "It depends on your competition, your website's history and the areas you target. Many sites see progress within three to six months; competitive searches take longer."),
            ("Do you do off-page SEO and link building?", "Yes, using ethical methods: citations on reputable directories, relationships with relevant local and industry websites, and content worth linking to. We don't buy links or use private blog networks."),
            ("Can you help my business rank in a specific Chennai area?", "Yes. We strengthen your Google Business Profile, build useful area-specific content where you genuinely serve customers and improve local signals — and we'll be honest about what's realistic for your location."),
        ],
        "related_locations": ["loc-chennai-digital-marketing", "loc-chennai-website-design", "loc-pallikaranai"],
        "related_services": ["svc-seo", "svc-local-seo", "svc-content"],
        "cta": {"h2": "Ready to grow your visibility in Chennai?",
                "text": "Get an SEO review of your website with clear, prioritised next steps.",
                "button": "Start Your SEO Project"},
    },

    # =====================================================================
    # WEBSITE DESIGNER — PALLIKARANAI
    # =====================================================================
    {
        "key": "loc-pallikaranai",
        "path": "locations/website-design-pallikaranai.html",
        "label": "Website Designer Pallikaranai",
        "short": "Pallikaranai",
        "area_tag": "Pallikaranai",
        "icon": "map-pin",
        "menu_desc": "Your local web design and SEO contact",
        "card_text": "Our home base. Website design, SEO and digital marketing for businesses in and around Pallikaranai.",
        "title": "Website Designer in Pallikaranai, Chennai | Kavitha Digital",
        "description": "Website designer in Pallikaranai, Chennai. Kavitha Digital builds websites and runs SEO and digital marketing for local businesses. Call Harish on 94459 78150.",
        "eyebrow": "Pallikaranai · Chennai 600100",
        "h1": "Website Designer in Pallikaranai, Chennai",
        "lead": "Kavitha Digital is based right here in Pallikaranai. We design websites and help local businesses get found on Google — from clinics and schools to shops, builders and service providers across the neighbourhood.",
        "image": "website-designer-pallikaranai",
        "image_alt": "Stylised map with a pin on Pallikaranai and nearby Velachery, Medavakkam, Perungudi and Thoraipakkam labelled",
        "wa_text": "a website for my Pallikaranai business",
        "service_type": "Website design and digital marketing",
        "area_served": [
            {"@type": "Place", "name": "Pallikaranai, Chennai"},
            {"@type": "Place", "name": "Velachery, Chennai"},
            {"@type": "Place", "name": "Medavakkam, Chennai"},
            {"@type": "Place", "name": "Perungudi, Chennai"},
            {"@type": "Place", "name": "Thoraipakkam, Chennai"},
        ],
        "overview": {
            "h2": "A local website design and digital marketing business in Pallikaranai",
            "paras": [
                "Pallikaranai has changed quickly. Once known mainly for its marshland, it is now a busy residential and commercial neighbourhood between Velachery, Medavakkam and the IT corridor, with the Pallavaram–Thoraipakkam Radial Road linking it to GST Road and OMR. New apartments, clinics, schools, shops and service businesses have followed — and so has competition for local customers.",
                "When residents need a service, most search on their phones: “dentist near me”, “tuition centre Pallikaranai”, “interior designer near me”. Kavitha Digital helps local businesses appear in those searches and make a strong impression when they do, with a professional website, a complete Google Business Profile and marketing that reaches people nearby.",
                "Because we're based in Pallikaranai ourselves, we understand the area, its customers and how they choose local businesses. Whether you need a new website, [local SEO](@svc-local-seo) or a complete [digital marketing plan](@loc-chennai-digital-marketing), you'll work directly with Harish.",
            ],
            "glance": [
                ("Office", "Pallikaranai, Chennai – 600100"),
                ("Owner", "Harish"),
                ("Services", "Website design, SEO, local SEO, Google Ads and social media"),
                ("Phone / WhatsApp", "{PHONE}"),
            ],
        },
        "businesses": {
            "h2": "Pallikaranai businesses we can help",
            "lead": "The neighbourhood's mix of families, professionals and new residents creates demand for a wide range of local services.",
            "items": [
                ("heart-pulse", "Clinics, hospitals and diagnostic centres", "Healthcare is one of the area's busiest categories. Clear treatment pages and a well-managed Business Profile help patients choose with confidence."),
                ("graduation", "Schools, tuition and coaching centres", "Parents compare options carefully. A website with courses, timings, facilities and easy enquiry options makes the shortlist."),
                ("home", "Builders, apartments and interiors", "New residential projects and home-improvement businesses need galleries, project details and enquiry forms that capture serious buyers."),
                ("store", "Shops, supermarkets and showrooms", "Local search and Google Maps visibility bring walk-ins from nearby streets and apartment communities."),
                ("utensils", "Restaurants, bakeries and caterers", "Photos, menus, reviews and WhatsApp ordering help food businesses stand out."),
                ("briefcase", "Professionals and home-based businesses", "Consultants, tutors, freelancers and home bakers benefit from a simple, credible website and Business Profile."),
            ],
        },
        "services": {
            "h2": "Services for businesses in Pallikaranai",
            "items": [
                ("svc-website-design", "Website design in Pallikaranai", "A fast, mobile-friendly website that presents your services clearly, shows you're local and makes calling or messaging you easy."),
                ("svc-local-seo", "SEO services in Pallikaranai", "Google Business Profile optimisation, local keywords and a review routine, so you appear when nearby customers search."),
                ("svc-google-ads", "Digital marketing in Pallikaranai", "Location-targeted Google Ads and social media campaigns that reach residents within a few kilometres of your business."),
            ],
        },
        "nearby": {
            "h2": "Nearby areas we serve from Pallikaranai",
            "paras": [
                "Pallikaranai sits at the centre of a cluster of growing South Chennai neighbourhoods. From here it's a short trip to Velachery, Medavakkam, Perungudi, Thoraipakkam, Sholinganallur, Madipakkam and Narayanapuram, and businesses in all of these areas can work with us easily.",
                "Many of our local SEO recommendations for Pallikaranai businesses apply to these areas too — people often search across neighbouring localities when choosing a clinic, school or service provider.",
            ],
            "areas": [
                "Velachery", "Medavakkam", "Perungudi", "Thoraipakkam", "Sholinganallur", "Madipakkam",
                "Narayanapuram", "OMR", "Tambaram", {"name": "Chennai", "key": "loc-chennai-digital-marketing"},
            ],
        },
        "approach": {
            "h2": "How we work with local businesses",
            "lead": "Being nearby keeps things simple.",
            "steps": [
                ("Talk to Harish", "Call or WhatsApp and explain what you need — a new website, more calls or better Google visibility."),
                ("Local review", "We look at your website, Business Profile and nearby competitors, and suggest priorities."),
                ("Clear proposal", "A written scope, timeline and quote for the agreed work."),
                ("Build and launch", "Your website or campaign goes live, with progress shared at every stage."),
                ("Ongoing support", "Updates, reports and a local contact whenever you need help."),
            ],
        },
        "faq_h2": "Pallikaranai FAQs",
        "faqs": [
            ("Is Kavitha Digital actually based in Pallikaranai?", "Yes. Kavitha Digital is based in Pallikaranai, Chennai – 600100, and run by Harish. We don't have branch offices elsewhere."),
            ("Can SEO help my Pallikaranai business get more customers?", "Yes, especially local SEO. Many residents search for services “near me” or by area name. A complete Google Business Profile, genuine reviews and a website that clearly mentions Pallikaranai and nearby areas help you appear in those searches."),
            ("Do you only work with businesses in Pallikaranai?", "No. Pallikaranai is our base, and we work with businesses across Chennai. See our [digital marketing company in Chennai](@loc-chennai-digital-marketing) page."),
            ("I searched “website designer near me”. How do I get started?", "Call or WhatsApp Harish on {PHONE} and tell him a little about your business. Being in Pallikaranai, we're close by for local businesses, and we'll agree the easiest way to discuss your project."),
            ("How much does a website cost for a small local business?", "It depends on the number of pages, the content and the features you need. Small local businesses often need a focused site with a handful of pages, which keeps costs manageable. You'll get a written quote after a short conversation."),
        ],
        "related_locations": ["loc-chennai-website-design", "loc-chennai-digital-marketing", "loc-chennai-seo"],
        "related_services": ["svc-website-design", "svc-local-seo", "svc-google-ads"],
        "cta": {"h2": "Need a website designer in Pallikaranai?",
                "text": "Call or WhatsApp Harish — your local contact for website design, SEO and digital marketing.",
                "button": "Get a Free Consultation"},
    },
]
