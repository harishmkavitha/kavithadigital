"""
Kavitha Digital — content/services.py — V1
One dictionary per service page. build.py renders them with the service template.

Link to any page with  [anchor text](@page-key)  — keys are listed in README.md.
Keep each page's copy unique: never duplicate paragraphs between services.
"""

SERVICES = [
    # =====================================================================
    # 1. WEBSITE DESIGN
    # =====================================================================
    {
        "key": "svc-website-design",
        "path": "services/website-design.html",
        "label": "Website Design",
        "menu_desc": "Custom sites that turn visitors into enquiries",
        "icon": "layout",
        "card_text": "Custom, professional websites planned around your customers — clear messaging, strong calls to action and a design that builds trust.",
        "title": "Professional Website Design Services | Kavitha Digital",
        "description": "Professional, mobile-friendly website design for Chennai businesses: custom layouts, clear messaging and enquiry-focused pages from Kavitha Digital, Pallikaranai.",
        "eyebrow": "Website design services",
        "h1": "Professional Website Design That Turns Visitors into Enquiries",
        "lead": "Kavitha Digital designs clean, fast, mobile-friendly business websites for companies in Chennai — planned around what your customers need to know before they call, WhatsApp or visit.",
        "image": "website-design-company-chennai",
        "image_alt": "Illustration of a business website layout in a browser window with colour and typography panels",
        "wa_text": "a new website design",
        "service_type": "Website design",
        "intro": {
            "h2": "Website design built around your customers, not a template",
            "paras": [
                "Your website is often the first conversation a customer has with your business. If it looks dated, loads slowly on a phone or makes people hunt for your phone number, they quietly move on to the next result on Google.",
                "Our website design service starts with your business: what you sell, who buys it, which areas you serve and what makes people choose you. From there we plan the pages, write clear headings and design layouts that guide visitors towards one action — calling, sending a WhatsApp message or filling in an enquiry form.",
                "Every design is [responsive](@svc-responsive) from the start, built to load quickly and structured for [search engine optimisation](@svc-seo), so the site is ready to be found as well as admired. Once a design is approved, our [website development](@svc-website-development) process turns it into a fast, secure live website.",
            ],
            "audience_title": "Who it's for",
            "audience": [
                ("New businesses", "Launching in Chennai and needing a credible first website."),
                ("Growing SMEs", "Outgrown a basic site and want one that generates enquiries."),
                ("Established firms", "Need a redesign that reflects the quality of their work today."),
                ("Service providers", "Clinics, consultants, contractors and studios who win work on trust."),
            ],
        },
        "problems": {
            "h2": "Common website problems we fix",
            "lead": "Most businesses that contact us already have a website. It just isn't doing its job.",
            "items": [
                ("It looks outdated", "An old design makes a capable business look small or inactive. Visitors judge credibility in seconds, long before they read about your services."),
                ("It is hard to use on phones", "Most local searches happen on mobile. Tiny text, broken layouts and buttons that are hard to tap send people straight back to Google."),
                ("It gets visits but no enquiries", "Unclear headings, missing calls to action and buried contact details mean interested visitors leave without getting in touch."),
                ("Nobody can update it", "Sites built on heavy themes, or by a developer who has moved on, become impossible to change — so information goes out of date."),
            ],
        },
        "features": {
            "h2": "What's included in our website design service",
            "lead": "A complete, practical package — not just a pretty home page.",
            "items": [
                ("compass", "Discovery and page planning", "We map your services, customers and competitors, then plan a sitemap and page structure before any design work begins."),
                ("layout", "Custom page layouts", "Distinct layouts for your home, service, about and contact pages, designed for your brand rather than a recycled theme."),
                ("pen", "Conversion-focused copy guidance", "Clear headlines, benefit-led sections and calls to action. We can also write the words through our [content marketing](@svc-content) service."),
                ("devices", "Mobile-first design", "Layouts designed for small screens first, then scaled up for tablets, laptops and large monitors."),
                ("message", "Enquiry paths", "Click-to-call buttons, WhatsApp chat links and enquiry forms placed where visitors actually need them."),
                ("search", "SEO-ready structure", "Logical headings, descriptive page titles, meta descriptions and internal links set up from day one."),
            ],
        },
        "benefits": {
            "h2": "What a well-designed website does for your business",
            "paras": [
                "A good website works for you around the clock. It answers the questions customers would otherwise ask on the phone, shows your work and makes the next step obvious.",
                "Design is not decoration here — every section has a job, whether that is building trust, explaining a service or prompting an enquiry.",
            ],
            "items": [
                ("First impressions that build trust", "A professional look that matches the quality of your products or services."),
                ("More enquiries from the same traffic", "Clear calls to action and easy contact options turn more visits into conversations."),
                ("A stronger base for marketing", "[Google Ads](@svc-google-ads) and [social media](@svc-social-media) campaigns perform better when they send people to a focused, persuasive page."),
                ("Less time answering the same questions", "Services, areas, process and FAQs explained clearly on the site."),
            ],
        },
        "process": {
            "h2": "How we design your website",
            "lead": "A clear five-step process, so you always know what happens next.",
            "steps": [
                ("Discovery call", "We learn about your business, customers, competitors and goals, and agree what the website must achieve."),
                ("Plan and structure", "We propose a sitemap, page list and content outline for your approval before design starts."),
                ("Design", "You review the home page design first, then key inner pages, with rounds of feedback built in."),
                ("Build and test", "The approved design is built, tested on phones, tablets and desktops, and checked for speed and SEO basics."),
                ("Launch and handover", "We connect your domain, submit the sitemap to Google and explain how future updates are handled."),
            ],
        },
        "why": {
            "h2": "Why businesses choose Kavitha Digital for website design",
            "items": [
                ("You work directly with Harish", "The person you brief is the person responsible for your project — no account managers passing messages along."),
                ("Design and marketing under one roof", "Your site is planned with SEO, Google Ads and social media in mind, not bolted on later."),
                ("Clear scope before work begins", "You know what is included, what content is needed from you and how long each stage takes."),
                ("Built to be fast", "Lightweight code and optimised images, because speed matters to visitors and to Google."),
            ],
        },
        "local": {
            "h2": "Website design for Chennai businesses",
            "paras": [
                "Based in Pallikaranai, we design websites for businesses across South Chennai and the wider city. See how we work as a [website design company in Chennai](@loc-chennai-website-design), or as your local [website designer in Pallikaranai](@loc-pallikaranai).",
            ],
            "links": ["loc-chennai-website-design", "loc-pallikaranai", "loc-chennai-digital-marketing"],
        },
        "related": ["svc-website-development", "svc-responsive", "svc-seo", "svc-ecommerce", "svc-content", "svc-maintenance"],
        "faq_h2": "Website design questions, answered",
        "faqs": [
            ("How much does website design cost in Chennai?", "The cost depends on the number of pages, whether content writing is included, custom features such as booking or e-commerce, and how much design work is involved. After a short discovery call we share a written quote with a clear scope. Our guide to [what affects website design cost](@post-website-cost) explains the main factors."),
            ("How long does it take to design and build a website?", "A focused business website with a handful of pages typically takes a few weeks from approved plan to launch. Larger sites, e-commerce stores or projects waiting on content take longer. We agree a timeline at the start and share progress at every stage."),
            ("Will my website be mobile friendly?", "Yes. Every site we design is fully responsive and tested at real phone, tablet and desktop sizes. Read more about our [responsive web design](@svc-responsive) approach."),
            ("Can you redesign my existing website?", "Yes. We review what works on your current site, keep useful content and search visibility where possible, and redesign the structure and look. When page addresses change, we plan redirects so existing Google rankings are not thrown away."),
            ("Do I need to provide the content?", "You know your business best, so we usually start with your input. If writing isn't your strength, we can plan and write the page content for you through our [content marketing](@svc-content) service."),
            ("Do you provide SEO after the website is built?", "Every website launches with SEO basics in place. For ongoing growth in Google, our [SEO services](@svc-seo) and [local SEO](@svc-local-seo) cover content, technical improvements and Google Business Profile work."),
        ],
        "cta": {"h2": "Ready for a website that brings in enquiries?",
                "text": "Tell Harish about your business and get a clear plan and written quote for your new website.",
                "button": "Get a Website Quote"},
    },

    # =====================================================================
    # 2. WEBSITE DEVELOPMENT
    # =====================================================================
    {
        "key": "svc-website-development",
        "path": "services/website-development.html",
        "label": "Website Development",
        "menu_desc": "Fast, secure, custom-built websites",
        "icon": "code",
        "card_text": "Fast, secure and search-friendly websites built with clean code, working forms and the integrations your business depends on.",
        "title": "Website Development Company in Chennai | Kavitha Digital",
        "description": "Custom website development in Chennai: fast, secure, SEO-ready websites with clean code, working forms, integrations and easy updates. Talk to Kavitha Digital.",
        "eyebrow": "Website development · Chennai",
        "h1": "Website Development in Chennai: Fast, Secure and Built to Grow",
        "lead": "We turn approved designs into reliable, fast-loading websites — hand-built with clean HTML, CSS and JavaScript or on the platform that suits your business, with forms, integrations and tracking that work from day one.",
        "image": "web-development-chennai",
        "image_alt": "Illustration of a code editor beside a website preview and a page speed indicator",
        "wa_text": "website development",
        "service_type": "Website development",
        "intro": {
            "h2": "Custom website development for Chennai businesses",
            "paras": [
                "Design decides how your website looks. Development decides how well it works — how quickly it loads on a patchy mobile connection, whether forms reliably reach you, how secure it is and how easily it can grow.",
                "As a website development company based in Pallikaranai, Chennai, we build business websites with lean, standards-based code. For most brochure and lead-generation sites that means fast static pages with no unnecessary plugins. When you need more — a product catalogue, bookings, a members area or an [online store](@svc-ecommerce) — we choose the platform that fits your budget and the people who will manage it.",
                "Every build follows the plan agreed during [website design](@svc-website-design), is tested across devices and ships with [SEO foundations](@svc-seo) in place.",
            ],
            "audience_title": "A good fit if you need",
            "audience": [
                ("A fast, low-maintenance site", "Lean pages that load quickly and have fewer moving parts to break."),
                ("Custom features", "Enquiry flows, calculators, galleries, booking or catalogue pages."),
                ("Integrations", "WhatsApp, Google Maps, analytics, payment gateways or your CRM."),
                ("A rebuild", "An existing site that is slow, insecure or impossible to update."),
            ],
        },
        "problems": {
            "h2": "Development problems that cost businesses enquiries",
            "items": [
                ("Slow pages", "Heavy themes, oversized images and dozens of plugins make pages crawl on mobile data, and visitors leave before they load."),
                ("Forms that fail silently", "An enquiry form that stops sending emails can go unnoticed for weeks — and every lead in that time is lost."),
                ("Security worries", "Outdated software and abandoned plugins are a common way business websites get hacked or filled with spam."),
                ("Locked-in platforms", "Some website builders make it hard to move your site, change hosts or add features without starting over."),
            ],
        },
        "features": {
            "h2": "What our website development includes",
            "items": [
                ("zap", "Performance-first build", "Images in modern formats, minimal JavaScript and clean markup for quick loading and healthy Core Web Vitals."),
                ("code", "Clean, semantic code", "Well-structured HTML that search engines and screen readers understand, with styles and scripts kept organised."),
                ("message", "Working lead capture", "Tested enquiry forms, click-to-call and WhatsApp links, connected to the tools you already use."),
                ("lock", "Security basics", "HTTPS, sensible form protection and no unnecessary plugins or admin panels exposed to attack."),
                ("bar-chart", "Analytics and tracking", "Visitor analytics and conversion tracking, so you can see which pages and channels bring enquiries."),
                ("layers", "Room to grow", "A folder structure and templates that make adding service pages, locations or blog posts straightforward."),
            ],
        },
        "benefits": {
            "h2": "Why solid development matters",
            "paras": [
                "Search engines reward pages that load fast and work well on mobile. So do customers. Good development quietly improves every other part of your marketing.",
                "It also saves money over time: a well-built site needs fewer emergency fixes and is simpler to extend when your business adds new services.",
            ],
            "items": [
                ("Faster pages", "Quicker loading keeps impatient mobile visitors on your site."),
                ("Reliable enquiries", "Forms and contact buttons tested before launch, not after a lost lead."),
                ("Easier updates", "Organised code and templates mean changes take minutes, not days."),
                ("Better SEO foundations", "Technical quality supports every page's chance to rank."),
            ],
        },
        "process": {
            "h2": "Our development process",
            "steps": [
                ("Technical plan", "We confirm features, integrations, hosting and the right platform for your site and budget."),
                ("Build", "Pages are developed from the approved design using reusable components for consistency."),
                ("Integrate", "Forms, WhatsApp, maps, analytics and any third-party services are connected and configured."),
                ("Test", "Every page is checked on phones, tablets and desktops, forms are tested end to end and speed is reviewed."),
                ("Launch and support", "We go live, watch the first days closely and offer ongoing [website maintenance](@svc-maintenance)."),
            ],
        },
        "why": {
            "h2": "Why work with Kavitha Digital on development",
            "items": [
                ("No unnecessary bloat", "We only add plugins, libraries and features that earn their place."),
                ("Your site, your accounts", "We recommend setting up your domain and hosting in your business's name, so you stay in control."),
                ("Design and development together", "No gaps between the person who planned your site and the person who builds it."),
                ("Local and reachable", "Based in Pallikaranai — a phone call or WhatsApp message away when you need a change."),
            ],
        },
        "local": {
            "h2": "Website development across Chennai",
            "paras": [
                "We develop websites for businesses in Pallikaranai, Velachery, Perungudi, Thoraipakkam, OMR and across Chennai. Comparing agencies? Read our page on choosing a [website design company in Chennai](@loc-chennai-website-design).",
            ],
            "links": ["loc-chennai-website-design", "loc-pallikaranai", "loc-chennai-digital-marketing"],
        },
        "related": ["svc-website-design", "svc-responsive", "svc-ecommerce", "svc-maintenance", "svc-seo"],
        "faq_h2": "Website development FAQs",
        "faqs": [
            ("Which platform will you build my website on?", "It depends on what the site needs to do and who will update it. Many business sites work best as fast static websites with no database to maintain. Sites that need a product catalogue, bookings or frequent updates by your team may be better on a content management system or an e-commerce platform. We explain the trade-offs before recommending one."),
            ("Can you fix or speed up my existing website?", "Often, yes. We start with a review of speed, mobile usability and errors. Sometimes targeted fixes are enough; sometimes a rebuild is more cost-effective. We'll tell you which, and why."),
            ("Will my website be secure?", "We use HTTPS, avoid unnecessary plugins, protect forms against spam and keep software up to date. Ongoing security checks are part of our [website maintenance](@svc-maintenance) service."),
            ("Can I update the website myself?", "Yes, if you want to. We can build on a platform with an easy editor, or keep a lean static site and handle updates for you. We agree this at the planning stage."),
            ("Can forms send enquiries to email or WhatsApp?", "Yes. Enquiry forms can deliver to email, a form service, a spreadsheet or straight into WhatsApp, and we test each route before launch."),
            ("Do you build landing pages for ads?", "Yes. Focused landing pages for [Google Ads](@svc-google-ads) and social media campaigns are among the things we build most often, with tracking set up so you can measure results."),
        ],
        "cta": {"h2": "Need a website that is fast, reliable and easy to grow?",
                "text": "Share what your website needs to do and Harish will recommend the right build and platform.",
                "button": "Discuss Your Website"},
    },

    # =====================================================================
    # 3. RESPONSIVE WEB DESIGN
    # =====================================================================
    {
        "key": "svc-responsive",
        "path": "services/responsive-web-design.html",
        "label": "Responsive Web Design",
        "menu_label": "Responsive Website Design",
        "menu_desc": "Looks right on every phone and screen",
        "icon": "devices",
        "card_text": "Websites that adapt to every screen — easy to read, tap and navigate on phones, tablets, laptops and large monitors.",
        "title": "Responsive Web Design in Chennai | Kavitha Digital",
        "description": "Mobile-friendly, responsive website design for Chennai businesses — sites that read clearly and load quickly on every phone, tablet, laptop and large screen.",
        "eyebrow": "Responsive web design",
        "h1": "Responsive Web Design for Mobile-First Chennai Customers",
        "lead": "Most of your customers will see your website on a phone first. We design and build mobile-friendly websites that read clearly, load quickly and stay easy to use on every screen — from a small 320px phone to a 4K monitor.",
        "image": "responsive-web-design-chennai",
        "image_alt": "Illustration of one website layout adapting across a desktop monitor, tablet and smartphone",
        "wa_text": "a mobile-friendly website",
        "service_type": "Responsive web design",
        "intro": {
            "h2": "What responsive web design really means",
            "paras": [
                "A responsive website rearranges itself to suit the screen it is viewed on. Columns stack on phones, text stays readable without zooming, images resize and buttons remain large enough to tap with a thumb.",
                "It sounds simple, but many business websites still show a shrunken desktop layout on mobile — or a separate, stripped-down mobile site that hides important information. Google uses the mobile version of your site for indexing and ranking, so a poor mobile experience affects your search visibility as well as your visitors.",
                "We design mobile-first: the phone layout is planned before the desktop one. It's part of every [website design](@svc-website-design) and [website development](@svc-website-development) project we deliver, and we also convert existing sites that aren't mobile friendly.",
            ],
            "audience_title": "You need this if",
            "audience": [
                ("Your site isn't mobile friendly", "Visitors pinch and zoom, or text runs off the screen."),
                ("Most enquiries start on phones", "Calls and WhatsApp messages come from mobile visitors."),
                ("Your layout breaks on tablets", "Menus overlap or images spill out of their boxes."),
                ("You run mobile ads", "Paid clicks land on pages that are hard to use on a phone."),
            ],
        },
        "problems": {
            "h2": "Mobile problems that drive customers away",
            "items": [
                ("Text too small to read", "Visitors should never have to zoom. We use comfortable text sizes and line lengths on every device."),
                ("Buttons too close together", "Tiny links and cramped menus cause mis-taps and frustration. Touch targets are sized for thumbs."),
                ("Sideways scrolling", "Wide tables, images and fixed-width sections that force horizontal scrolling look broken — we remove them."),
                ("Slow mobile loading", "Desktop-sized images sent to phones waste data. We serve appropriately sized images to each screen."),
            ],
        },
        "features": {
            "h2": "What's included",
            "items": [
                ("smartphone", "Mobile-first layouts", "Every page planned for small screens first, then enhanced for larger ones."),
                ("type", "Readable typography", "Fluid text sizes that stay comfortable to read on phones, tablets and large displays."),
                ("pointer", "Touch-friendly navigation", "A clear mobile menu, large tap targets, and call and WhatsApp buttons within easy reach."),
                ("image", "Responsive images", "Modern image formats in several sizes, so phones download less and pages load faster."),
                ("monitor", "Tested across screen sizes", "Checked at common phone, tablet, laptop and desktop widths, including very small and very large screens."),
                ("eye", "Accessibility basics", "Good colour contrast, visible focus states and keyboard-friendly menus."),
            ],
        },
        "benefits": {
            "h2": "Why mobile-friendly design pays off",
            "paras": [
                "Local searches like “website designer near me” or “clinic in Velachery” are made mostly on phones, often by people ready to call. A mobile-friendly site turns more of those searches into conversations.",
            ],
            "items": [
                ("A better experience on every device", "One website that works everywhere — no separate mobile version to maintain."),
                ("Support for your SEO", "Mobile usability and speed are part of how Google evaluates pages."),
                ("More calls and messages", "Contact buttons that are always easy to reach on a phone."),
                ("Future-proof layouts", "Fluid designs adapt to new screen sizes without a redesign."),
            ],
        },
        "process": {
            "h2": "How we make your website responsive",
            "steps": [
                ("Audit", "We test your current site or design on phones, tablets and desktops and list every issue."),
                ("Mobile-first plan", "We decide what matters most on small screens and how content should reflow."),
                ("Design and build", "Flexible grids, fluid typography and responsive images are built in."),
                ("Cross-device testing", "Every template is checked at multiple widths and on touch devices before launch."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for responsive design",
            "items": [
                ("Mobile-first by default", "Responsive design is standard in every project, not an optional extra."),
                ("Speed-conscious", "We keep pages light so they load well on mobile data."),
                ("SEO-aware", "Mobile improvements are made with your search visibility in mind."),
                ("Practical advice", "If your current site can be fixed rather than rebuilt, we'll say so."),
            ],
        },
        "local": {
            "h2": "Mobile-friendly websites for Chennai businesses",
            "paras": [
                "Whether your customers find you on the Velachery main road or search from an office on OMR, they are probably holding a phone. Read more about our work as a [website designer in Pallikaranai](@loc-pallikaranai) and a [website design company in Chennai](@loc-chennai-website-design).",
            ],
            "links": ["loc-pallikaranai", "loc-chennai-website-design"],
        },
        "related": ["svc-website-design", "svc-website-development", "svc-seo", "svc-local-seo", "svc-maintenance"],
        "faq_h2": "Responsive design FAQs",
        "faqs": [
            ("How do I know if my website is mobile friendly?", "Open it on your phone and try to find your services, read a page and contact the business. If you need to zoom, scroll sideways or tap more than once to hit a button, it isn't mobile friendly. We can check it for free and send you a short list of issues."),
            ("Can you make my existing website responsive?", "Often, yes. Depending on how the site was built, we either update the existing templates or rebuild them on a responsive foundation, whichever is more cost-effective for you."),
            ("Does a responsive website help with Google rankings?", "Google indexes and ranks the mobile version of websites, so mobile usability and speed matter. A responsive site won't rank on its own, but it removes a common obstacle. Our [SEO services](@svc-seo) cover the rest."),
            ("Will my website work on very large screens too?", "Yes. We cap line lengths for readability and scale layouts and text sensibly on large monitors and 4K displays, so pages never look stretched."),
            ("Is a separate mobile site better?", "Rarely. A single responsive site is easier to maintain, avoids duplicate content and gives every visitor the same information."),
        ],
        "cta": {"h2": "Is your website losing mobile visitors?",
                "text": "Send us your website address and we'll check how it performs on phones and tablets — free.",
                "button": "Get a Free Mobile Check"},
    },

    # =====================================================================
    # 4. E-COMMERCE
    # =====================================================================
    {
        "key": "svc-ecommerce",
        "path": "services/ecommerce-website-development.html",
        "label": "E-commerce Development",
        "menu_desc": "Online stores that are easy to buy from",
        "icon": "cart",
        "card_text": "Online stores with clear product pages, secure payments and smooth checkout — built to be found on Google and easy to manage.",
        "title": "E-commerce Website Development Chennai | Kavitha Digital",
        "description": "E-commerce website development in Chennai: online stores with product catalogues, secure UPI and card payments, shipping, WhatsApp orders and SEO-ready pages.",
        "eyebrow": "E-commerce website development",
        "h1": "E-commerce Website Development in Chennai",
        "lead": "Sell online with a store that is easy to browse, simple to buy from and straightforward for your team to manage. We design and build e-commerce websites for Chennai retailers, manufacturers and direct-to-consumer brands.",
        "image": "ecommerce-website-development-chennai",
        "image_alt": "Illustration of an online store with a product grid, shopping cart and order confirmation",
        "wa_text": "an e-commerce website",
        "service_type": "E-commerce website development",
        "intro": {
            "h2": "Online store development that fits how you sell",
            "paras": [
                "Every business sells differently. A boutique may need a handful of beautifully presented products and WhatsApp orders. A distributor may need hundreds of products, variants and bulk enquiries. A food brand may need delivery areas and time slots.",
                "We start by understanding your products, delivery options and who will run the store day to day. Then we recommend the right approach — a hosted e-commerce platform, an open-source store or a lean catalogue with WhatsApp ordering — and build the store around your customers' buying journey.",
                "Stores are designed with the same care as our [website design](@svc-website-design) projects and set up for [SEO](@svc-seo) from the start, with clean product URLs, structured data and fast category pages.",
            ],
            "audience_title": "Built for",
            "audience": [
                ("Retailers going online", "Shops adding an online channel alongside the store."),
                ("Direct-to-consumer brands", "Brands selling their own products to customers across India."),
                ("Manufacturers and wholesalers", "Catalogues with enquiry or bulk-order options."),
                ("Home businesses", "Bakers, crafters and small brands ready to move beyond Instagram messages."),
            ],
        },
        "problems": {
            "h2": "E-commerce problems we solve",
            "items": [
                ("Orders stuck in chats", "Taking every order through Instagram or WhatsApp chats becomes chaotic as you grow. A store organises products, payments and orders."),
                ("Abandoned checkouts", "Long forms, surprise charges and slow pages make shoppers give up. We keep checkout short and transparent."),
                ("Products that never appear on Google", "Thin product pages and copied manufacturer descriptions are invisible in search. We structure product and category pages to be found."),
                ("A store that's hard to manage", "If adding a product takes an hour, the catalogue goes stale. We set up simple workflows your team can follow."),
            ],
        },
        "features": {
            "h2": "What your online store includes",
            "items": [
                ("grid", "Product catalogue", "Categories, filters, variants such as size and colour, and product photography layouts that sell."),
                ("credit-card", "Secure payments", "Integration with Indian payment gateways for UPI, cards, net banking and wallets, plus cash on delivery if you offer it."),
                ("truck", "Shipping and delivery", "Delivery zones, shipping rates and order notifications configured for how you fulfil orders."),
                ("whatsapp", "WhatsApp ordering", "Order-on-WhatsApp buttons for businesses that prefer a conversation before the sale."),
                ("search", "SEO-ready product pages", "Unique titles, descriptions, product schema and clean URLs for every product and category."),
                ("bar-chart", "Sales tracking", "E-commerce analytics showing which products, pages and campaigns drive sales."),
            ],
        },
        "benefits": {
            "h2": "What a well-built store gives you",
            "paras": [
                "An online store extends your opening hours to 24/7 and your reach beyond your neighbourhood — but only if people can find it and trust it enough to pay.",
            ],
            "items": [
                ("Sales around the clock", "Customers browse and buy when it suits them."),
                ("Less manual order handling", "Orders, payments and stock in one place."),
                ("Reach beyond your area", "Sell across Chennai, Tamil Nadu and the rest of India."),
                ("Better returns from ads", "[Google Ads](@svc-google-ads) and [social media ads](@svc-social-media) can send shoppers straight to the right product."),
            ],
        },
        "process": {
            "h2": "How we build your online store",
            "steps": [
                ("Discovery", "Products, pricing, payments, delivery and the team who will manage the store."),
                ("Platform and plan", "We recommend a platform and plan categories, product templates and checkout flow."),
                ("Design and build", "Store design, product templates, payment gateway and shipping set-up."),
                ("Products and testing", "We load products or train your team, then test orders, payments and emails end to end."),
                ("Launch and grow", "Go live, then promote the store with SEO, ads and social media."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for e-commerce",
            "items": [
                ("Honest platform advice", "We recommend what suits your catalogue and budget, not what is easiest for us."),
                ("Marketing built in", "Your store is planned alongside SEO, Google Ads and social media campaigns."),
                ("Training at handover", "We show your team how to add products and process orders."),
                ("One point of contact", "Harish manages your project from discovery to launch."),
            ],
        },
        "local": {
            "h2": "E-commerce for Chennai businesses",
            "paras": [
                "We work with retailers and brands anywhere in Chennai, whether you have a shop in Pallikaranai or sell only online. Pair your store with our [digital marketing services in Chennai](@loc-chennai-digital-marketing) to bring in your first customers.",
            ],
            "links": ["loc-chennai-digital-marketing", "loc-pallikaranai", "loc-chennai-seo"],
        },
        "related": ["svc-website-development", "svc-seo", "svc-google-ads", "svc-social-media", "svc-content", "svc-graphic-design"],
        "faq_h2": "E-commerce website FAQs",
        "faqs": [
            ("Which e-commerce platform is best for my business?", "It depends on your catalogue size, budget, how often products change and who will manage the store. Hosted platforms are quick to launch and easy to run; open-source platforms offer more control; a simple catalogue with WhatsApp ordering can suit small ranges. We explain the pros and cons for your situation."),
            ("Can customers pay using UPI?", "Yes. Indian payment gateways support UPI, cards, net banking and wallets. We integrate the gateway you choose and test live payments before launch."),
            ("Can I manage products and orders myself?", "Yes. We set up the store so your team can add products, update prices and process orders, and we walk you through it at handover."),
            ("How will people find my online store?", "Through search, ads and social media. Product and category pages are built for [SEO](@svc-seo), and we can run [Google Ads](@svc-google-ads), including Shopping campaigns, plus [social media marketing](@svc-social-media) to drive early sales."),
            ("Can you add a store to my existing website?", "Often, yes — either as a section of your current site or as a connected store. We review your current setup and recommend the cleanest option."),
            ("How long does an e-commerce website take?", "It depends mainly on the number of products, custom features and how quickly product photos and descriptions are ready. We share a realistic schedule after discovery."),
        ],
        "cta": {"h2": "Ready to sell online?",
                "text": "Tell us about your products and how you deliver, and we'll recommend the right store setup.",
                "button": "Plan Your Online Store"},
    },

    # =====================================================================
    # 5. SEO SERVICES
    # =====================================================================
    {
        "key": "svc-seo",
        "path": "services/seo-services.html",
        "label": "SEO Services",
        "menu_desc": "Technical, on-page and off-page SEO",
        "icon": "search",
        "card_text": "Technical, on-page and off-page SEO that helps the right customers find your business on Google — with transparent reporting.",
        "title": "SEO Services: Technical, On-Page & Off-Page | Kavitha Digital",
        "description": "Search engine optimisation services for Chennai businesses: technical SEO, on-page SEO, content and ethical link building to grow Google visibility and enquiries.",
        "eyebrow": "Search engine optimisation",
        "h1": "SEO Services That Grow Your Visibility on Google",
        "lead": "Kavitha Digital helps Chennai businesses rank for the searches their customers actually make — through technical fixes, better pages, useful content and ethical link building. No shortcuts and no guaranteed-ranking promises: just steady work you can measure.",
        "image": "seo-services-chennai",
        "image_alt": "Illustration of a search results page with a highlighted listing and an SEO audit checklist",
        "wa_text": "SEO for my website",
        "service_type": "Search engine optimisation",
        "intro": {
            "h2": "Search engine optimisation built for long-term growth",
            "paras": [
                "When someone in Chennai searches for a service you offer, the businesses on the first page get the calls. SEO is the work of earning a place there — making your website technically sound, clearly relevant to what people search for and trusted enough to rank.",
                "Our SEO services cover the three areas search engines look at: **technical SEO** (can Google crawl, render and understand your site?), **on-page SEO** (does each page clearly answer a search?) and **off-page SEO** (do other reputable websites and listings vouch for you?).",
                "For businesses that serve customers in specific areas, we combine this with [local SEO](@svc-local-seo) and Google Business Profile work. Comparing providers? Our page on choosing an [SEO company in Chennai](@loc-chennai-seo) explains what to look for.",
            ],
            "audience_title": "SEO is right for you if",
            "audience": [
                ("Customers search for what you sell", "People look for your service or product on Google."),
                ("You rely on ads alone", "And want enquiries that don't stop when the ad budget does."),
                ("Competitors outrank you", "Even though your service is as good or better."),
                ("You've launched a new site", "And need it to start appearing in search."),
            ],
        },
        "problems": {
            "h2": "SEO problems we find most often",
            "items": [
                ("Pages Google can't properly read", "Slow loading, blocked resources, duplicate pages and missing sitemaps stop search engines from understanding a site."),
                ("One page trying to rank for everything", "A single services page listing ten services rarely ranks for any of them. Each important service needs its own focused page."),
                ("Thin, generic content", "Copy that could describe any business gives Google and customers little reason to choose you."),
                ("No trust signals", "Few quality links, inconsistent business listings and no reviews make it hard to compete in crowded searches."),
            ],
        },
        "features": {
            "h2": "What our SEO services include",
            "items": [
                ("gauge", "Technical SEO", "Crawlability, indexing, site speed, Core Web Vitals, mobile usability, structured data, sitemaps and crawl-error fixes."),
                ("file-text", "On-page SEO", "Keyword research, page titles, meta descriptions, headings, internal links and content improvements for each key page."),
                ("key", "Keyword and competitor research", "The searches your customers make — including local and “near me” variations — and what top-ranking pages do well."),
                ("pen", "Content planning", "Service pages, location pages and articles that answer real questions, delivered through our [content marketing](@svc-content) service."),
                ("link", "Off-page SEO", "Ethical link building, citations on reputable directories and digital PR — never spammy link packages."),
                ("pie-chart", "Reporting you can read", "Monthly reports on visibility, traffic, enquiries and the work completed, explained in plain language."),
            ],
        },
        "benefits": {
            "h2": "What SEO can do for your business",
            "paras": [
                "SEO takes time, but the results compound. A page that ranks well keeps bringing visitors every day without a cost for each click.",
                "We never promise a specific ranking — nobody honestly can. What we do promise is transparent work, clear priorities and reporting that shows what changed.",
            ],
            "items": [
                ("Steady, compounding traffic", "Rankings built on quality tend to last longer than paid visibility."),
                ("Visitors with intent", "People searching for your service are already looking to buy or book."),
                ("Lower cost per enquiry over time", "Organic enquiries don't carry a per-click cost."),
                ("A stronger website overall", "Technical and content improvements help every visitor, not just Google."),
            ],
        },
        "process": {
            "h2": "How our SEO process works",
            "steps": [
                ("SEO audit", "A full review of technical health, content, competitors, links and your current visibility."),
                ("Strategy and priorities", "A clear plan: which pages to fix, create or merge, and which keywords to target first."),
                ("On-page and technical fixes", "We implement improvements to speed, structure, titles, content and internal linking."),
                ("Content and authority", "New pages and articles, plus ethical link building and citation work."),
                ("Measure and refine", "Monthly reporting and adjustments based on what the data shows."),
            ],
        },
        "why": {
            "h2": "Why businesses choose Kavitha Digital for SEO",
            "items": [
                ("Ethical, white-hat methods", "No link farms, keyword stuffing or tricks that risk penalties."),
                ("We can fix things ourselves", "As website developers too, we implement technical changes rather than just listing them."),
                ("Plain-language reporting", "You'll understand what was done and why it matters."),
                ("Realistic expectations", "We explain likely timelines honestly instead of guaranteeing rankings."),
            ],
        },
        "local": {
            "h2": "SEO for Chennai and Pallikaranai businesses",
            "paras": [
                "Local competition varies from one neighbourhood to the next. We help businesses rank for the searches that matter in their area — see our [SEO company in Chennai](@loc-chennai-seo) page, or how we support businesses near our [Pallikaranai base](@loc-pallikaranai).",
            ],
            "links": ["loc-chennai-seo", "loc-pallikaranai", "loc-chennai-digital-marketing"],
        },
        "related": ["svc-local-seo", "svc-content", "svc-website-development", "svc-google-ads", "svc-responsive"],
        "faq_h2": "SEO questions, answered",
        "faqs": [
            ("How long does SEO normally take?", "Most websites start to see meaningful movement within three to six months, depending on competition, the site's history and how much needs fixing. Quick wins, such as fixing technical errors or improving page titles, can help sooner. SEO is an ongoing investment rather than a one-off task."),
            ("Can you guarantee first-page rankings?", "No — and be cautious of anyone who does. Google's results depend on many factors outside any agency's control. We commit to transparent, ethical work and clear reporting on the results it produces."),
            ("What is the difference between technical, on-page and off-page SEO?", "Technical SEO makes sure search engines can crawl and understand your site. On-page SEO improves the content and structure of individual pages. Off-page SEO builds trust signals, such as links and business citations, from other websites."),
            ("Do I need SEO if I already run Google Ads?", "Ads bring immediate visibility for as long as you pay. SEO builds visibility that continues without a per-click cost. Many businesses use both — our article on [SEO vs Google Ads](@post-seo-vs-ads) explains how to decide."),
            ("Will you need access to my website?", "Yes, to implement changes. We also ask for access to Google Search Console and analytics so we can measure progress. If we built your site, we already have what we need."),
            ("Do you offer SEO for small businesses?", "Yes. Many of the businesses we work with are small and local. We focus effort where it will make the biggest difference first, so smaller budgets are used well."),
        ],
        "cta": {"h2": "Want more customers to find you on Google?",
                "text": "Start with an SEO review of your website and a clear list of priorities.",
                "button": "Start Your SEO Project"},
    },

    # =====================================================================
    # 6. LOCAL SEO
    # =====================================================================
    {
        "key": "svc-local-seo",
        "path": "services/local-seo.html",
        "label": "Local SEO",
        "more": "Local SEO Services",
        "menu_desc": "Google Maps and “near me” visibility",
        "icon": "map-pin",
        "card_text": "Show up in Google Maps and “near me” searches with an optimised Google Business Profile, consistent listings and genuinely useful local pages.",
        "title": "Local SEO & Google Business Profile Chennai | Kavitha Digital",
        "description": "Local SEO in Chennai: Google Business Profile optimisation, map pack visibility, review strategy and local pages that bring nearby customers to your business.",
        "eyebrow": "Local SEO · Google Business Profile",
        "h1": "Local SEO Services: Get Found in Google Maps and “Near Me” Searches",
        "lead": "When nearby customers search for what you offer, local SEO helps your business appear in the Google map pack and local results — with the right address, phone number, photos and reasons to choose you.",
        "image": "local-seo-chennai",
        "image_alt": "Illustration of a map with location pins beside a list of local business results",
        "wa_text": "local SEO and Google Maps",
        "service_type": "Local SEO",
        "intro": {
            "h2": "What is local SEO?",
            "paras": [
                "Local SEO is the part of search engine optimisation focused on location-based searches — “dentist in Velachery”, “interior designer near me” or “AC service Pallikaranai”. For these searches Google shows a map with three businesses, often called the map pack, above the regular results, and those businesses receive a large share of the calls.",
                "Google decides which businesses to show based on relevance, distance and prominence. We improve the parts you can influence: a complete, accurate Google Business Profile, consistent business details across the web, a steady flow of genuine reviews, and website pages that clearly connect your services to the areas you serve.",
                "Local SEO works best alongside core [SEO services](@svc-seo) and a [mobile-friendly website](@svc-responsive) that makes calling you effortless. For a practical overview, read our [local SEO checklist for Chennai businesses](@post-local-seo).",
            ],
            "audience_title": "Ideal for",
            "audience": [
                ("Shops and showrooms", "Businesses that want more walk-ins and direction requests."),
                ("Clinics and salons", "Appointment-led businesses serving nearby residents."),
                ("Home and trade services", "Plumbers, electricians, interiors and repair services covering set areas."),
                ("Restaurants and caterers", "Food businesses competing in crowded local searches."),
            ],
        },
        "problems": {
            "h2": "Why local businesses stay invisible on Google Maps",
            "items": [
                ("An incomplete Business Profile", "Missing categories, services, photos and descriptions give Google less to work with — and customers less reason to call."),
                ("Inconsistent business details", "Different phone numbers or address formats across directories confuse Google about which details are correct."),
                ("Few or old reviews", "Reviews influence both rankings and choice. A profile with no recent reviews looks inactive."),
                ("No local pages on the website", "If your website never mentions the areas you serve, it's harder for Google to connect you with those searches."),
            ],
        },
        "features": {
            "h2": "What our local SEO service includes",
            "items": [
                ("map-pin", "Google Business Profile optimisation", "Categories, services, description, photos, products and posts — completed and kept up to date."),
                ("list-check", "Citation and NAP consistency", "Your name, address and phone number made consistent across important directories such as JustDial, Sulekha and IndiaMART where relevant."),
                ("message", "Review strategy", "A simple, policy-compliant routine for asking happy customers for reviews, and guidance on responding to every review."),
                ("file-text", "Local landing pages", "Useful, genuinely different pages for the areas you serve — never copy-and-paste doorway pages."),
                ("navigation", "Local on-page SEO", "Location signals in titles, headings, content and structured data on your key pages."),
                ("activity", "Call and direction tracking", "Tracking of calls, website visits and direction requests from your profile, so you can see what's working."),
            ],
        },
        "benefits": {
            "h2": "What local SEO can bring",
            "paras": [
                "Local searches often come from people who are ready to act — today. Appearing in the map pack puts your phone number and directions in front of them at exactly the right moment.",
            ],
            "items": [
                ("More calls from nearby customers", "Call buttons on your profile and site make contact one tap away."),
                ("More walk-ins and direction requests", "Accurate map listings guide customers to your door."),
                ("Trust before the first conversation", "Photos, reviews and complete information answer questions early."),
                ("A lasting local presence", "A well-maintained profile keeps working month after month."),
            ],
        },
        "process": {
            "h2": "How we improve your local visibility",
            "steps": [
                ("Local audit", "We review your Business Profile, listings, reviews, website and local competitors."),
                ("Fix the foundations", "Profile completion, category choice and NAP clean-up across directories."),
                ("Build local relevance", "Location-aware page updates and genuinely useful local landing pages."),
                ("Grow reviews and activity", "A review-request routine plus regular profile updates and posts."),
                ("Track and report", "Monthly reporting on calls, direction requests, website clicks and local rankings."),
            ],
        },
        "why": {
            "h2": "Why choose Kavitha Digital for local SEO",
            "items": [
                ("We're local ourselves", "Based in Pallikaranai, we know how people across South Chennai search for services."),
                ("Policy-safe methods", "No fake reviews, keyword-stuffed business names or virtual-office tricks."),
                ("Website and profile together", "We improve both your Business Profile and the website it links to."),
                ("Clear reporting", "Calls, directions and clicks — the numbers that matter to a local business."),
            ],
        },
        "local": {
            "h2": "Local SEO across Chennai",
            "paras": [
                "Whether you serve one neighbourhood or several — from Pallikaranai and Medavakkam to Thoraipakkam, Sholinganallur and Tambaram — we help you appear where your customers are searching. See our [SEO company in Chennai](@loc-chennai-seo) page and our page for [businesses in Pallikaranai](@loc-pallikaranai).",
            ],
            "links": ["loc-pallikaranai", "loc-chennai-seo", "loc-chennai-digital-marketing"],
        },
        "related": ["svc-seo", "svc-content", "svc-google-ads", "svc-responsive", "svc-website-design"],
        "faq_h2": "Local SEO questions, answered",
        "faqs": [
            ("What is local SEO?", "Local SEO is the process of improving how your business appears in location-based searches and on Google Maps. It combines your Google Business Profile, consistent business listings, reviews and location-relevant website content."),
            ("Can SEO help businesses in Pallikaranai?", "Yes. Searches like “clinic in Pallikaranai” or “interior designer near me” are local by nature. A complete Business Profile, genuine reviews and a website that clearly mentions the areas you serve all help. See our page for [businesses in Pallikaranai](@loc-pallikaranai)."),
            ("How long does local SEO take to work?", "Fixing profile and listing issues can show results within weeks, while competitive categories take several months of consistent work. We share progress every month."),
            ("Do I need a physical address to rank on Google Maps?", "Google requires either a real business location or a defined service area. Service-area businesses can hide their address and list the areas they cover. We follow Google's guidelines — never virtual offices or fake addresses."),
            ("Can you get us more Google reviews?", "We set up a simple routine for asking genuine customers for reviews and help you respond to them. We never buy or write fake reviews, which break Google's policies and can get a profile suspended."),
            ("Can I rank in areas where I don't have an office?", "You can appear for searches in nearby areas you genuinely serve, especially through useful service-area pages on your website. Ranking far from your location is harder in the map pack, and we'll be honest about what's realistic."),
        ],
        "cta": {"h2": "Want to show up when locals search for you?",
                "text": "Get a free review of your Google Business Profile and local visibility.",
                "button": "Improve Your Google Visibility"},
    },

    # =====================================================================
    # 7. GOOGLE ADS
    # =====================================================================
    {
        "key": "svc-google-ads",
        "path": "services/google-ads.html",
        "label": "Google Ads",
        "more": "Google Ads Management",
        "menu_label": "Google Ads / PPC",
        "menu_desc": "PPC campaigns built around real enquiries",
        "icon": "target",
        "card_text": "Search, Performance Max and call campaigns set up around your budget, with conversion tracking so you know what each enquiry costs.",
        "title": "Google Ads Management in Chennai | Kavitha Digital",
        "description": "Google Ads and PPC management in Chennai: search, Performance Max and call campaigns built around your budget, with conversion tracking and honest reporting.",
        "eyebrow": "Google Ads & PPC management",
        "h1": "Google Ads Management for Chennai Businesses",
        "lead": "Put your business at the top of Google today. We plan, build and manage Google Ads campaigns that focus your budget on the searches most likely to become calls, WhatsApp messages and sales — and show you exactly what they cost.",
        "image": "google-ads-management-chennai",
        "image_alt": "Illustration of an advertising campaign dashboard with bar charts and a sponsored search result",
        "wa_text": "Google Ads management",
        "service_type": "Pay-per-click advertising management",
        "intro": {
            "h2": "PPC management focused on enquiries, not just clicks",
            "paras": [
                "Google Ads can deliver enquiries within days of launch. It can also burn through a budget quickly if campaigns target the wrong searches, send clicks to a weak page or run without tracking.",
                "Our Google Ads management starts with the basics that make the biggest difference: tight keyword targeting, negative keywords to filter out irrelevant searches, compelling ads, focused landing pages and conversion tracking for calls, forms and WhatsApp clicks. Then we manage and refine the account every month.",
                "Ads work best alongside a strong website and long-term [SEO](@svc-seo). Unsure which to start with? Read [SEO vs Google Ads for small businesses](@post-seo-vs-ads), or see our wider [digital marketing services in Chennai](@loc-chennai-digital-marketing).",
            ],
            "audience_title": "Google Ads suits",
            "audience": [
                ("Businesses needing leads now", "New launches, seasonal offers or a quiet sales pipeline."),
                ("Competitive local services", "Where organic rankings will take time to earn."),
                ("E-commerce stores", "Shopping campaigns that show products, prices and images."),
                ("High-value services", "Where the value of a customer comfortably justifies paid clicks."),
            ],
        },
        "problems": {
            "h2": "Why Google Ads campaigns waste money",
            "items": [
                ("Broad, untargeted keywords", "Ads appearing for loosely related searches attract clicks from people who were never going to buy."),
                ("No conversion tracking", "Without tracking calls and forms, there's no way to know which keywords bring customers and which just spend money."),
                ("Clicks sent to the home page", "Paid visitors need a focused page that matches the ad. A generic home page loses many of them."),
                ("Set-and-forget management", "Campaigns left unchanged drift as competition, costs and search behaviour change."),
            ],
        },
        "features": {
            "h2": "What our Google Ads management includes",
            "items": [
                ("key", "Keyword and competitor research", "Finding high-intent searches, estimating costs and building negative keyword lists."),
                ("target", "Campaign setup", "Search, Performance Max, call-focused and Shopping campaigns, structured so each ad group stays relevant."),
                ("pen", "Ad copy and assets", "Headlines, descriptions, sitelinks, and call and location assets written to earn qualified clicks."),
                ("layout", "Landing pages", "Focused landing pages built through our [website development](@svc-website-development) service to turn clicks into enquiries."),
                ("activity", "Conversion tracking", "Tracking for calls, form submissions and WhatsApp clicks, so decisions are based on real results."),
                ("bar-chart", "Monthly optimisation and reports", "Bid, budget, keyword and ad improvements, with a clear report on spend, enquiries and cost per enquiry."),
            ],
        },
        "benefits": {
            "h2": "What well-managed Google Ads delivers",
            "paras": [
                "Paid search puts you in front of people at the moment they search. Managed well, it gives you a predictable, measurable flow of enquiries you can scale up or down.",
            ],
            "items": [
                ("Fast visibility", "Campaigns can go live quickly — useful for launches and offers."),
                ("Control over spend", "Set daily budgets and focus on the areas and hours that matter."),
                ("Measurable results", "See the cost per call, form or sale, not just clicks."),
                ("Useful search insights", "Real search-term data that also informs your SEO and content."),
            ],
        },
        "process": {
            "h2": "How we manage your campaigns",
            "steps": [
                ("Account review or setup", "We audit an existing account or build a new one with the right structure."),
                ("Tracking first", "Conversion tracking for calls, forms and WhatsApp is set up before spend increases."),
                ("Launch", "Campaigns go live with tightly themed ad groups and matching landing pages."),
                ("Optimise", "We review search terms, add negatives, test ads and adjust bids and budgets."),
                ("Report", "A monthly summary of spend, enquiries, cost per enquiry and next steps."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for Google Ads",
            "items": [
                ("Your account stays yours", "Campaigns run in an ad account owned by your business."),
                ("Transparent spend", "Ad spend and management fees are kept separate and clearly reported."),
                ("Landing pages in-house", "We build and improve the pages your ads send people to."),
                ("Honest recommendations", "If ads aren't the right fit for your budget or market, we'll tell you."),
            ],
        },
        "local": {
            "h2": "Google Ads for Chennai businesses",
            "paras": [
                "Target the areas you actually serve — a radius around Pallikaranai, specific neighbourhoods such as Velachery and Medavakkam, or the whole of Chennai. Location targeting keeps your budget focused on customers who can use your service. Learn more about our [digital marketing company in Chennai](@loc-chennai-digital-marketing).",
            ],
            "links": ["loc-chennai-digital-marketing", "loc-pallikaranai"],
        },
        "related": ["svc-seo", "svc-local-seo", "svc-social-media", "svc-website-development", "svc-ecommerce"],
        "faq_h2": "Google Ads questions, answered",
        "faqs": [
            ("Do you manage Google Ads?", "Yes. We set up new accounts, take over existing ones and manage campaigns every month — keywords, ads, bids, budgets, landing pages and reporting."),
            ("How much should I spend on Google Ads?", "It depends on how competitive your keywords are, the areas you target and the value of a customer. We estimate likely click costs during research and recommend a starting budget you're comfortable with, then adjust based on results."),
            ("How quickly will I see results?", "Ads can start showing as soon as campaigns are approved, and many businesses receive their first enquiries within the first weeks. The first month or two is also a learning period while keywords and bids are refined."),
            ("Can you track phone calls from ads?", "Yes. We set up tracking for calls from ads and from your website, as well as form submissions and WhatsApp clicks."),
            ("Should I run Google Ads or invest in SEO?", "Ads bring immediate visibility while you pay; SEO builds longer-term visibility. Many businesses use ads for quick results while SEO grows. Read our guide to [SEO vs Google Ads](@post-seo-vs-ads)."),
            ("Can you target only certain areas of Chennai?", "Yes. Campaigns can target a radius around your location, specific areas or PIN codes, or the whole city, and exclude places you don't serve."),
        ],
        "cta": {"h2": "Want enquiries from Google this month?",
                "text": "Book a free review of your Google Ads account — or plan your first campaign with us.",
                "button": "Plan Your Google Ads"},
    },

    # =====================================================================
    # 8. SOCIAL MEDIA MARKETING
    # =====================================================================
    {
        "key": "svc-social-media",
        "path": "services/social-media-marketing.html",
        "label": "Social Media Marketing",
        "menu_desc": "Facebook and Instagram content and ads",
        "icon": "share",
        "card_text": "Facebook and Instagram content, ads and lead generation planned around your customers — with clear monthly reporting.",
        "title": "Social Media Marketing in Chennai | Kavitha Digital",
        "description": "Social media marketing in Chennai: Facebook and Instagram content, advertising and lead generation planned around your customers, with clear monthly reporting.",
        "eyebrow": "Social media marketing",
        "h1": "Social Media Marketing in Chennai: Content and Ads That Build Demand",
        "lead": "We help Chennai businesses use Facebook, Instagram and other platforms to stay visible, build trust and generate enquiries — with consistent content, targeted ads and reporting that goes beyond likes.",
        "image": "social-media-marketing-chennai",
        "image_alt": "Illustration of a smartphone showing a social media post next to a content calendar",
        "wa_text": "social media marketing",
        "service_type": "Social media marketing",
        "intro": {
            "h2": "Social media that supports real business goals",
            "paras": [
                "For many local businesses, social media is where customers check you out before they call. An active, professional profile reassures them; an abandoned page with a post from last year raises doubts.",
                "We plan social media around what you want to achieve — more enquiries, more footfall, a product launch or stronger brand recognition. That means choosing the right platforms, creating content your audience cares about and using Facebook and Instagram advertising to reach specific people in specific areas.",
                "Strong visuals matter here, so our [graphic design](@svc-graphic-design) service keeps your posts consistent with your brand. When campaigns send people to your website, a focused landing page from our [website design](@svc-website-design) service turns interest into enquiries.",
            ],
            "audience_title": "Great for",
            "audience": [
                ("Visual businesses", "Interiors, restaurants, fashion, events and real estate."),
                ("Local service providers", "Clinics, salons, gyms and coaching centres."),
                ("Launches and offers", "New branches, products and seasonal promotions."),
                ("Lead generation", "Businesses using Instagram and Facebook lead ads."),
            ],
        },
        "problems": {
            "h2": "Social media problems we solve",
            "items": [
                ("Posting without a plan", "Random posts whenever someone remembers rarely build an audience or bring enquiries."),
                ("Inconsistent branding", "Different styles, fonts and colours in every post make a business look disorganised."),
                ("Boosting posts blindly", "Pressing “boost” without proper targeting spends money on people who will never become customers."),
                ("No link to results", "Likes and followers are easy to count; enquiries and sales need proper tracking."),
            ],
        },
        "features": {
            "h2": "What our social media marketing includes",
            "items": [
                ("calendar", "Monthly content plan", "A calendar of posts, stories and reel ideas tied to your services, offers and seasons."),
                ("image", "Branded creatives", "Post and ad designs that follow your brand style, created with our [graphic design](@svc-graphic-design) service."),
                ("megaphone", "Facebook and Instagram ads", "Campaigns for awareness, traffic, messages and leads, targeted by location, interests and demographics."),
                ("users", "Lead generation campaigns", "Lead forms and click-to-WhatsApp ads that deliver enquiries straight to you."),
                ("refresh", "Retargeting", "Reaching people who visited your website or engaged with your content but haven't enquired yet."),
                ("pie-chart", "Reporting", "Monthly reporting on reach, engagement, enquiries and ad spend, with recommendations."),
            ],
        },
        "benefits": {
            "h2": "What consistent social media marketing brings",
            "paras": [
                "Social media keeps your business in front of people between the moments they search. Combined with search marketing, it builds familiarity, so when they need you, they already know your name.",
            ],
            "items": [
                ("Stronger brand recognition", "Regular, consistent content builds familiarity in your area."),
                ("Targeted reach", "Ads can focus on specific parts of Chennai and specific audiences."),
                ("Direct conversations", "Click-to-WhatsApp and lead ads start conversations quickly."),
                ("Social proof", "Showing your work and behind-the-scenes moments builds trust."),
            ],
        },
        "process": {
            "h2": "How we run your social media",
            "steps": [
                ("Understand your audience", "Who your customers are, which platforms they use and what they respond to."),
                ("Plan", "Content themes, a monthly calendar and campaign objectives."),
                ("Create", "Designs, captions and ad creatives prepared for your approval."),
                ("Publish and promote", "Scheduled posting and targeted ad campaigns."),
                ("Review", "Monthly results, what worked and what we'll change next."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for social media",
            "items": [
                ("Connected to your website and SEO", "Social campaigns link to pages built to convert."),
                ("Design and copy together", "Creatives and captions planned as one piece."),
                ("Results over vanity metrics", "Reporting focuses on enquiries and actions, not just likes."),
                ("Approval before anything goes live", "You see and approve content before it's published."),
            ],
        },
        "local": {
            "h2": "Social media marketing for Chennai businesses",
            "paras": [
                "We plan campaigns that reach people in the parts of Chennai you serve — whether that's a few kilometres around Pallikaranai or the whole city. Our [digital marketing company in Chennai](@loc-chennai-digital-marketing) page shows how social media fits into a wider plan.",
            ],
            "links": ["loc-chennai-digital-marketing", "loc-pallikaranai"],
        },
        "related": ["svc-graphic-design", "svc-content", "svc-google-ads", "svc-website-design", "svc-ecommerce"],
        "faq_h2": "Social media marketing FAQs",
        "faqs": [
            ("Which social media platforms should my business be on?", "The ones your customers use. For most local businesses in Chennai, Instagram and Facebook are the starting point; LinkedIn suits B2B services, and YouTube suits businesses that can explain or demonstrate their work on video. We recommend a focused mix rather than every platform."),
            ("How often should we post?", "Consistency matters more than volume. A realistic schedule of quality posts each week usually beats daily posts that feel rushed. We agree a frequency that fits your goals and budget."),
            ("Do you run Facebook and Instagram ads?", "Yes. We plan, create and manage ads for awareness, website traffic, messages and lead generation, targeted by location, age, interests and more."),
            ("Can social media generate leads for my business?", "Yes, particularly with lead forms and click-to-WhatsApp ads. Results depend on your offer, audience and budget, and we track enquiries so you can see what each campaign delivers."),
            ("Do we need to provide photos?", "Real photos of your work, team and premises perform best, and we'll guide you on what to capture. We also design graphics and can use suitably licensed images where needed."),
        ],
        "cta": {"h2": "Ready to make social media work for your business?",
                "text": "Tell us your goals and we'll suggest a practical content and advertising plan.",
                "button": "Grow Your Business Online"},
    },

    # =====================================================================
    # 9. CONTENT MARKETING
    # =====================================================================
    {
        "key": "svc-content",
        "path": "services/content-marketing.html",
        "label": "Content Marketing",
        "menu_desc": "Website copy, blogs and guides that rank",
        "icon": "pen",
        "card_text": "Website copy, service pages, blogs and guides written for your customers first and search engines second.",
        "title": "Content Marketing Services in Chennai | Kavitha Digital",
        "description": "Content marketing in Chennai: website copy, blogs, guides and service pages written for your customers and search engines, planned around real questions.",
        "eyebrow": "Content marketing & copywriting",
        "h1": "Content Marketing That Answers Your Customers' Questions",
        "lead": "Useful content is how websites earn search visibility and trust. We plan and write service pages, location pages, blog articles and guides that answer real customer questions — in clear, human language.",
        "image": "content-marketing-chennai",
        "image_alt": "Illustration of an article being written in an editor with a content outline checklist",
        "wa_text": "content marketing",
        "service_type": "Content marketing",
        "intro": {
            "h2": "Content that works for readers and for Google",
            "paras": [
                "Before someone contacts a business, they usually have questions: How much will it cost? How long will it take? Is this the right option for me? Businesses that answer those questions clearly on their websites earn trust — and search engines notice.",
                "Our content marketing service turns your knowledge into pages people want to read. We research the questions your customers ask, the searches they make and what competitors cover, then write content with a clear structure, a natural tone and helpful links to your services.",
                "Content is the engine behind effective [SEO services](@svc-seo) and gives your [social media](@svc-social-media) something worth sharing. You can see the approach in action on the [Kavitha Digital blog](@blog).",
            ],
            "audience_title": "Useful when",
            "audience": [
                ("Your pages are thin", "Service pages with a few lines that don't explain much."),
                ("You don't have time to write", "You know your subject but can't find the hours."),
                ("You want to rank for more searches", "Each topic deserves a focused, helpful page."),
                ("You're launching a new site", "And need professional copy from day one."),
            ],
        },
        "problems": {
            "h2": "Content problems holding websites back",
            "items": [
                ("Generic copy", "Phrases like “quality service at the best price” appear on thousands of sites and say nothing about you."),
                ("Written for search engines, not people", "Keyword-stuffed text reads badly and no longer works — Google rewards helpful content."),
                ("No plan", "Occasional blog posts on random topics rarely build visibility or support sales."),
                ("Content that never gets updated", "Old prices, services or information quietly erode trust."),
            ],
        },
        "features": {
            "h2": "What our content marketing includes",
            "items": [
                ("key", "Topic and keyword research", "Finding the questions and searches that matter to your customers and your business."),
                ("list-check", "Content strategy", "A plan that maps topics to pages — services, locations, guides, FAQs and articles."),
                ("file-text", "Website and service page copy", "Clear, persuasive pages that explain what you do and prompt enquiries."),
                ("pen", "Blog articles and guides", "In-depth, well-structured articles that answer customer questions and link to your services."),
                ("refresh", "Content updates", "Refreshing existing pages that have lost visibility or gone out of date."),
                ("share", "Repurposing", "Turning articles into social posts, FAQs and email content."),
            ],
        },
        "benefits": {
            "h2": "Why content is worth investing in",
            "paras": [
                "Well-written content keeps working long after it is published. A helpful guide can attract visitors and build trust for years.",
            ],
            "items": [
                ("More search visibility", "Every useful page is another way for customers to find you."),
                ("Better-informed enquiries", "Customers arrive already understanding your services and process."),
                ("Authority in your field", "Helpful, accurate content shows real expertise."),
                ("Material for every channel", "Content feeds your social media, ads and email."),
            ],
        },
        "process": {
            "h2": "Our content process",
            "steps": [
                ("Research", "Customer questions, keywords, competitors and your own expertise."),
                ("Plan", "A content calendar with topics, formats and target pages."),
                ("Write", "Drafts in a clear, natural voice with a logical structure and internal links."),
                ("Review", "You check facts and tone; we refine."),
                ("Publish and promote", "Pages are formatted, optimised and shared across your channels."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for content",
            "items": [
                ("Reviewed for accuracy", "Content is checked with you for facts and tone before it goes live."),
                ("SEO-aware without stuffing", "Keywords are used naturally, where they help the reader."),
                ("Local understanding", "We write for Chennai audiences and the way they search."),
                ("Connected to your goals", "Every piece links to a service or a clear next step."),
            ],
        },
        "local": {
            "h2": "Content for Chennai businesses",
            "paras": [
                "We write content that reflects how Chennai customers search and buy — including area pages for the neighbourhoods you genuinely serve. Our [Pallikaranai page](@loc-pallikaranai) shows how local content can stay useful rather than repetitive.",
            ],
            "links": ["loc-pallikaranai", "loc-chennai-seo", "loc-chennai-digital-marketing"],
        },
        "related": ["svc-seo", "svc-local-seo", "svc-social-media", "svc-website-design", "svc-graphic-design"],
        "faq_h2": "Content marketing FAQs",
        "faqs": [
            ("Do you write content for new websites?", "Yes. We can write all the copy for a new website — home, about, service, location and contact pages — working from a short interview and any material you already have."),
            ("Will the content be original?", "Yes. Every page is written specifically for your business. We don't copy competitor content or publish mass-produced text."),
            ("How often should we publish blog posts?", "Quality and relevance matter more than frequency. A few genuinely helpful articles each month usually outperform frequent short posts. We'll suggest a realistic schedule."),
            ("Can you write content in Tamil?", "Most business websites we work on are in English. If you need Tamil content as well, tell us at the start so we can plan the best way to handle it."),
            ("How long before content helps our SEO?", "New pages typically take from a few weeks to a few months to be indexed and gain rankings, depending on competition and your site's authority. Improving existing pages can sometimes show results sooner."),
        ],
        "cta": {"h2": "Need content that brings in the right visitors?",
                "text": "Share your website and goals, and we'll suggest the first pages and articles worth writing.",
                "button": "Plan Your Content"},
    },

    # =====================================================================
    # 10. WEBSITE MAINTENANCE
    # =====================================================================
    {
        "key": "svc-maintenance",
        "path": "services/website-maintenance.html",
        "label": "Website Maintenance",
        "menu_desc": "Updates, backups, security and fixes",
        "icon": "shield-check",
        "card_text": "Updates, backups, security checks, speed tuning and content changes — so your website stays fast, safe and current.",
        "title": "Website Maintenance Services in Chennai | Kavitha Digital",
        "description": "Website maintenance in Chennai: updates, backups, security checks, speed fixes and content changes that keep your business website fast, safe and up to date.",
        "eyebrow": "Website maintenance & support",
        "h1": "Website Maintenance Services That Keep Your Site Fast and Secure",
        "lead": "Your website is never really finished. We handle the updates, backups, security checks, fixes and content changes that keep it working properly — so you can focus on running your business.",
        "image": "website-maintenance-chennai",
        "image_alt": "Illustration of a website health dashboard showing backups, updates, SSL and security checks",
        "wa_text": "website maintenance",
        "service_type": "Website maintenance",
        "intro": {
            "h2": "Ongoing care for your business website",
            "paras": [
                "Websites need regular attention. Software needs updates, SSL certificates need renewing, forms need testing and content needs to reflect your current services, prices and contact details. Left alone, small issues become broken pages, security problems or lost enquiries.",
                "Our website maintenance service gives you a dependable person to call when something needs changing, plus routine checks that catch problems before your customers do. We maintain websites we have built, and sites built by others after an initial health check.",
                "Maintenance pairs naturally with [SEO](@svc-seo) — a healthy, up-to-date website gives your search visibility a solid foundation. Planning something bigger? A [website redesign](@svc-website-design) may cost less than repeatedly patching an old site.",
            ],
            "audience_title": "Helpful if",
            "audience": [
                ("You don't have a web person", "And changes wait weeks or never happen."),
                ("Your developer has moved on", "Leaving nobody who knows how the site works."),
                ("You worry about security", "Or have had spam, hacks or downtime before."),
                ("Your content changes often", "New services, offers, staff or projects to add."),
            ],
        },
        "problems": {
            "h2": "Problems regular maintenance prevents",
            "items": [
                ("Security vulnerabilities", "Outdated software and plugins are one of the most common ways websites get compromised."),
                ("Broken forms and links", "An enquiry form that stops working can cost weeks of leads before anyone notices."),
                ("Slowing performance", "Growing image libraries, unused plugins and old code gradually slow a site down."),
                ("Outdated information", "Old prices, discontinued services or a previous phone number confuse customers and damage trust."),
            ],
        },
        "features": {
            "h2": "What our maintenance service includes",
            "items": [
                ("refresh", "Software and plugin updates", "Core, theme and plugin updates applied carefully and tested, where your platform needs them."),
                ("database", "Regular backups", "Scheduled backups of your files and content, so the site can be restored if something goes wrong."),
                ("shield-check", "Security monitoring", "SSL checks, spam protection and security reviews to keep threats out."),
                ("activity", "Uptime and form checks", "Monitoring that your site is online and that enquiry forms still deliver."),
                ("gauge", "Speed tuning", "Image optimisation and performance checks to keep pages loading quickly."),
                ("pen", "Content changes", "Text, image, price and page updates handled for you on request."),
            ],
        },
        "benefits": {
            "h2": "Peace of mind for your online presence",
            "paras": [
                "Maintenance is insurance for your website. Preventing problems costs far less than recovering a hacked site or explaining to customers why their enquiry never got a reply.",
            ],
            "items": [
                ("Fewer surprises", "Issues spotted and fixed before they affect customers."),
                ("A faster, safer site", "Regular updates and performance checks."),
                ("Quick changes", "Updates handled without hunting for a developer."),
                ("Protected search visibility", "Downtime and errors can hurt rankings; monitoring helps prevent them."),
            ],
        },
        "process": {
            "h2": "How website maintenance works",
            "steps": [
                ("Health check", "We review your website's software, security, speed, backups and forms."),
                ("Fix urgent issues", "Critical problems are resolved first and the site is backed up."),
                ("Agree a care plan", "The checks, update frequency and content changes that suit your site."),
                ("Ongoing maintenance", "Routine updates, backups and monitoring on an agreed schedule."),
                ("Regular summaries", "A short report of what was checked, updated and fixed."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for website maintenance",
            "items": [
                ("One reliable contact", "Call or WhatsApp Harish when you need a change."),
                ("We build websites too", "So we fix underlying problems, not just symptoms."),
                ("Clear scope", "You know what's included and what counts as new work."),
                ("Honest advice", "If a rebuild would cost less than ongoing patches, we'll tell you."),
            ],
        },
        "local": {
            "h2": "Website maintenance in Chennai",
            "paras": [
                "We look after websites for businesses in Pallikaranai and across Chennai. Being local means quick conversations when something needs attention. Our [website designer in Pallikaranai](@loc-pallikaranai) page explains more about working with us locally.",
            ],
            "links": ["loc-pallikaranai", "loc-chennai-website-design"],
        },
        "related": ["svc-website-development", "svc-website-design", "svc-seo", "svc-responsive", "svc-content"],
        "faq_h2": "Website maintenance FAQs",
        "faqs": [
            ("Can you maintain my website after launch?", "Yes. Maintenance is available for every website we build, and we can take on websites built by others after an initial health check."),
            ("What if my website was built by someone else?", "We start with a health check to understand the platform, hosting, access and any existing problems. Then we recommend a care plan — or, if the site is in poor shape, explain your options."),
            ("How quickly can you make changes to my website?", "Routine content changes are handled promptly, and urgent issues such as a broken page or form are prioritised. We agree response expectations in your care plan."),
            ("Do you offer website redesign as well?", "Yes. If maintaining an older site no longer makes sense, we can plan a [redesign](@svc-website-design) that keeps your existing content and search visibility where possible."),
            ("Does a static website need maintenance?", "Static websites need far less maintenance than database-driven ones, but content updates, domain and SSL renewals, form checks and occasional improvements still matter."),
        ],
        "cta": {"h2": "Want someone reliable looking after your website?",
                "text": "Start with a website health check and a simple care plan.",
                "button": "Get a Website Health Check"},
    },

    # =====================================================================
    # 11. GRAPHIC DESIGN
    # =====================================================================
    {
        "key": "svc-graphic-design",
        "path": "services/graphic-design.html",
        "label": "Graphic Design",
        "menu_desc": "Logos, brand kits and marketing creatives",
        "icon": "palette",
        "card_text": "Logos, brand colours, social media creatives, brochures and ad designs that keep your business consistent everywhere.",
        "title": "Graphic Design & Logo Design in Chennai | Kavitha Digital",
        "description": "Graphic design in Chennai: logos, brand colours, social media creatives, brochures and ad designs that keep your business consistent online and in print.",
        "eyebrow": "Graphic design & branding",
        "h1": "Graphic Design and Logo Design for Growing Chennai Businesses",
        "lead": "A consistent, professional look makes a business easier to remember and easier to trust. We design logos, brand kits, social media creatives, brochures and marketing materials that work together online and in print.",
        "image": "graphic-design-logo-design-chennai",
        "image_alt": "Illustration of a brand kit with a logo, colour palette, typography and social media templates",
        "wa_text": "graphic design",
        "service_type": "Graphic design",
        "intro": {
            "h2": "Design that makes your business recognisable",
            "paras": [
                "Customers see your business in many places — your website, Google Business Profile, Instagram feed, WhatsApp catalogue, visiting card and shop signage. When each looks different, the business seems less established than it really is.",
                "Our graphic design service creates a clear visual identity and applies it consistently: a logo that works large and small, a colour palette, typography, and templates for the materials you use most. The same system then carries through your [website design](@svc-website-design) and [social media marketing](@svc-social-media).",
            ],
            "audience_title": "Popular with",
            "audience": [
                ("New businesses", "Needing a logo and a basic brand kit to launch with."),
                ("Businesses refreshing their look", "Modernising a dated identity without losing recognition."),
                ("Active social media users", "Needing on-brand creatives every month."),
                ("Businesses with print needs", "Brochures, flyers, banners and visiting cards."),
            ],
        },
        "problems": {
            "h2": "Design problems we solve",
            "items": [
                ("A logo that doesn't scale", "Detailed logos become unreadable as a small profile picture or browser icon."),
                ("No consistent style", "Different fonts and colours across materials weaken recognition."),
                ("Creatives made in a rush", "Last-minute posts and ads that look amateur reflect on the business."),
                ("Files you can't find or use", "No master files, so every new design starts from scratch."),
            ],
        },
        "features": {
            "h2": "What our graphic design service covers",
            "items": [
                ("pen-tool", "Logo design", "Original logo concepts with versions for light and dark backgrounds and small sizes."),
                ("palette", "Brand kit", "Colour palette, typography, logo usage guidance and visual style in one simple reference."),
                ("image", "Social media creatives", "Post, story and ad templates designed for Instagram, Facebook and LinkedIn."),
                ("printer", "Print materials", "Brochures, flyers, visiting cards, letterheads and banners prepared print-ready."),
                ("layout", "Website graphics", "Banners, icons and illustrations that fit your website design."),
                ("megaphone", "Ad creatives", "Display and social ad designs sized for each platform."),
            ],
        },
        "benefits": {
            "h2": "Why consistent design matters",
            "paras": [
                "Consistency builds recognition. When customers see the same colours, logo and style everywhere, your business feels established and trustworthy.",
            ],
            "items": [
                ("A professional first impression", "Design that reflects the quality of your work."),
                ("Faster marketing", "Templates make new posts and materials quicker to produce."),
                ("Stronger recall", "A distinctive, consistent look is easier to remember."),
                ("Ready for every channel", "Files prepared for web, social media and print."),
            ],
        },
        "process": {
            "h2": "Our design process",
            "steps": [
                ("Brief", "Your business, audience, competitors and the impression you want to create."),
                ("Concepts", "Initial design directions presented for your feedback."),
                ("Refine", "The chosen direction developed through rounds of revisions."),
                ("Deliver", "Final files in the formats you need, with simple usage guidance."),
            ],
        },
        "why": {
            "h2": "Why Kavitha Digital for graphic design",
            "items": [
                ("Design with a marketing purpose", "Every design supports your website, social media or sales."),
                ("Original work", "Designed for your business — never copied from other brands."),
                ("Consistent across channels", "The same studio handles your website, social and print design."),
                ("Files you keep", "Final files are delivered to you for future use."),
            ],
        },
        "local": {
            "h2": "Graphic design for Chennai businesses",
            "paras": [
                "We design for businesses in Pallikaranai and across Chennai, often alongside a new website or social media campaign. Our [digital marketing company in Chennai](@loc-chennai-digital-marketing) page shows how design fits into a complete plan.",
            ],
            "links": ["loc-chennai-digital-marketing", "loc-pallikaranai"],
        },
        "related": ["svc-social-media", "svc-website-design", "svc-content", "svc-ecommerce", "svc-google-ads"],
        "faq_h2": "Graphic design FAQs",
        "faqs": [
            ("Do you design logos?", "Yes. Logo design includes research, initial concepts, revisions and final files in the formats you need for web, social media and print."),
            ("What files will I receive?", "Typically vector files for print and signage, plus PNG and other web-ready formats, in colour and single-colour versions. We confirm the exact list at the start."),
            ("Can you design our social media posts every month?", "Yes. We can create a set of branded templates or produce monthly creatives as part of our [social media marketing](@svc-social-media) service."),
            ("Can you refresh our existing logo?", "Yes. A refresh can modernise your logo while keeping the recognisable elements your customers already know."),
            ("Do you handle printing?", "We prepare print-ready files to your printer's specifications and can help you brief a printer."),
        ],
        "cta": {"h2": "Want a brand that looks as good as your work?",
                "text": "Tell us what you need designed and we'll suggest the right starting point.",
                "button": "Start Your Design Project"},
    },
]
