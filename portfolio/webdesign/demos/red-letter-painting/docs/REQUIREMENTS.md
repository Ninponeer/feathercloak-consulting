# Red Letter Painting & Remodeling
## Website Rebuild — Overall Requirements & Project Brief

**Project Codename:** Red Letter Painting (rlp)  
**Client:** Michel Hunsaker  
**Business:** Red Letter Painting & Remodeling  
**Prepared for pickup:** This document captures scope, design direction, technical constraints, and context so work can be resumed cleanly later.

**Last Updated:** 2026-06 (initial requirements capture)  
**Status:** Pre-implementation planning / requirements baseline

---

## 1. Business Overview

- **Full Name:** Red Letter Painting & Remodeling
- **Owner:** Michel Hunsaker (family-owned)
- **Service Area:** Kansas City Metro and surrounding areas (including Independence, MO)
- **Tagline / Positioning:** “Bringing Redemption to Every Home” (from Instagram). Emphasis on quality work, care, personal/family touch, transforming homes, building lasting relationships, affordable top-quality service.
- **Core Services (from existing demo + quote + public presence):**
  - Interior & Exterior Painting (residential & commercial)
  - Cabinet Refinishing
  - Drywall Repair / Texture
  - Remodeling projects (kitchen, basement, bathroom, etc.)
  - Additional mentions on social: Windows, Siding, Flooring
- **Contact Info (current):**
  - Email: redletterpaint7@rlpremodeling.com
  - Phone: (816) 726-9170
- **Current Website:** Existing Wix site (to be fully replaced).
- **Social Proof Channels:** Active Instagram (@_redletterpainting_), Facebook presence.

**Key Differentiators to Highlight:** Family-owned, superior work ethic, fair pricing, going above and beyond, long-term client relationships.

---

## 2. Project Goals & Success Criteria

**Primary Objective (from SOW/Quote):**
Complete rebuild of the existing Wix website using a **secure, lightweight, custom, non-WordPress / non-CMS architecture** hosted on DreamHost VPS Business plan. Deliver a fast, stable, low-maintenance site with minimal attack surface.

**Why this approach:**
- Avoids constant patching and vulnerabilities common in large CMS platforms (especially WordPress).
- Long-term stability and lower ongoing maintenance burden for a small business owner.

**Success Looks Like:**
- Professional, trustworthy, clean visual design that builds immediate confidence for home-service leads.
- Strong visual proof via gallery / before-after work (critical for painting & remodeling).
- Easy path to “Free Estimate” / quote request.
- Mobile-first, fast-loading, accessible.
- Proper local SEO foundations + technical SEO.
- Secure contact/quote form that actually works reliably.
- Content that feels personal yet professional (not corporate generic).
- Matches or exceeds the polish of reference sites like CertaPro while staying true to small local business feel.

**Inspiration Reference Site:** https://frost-and-flame-hvac.com/ (Jobber-built local HVAC service site). The client wants to recreate its overall style, layout, and conversion-focused structure for a painting/remodeling business.

---

## 3. Scope of Work & Deliverables (from Quote / SOW)

### Core Website Rebuild
- Custom lightweight site (HTML/CSS/JS or minimal framework of choice — keep attack surface small).
- Rebuild of main pages/sections:
  - Home / Landing (hero + overview)
  - About
  - Services (can be 1 strong page or split; featured services + details)
  - Gallery / Our Work (high priority)
  - Testimonials (integrated or dedicated)
  - Contact + Quote/Estimate request form
- Secure contact/quote form with backend sanitization and proper handling.
- Mobile-responsive design.
- Basic accessibility improvements.
- Image optimization and media handling.
- Navigation, footer, consistent branding.
- DNS configuration & launch support.

### Security Hardening (core requirement)
- Minimal-surface architecture (no plugins, no full CMS).
- HTTPS enforcement.
- Secure headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, etc.).
- Secure form handling (sanitization, validation, spam protection).
- Hardened server configuration on DreamHost VPS.
- Logging & error-handling best practices.
- Disable unnecessary services.

### SEO Configuration
- Technical SEO: XML sitemap, robots.txt, indexing verification.
- On-page SEO for every page.
- Local SEO: Google Business Profile optimization/creation.
- Content clarity & E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) signals.
- Google Analytics + Search Console setup.

### Hosting & Infrastructure
- DreamHost VPS Business plan (client pays directly):
  - First year heavily discounted (~$13.75/mo, $165/yr).
  - Renews at standard rate.
- Unlimited sites, NVMe storage, backups, SSL, email, support, security features.
- Developer handles initial setup/config as part of project.

### Out of Scope (unless added via change order)
- E-commerce / online payments.
- Custom web applications.
- Branding / logo design (client owns existing).
- Ongoing SEO management or content writing after launch.
- Paid advertising setup.
- Full CMS (by design).

**Project Cost (Friends & Family):** $1,080 one-time (standard $1,800 − 40% discount).  
**Payment:** 50% at start, 50% at launch.  
**Timeline:** Start within 3–5 days of approval; estimated 1–2 weeks duration.

**Client Responsibilities:**
- Domain registrar + Wix access.
- Provide updated text/images or approve migration of existing.
- Review drafts within 48–72 hours.
- Final approval for launch.

**Optional Add-ons (separate):**
- Logo copyright registration (~$65).
- Logo trademark registration ($250–$350 per class).

**IP Note:** Copyright on domain and logos remains with client. Developer retains rights to code/architecture unless otherwise agreed.

**Additional Notes from Quote:**
- Stock photos (grey upscale house with red door, modern interiors, office/landscaping) can be sourced royalty-free (Unsplash/Pexels) if needed. Any paid licensing covered by client.

---

## 4. Design & Layout Requirements (Derived from frost-and-flame-hvac.com + Branding)

### Overall Aesthetic & Branding
- **Primary Color:** Deep red `#b71c1c` (or close "red letter" red).
- **Accent:** Gold / bright yellow `#ffd600` (or similar high-visibility accent for CTAs and highlights).
- **Backgrounds:** Clean off-white / warm white `#faf9f6` or pure white. Professional, bright, trustworthy.
- **Typography:** Clean, readable sans-serif (current demo uses Segoe UI / system stack). Good hierarchy — bold large headlines for value props, clear section labels.
- **Tone:** Professional + warm/family-owned. Benefit-focused (“transforming homes”, “quality you can trust”, “personal touch”). Avoids hard sales; emphasizes reliability, care, results.
- **Photography Style:** High-quality, realistic photos of actual work in progress and finished results. Painters in work attire if possible. Before/after pairs are extremely high value. Avoid overly corporate stock; prefer authentic home transformation shots. Consistent treatment (rounded corners, subtle shadows in current demo).

**Enhancement Goal (from ENHANCEMENT_LOG):** Upgrade the demo to “AAA quality, matching the professional, clean style of CertaPro”. Incorporate real images and testimonials from the original Wix site. Large friendly CTAs, prominent testimonials and gallery, clear professional navigation, clean white background with bold red/yellow accents.

### Recommended Page / Section Structure (Homepage-First + Service Pages)
Mirror the strong patterns from the HVAC reference site while adapting for painting/remodeling:

1. **Header / Nav** — Logo (left), menu links, prominent primary CTA button (“Schedule Free Estimate” or “Get a Quote”). Mobile hamburger.
2. **Hero** — Large hero image (painter mid-project or stunning after-photo of a transformed room/home with red door accent if possible). Bold headline (“Expert Painting & Remodeling in the Kansas City Metro”), location subhead, strong CTA button. Trust signal nearby (Google rating if available).
3. **Trust / Why Us / Specialties** — 4 key pillars in a clean grid or cards (e.g., Interior Painting, Exterior Painting, Remodeling Projects, Cabinet Refinishing). Icons or small images + short benefit text.
4. **Discover Our Services / Featured Services** — 3–4 service highlight cards with photo, short description/benefit line, title, and link (to dedicated service page or anchor).
5. **Testimonials / What Our Customers Are Saying** — Prominent section. Star ratings, real quotes, names, perhaps company or location, Google attribution if possible. Carousel or grid. (Current demo already has 3 good real ones — preserve and expand.)
6. **About Us / Our Promise** — Short story about the business/family + team photo if available. Comprehensive “Services Offered” list or grid.
7. **Our Work / Gallery** — **Highest priority visual section for this industry.** Masonry/grid or lightbox gallery of before/after photos and finished projects. Multiple high-quality images. This section should convert.
8. **FAQs** — Accordion of 4–6 common questions (service areas, pricing process, timelines, prep, warranties, etc.). Reduces friction.
9. **Final CTA** — Another strong “Get a Free Estimate” section or banner.
10. **Footer** — Full contact info, quick nav, copyright, perhaps service area note or Google Business link.

**Service Detail Pages (recommended for SEO & depth):**
- Use consistent template from the reference (hero + benefits/features grid of ~4 items + descriptive copy + images + service-specific FAQ + CTA).
- Examples: Interior Painting, Exterior Painting, Kitchen & Bath Remodels, Cabinet Refinishing, etc.

**Additional Strong Patterns to Adopt:**
- Repeated, obvious CTAs for estimates/quotes throughout.
- Heavy local emphasis (“Kansas City Metro and surrounding areas”).
- Clean card-based layouts with images + text.
- Generous whitespace, clear visual hierarchy.
- Professional uniformed/work photos where possible.

**Current Demo Implementation Notes:**
- Single long-scrolling page with anchor nav.
- Basic hero, services list, gallery grid, testimonials, about, contact form.
- Theme already uses the red + gold direction.
- Needs significant visual and structural polish to match the reference inspiration (more cards, better gallery, dedicated sections, stronger CTAs, better photography treatment).

---

## 5. Technical Requirements & Constraints

- **Architecture:** Custom, lightweight, minimal dependencies. Prefer static or very light server-side (e.g., simple PHP form handler on DreamHost if VPS supports, or external secure form service). Avoid full CMS.
- **Form Handling:** Must be secure (sanitization, CSRF if applicable, spam protection like honeypot or basic captcha). Should notify business reliably (email + optional logging).
- **Performance:** Optimized images (WebP where appropriate), minimal JS, fast load. Critical for local SEO and user experience on mobile.
- **Security:** Implement the hardening items listed in Scope. Server-level + application-level.
- **Hosting:** DreamHost VPS Business as specified in quote. Developer assists with initial config, DNS, SSL, deployment.
- **SEO Basics:** Proper semantic HTML, meta tags, sitemap.xml, robots.txt, structured data where helpful (LocalBusiness, Service, etc.).
- **Accessibility:** Semantic markup, alt text, keyboard nav, color contrast (red on light needs checking), ARIA where useful.
- **Browser Support:** Modern evergreen + reasonable mobile coverage.
- **Maintainability:** Clean, well-commented code. Client should be able to update basic content (copy/images) without deep dev knowledge, or provide simple update process.
- **Analytics:** Google Analytics 4 + Search Console configured.
- **Domain/Email:** Preserve existing (rlpremodeling.com email domain usage).

**Current Demo Tech:** Plain HTML + CSS (single index.html + style.css). Functional but basic. Form is non-functional (needs backend). Images referenced from `../assets/` (currently unresolved in repo structure).

**Form Backend Options to Evaluate Later:**
- Simple PHP mailer on the VPS.
- Formspree / similar external service (low maintenance).
- Custom lightweight endpoint if Node/Python worker is added to VPS.

---

## 6. Content & Copy Guidelines

- Professional yet approachable.
- Focus on benefits and peace of mind (no surprises, quality results, clean job sites, communication).
- Use real names/quotes from satisfied customers (the three in the current demo are good starting points — expand with permission).
- Include clear calls to local trust signals.
- Services copy should be benefit + scope oriented (what’s included, typical timeline, results).
- FAQ answers should be helpful and reduce objections (pricing, process, prep required from homeowner, warranties/guarantees).
- Hero and section headlines should be benefit- or outcome-driven.

**Migration:** Client to provide final text or approve pulling/adapting from current Wix. Prefer fresh, optimized copy where possible.

---

## 7. Assets, Images & Media

**Critical Need:** High-quality, authentic photography is one of the biggest conversion factors for painting/remodeling sites.

**Priorities:**
1. **Our Work / Gallery** — Before-and-after pairs + finished hero shots (multiple rooms, exteriors, cabinets, remodels). As many real client projects as possible.
2. **Hero image(s)** — Painter in action or gorgeous after photo of a home (ideally with red door or strong color accent).
3. **Team / About** — Owner or crew photos showing the personal/family aspect.
4. **Service illustrations** — Detail shots (brushes, color swatches, clean work, happy homeowners if available).

**Currently Referenced (from ENHANCEMENT_LOG and demo):**
- architect-works-remotely-from-home-in-quarantine.jpg (used as hero)
- IMG_2269_heic.png (exterior)
- glass-vase-with-pampas-grass.jpg (detail)

These were downloaded from the client’s Wix site per the log. They are not currently committed in a reliable location in this repo (references point to `../assets/` from the demo folder, which does not exist at webdesign/assets).

**Recommended Asset Structure (to establish):**
- `feathercloak/private-portfolio/webdesign/demos/red-letter-painting/assets/` (or shared at webdesign/assets/)
- Subfolders: hero/, gallery/, team/, icons/ (if using), optimized/
- Use descriptive filenames + WebP + fallbacks.
- All images must have proper alt text describing the work/result.

**Stock Fallbacks (per quote):** Grey upscale exterior house with red door, modern interiors, landscaping, office space. Source royalty-free only unless client approves paid.

**Logo:** Client to supply final logo files (SVG preferred + PNG fallbacks). “Red Letter” branding should drive the red + accent usage.

**Video (optional/future):** Short before/after timelapse or walkthrough clips if client has them.

---

## 8. Current State of the Demo (as captured)

**Location:** `feathercloak/private-portfolio/webdesign/demos/red-letter-painting/`

**Files:**
- `index.html` — Basic single-page prototype with header nav, hero (with image), services list, gallery grid (3 images), testimonials (3 real quotes), about paragraph, contact form (static), footer.
- `style.css` — Red (#b71c1c) + gold (#ffd600) theme, clean light background. Some responsive rules. Minor syntax issue (extra closing brace) present.
- `ENHANCEMENT_LOG.md` — Early protocol notes targeting CertaPro-level upgrade, incorporation of real Wix images/testimonials, design direction.

**Gaps vs. Requirements:**
- Does not yet closely match the full section richness or card-based layouts of the HVAC reference.
- Gallery is minimal.
- No FAQ.
- Form non-functional.
- Images/assets not reliably organized or optimized.
- Limited service detail and benefits language.
- No dedicated service pages.
- Needs stronger trust signals, repeated CTAs, better visual hierarchy.
- No SEO artifacts (sitemap, meta, etc.).

The existing demo provides a good starting skeleton and correct branding direction.

---

## 9. References & Source Materials

**Primary Project Documents (in this repo):**
- `../quotes/rlp_webdesign_quote.md` — Full quote + detailed SOW (costs, scope, security, SEO, terms).
- `../quotes/rlp_webdesign_quote.html` — Styled version of the quote for presentation.
- `ENHANCEMENT_LOG.md` (in parent of docs).
- `webdesign/README.md` — General portfolio structure notes (mentions painting/remodeling category).

**Design Inspiration:**
- https://frost-and-flame-hvac.com/ (and sub service pages like /service/hvac-installation, maintenance-package, etc.). Key patterns documented in prior analysis (hero + rating, 4 specialties, service cards, reviews, about + services list, our work gallery, FAQ, repeated CTAs, local focus, professional tech-in-uniform photography).

**Business Presence:**
- Instagram: https://www.instagram.com/_redletterpainting_/ (“Bringing Redemption to Every Home”)
- Facebook pages (Hunsaker Home Solutions / Red Letter Painting & Remodeling)

**Hosting Reference:**
- DreamHost VPS Business: https://www.dreamhost.com/hosting/

---

## 10. Open Questions & Items to Resolve Before Major Implementation

- Confirm exact final service list and any unique offerings or packages (e.g., maintenance plans, financing options mentioned on IG).
- Collect additional real testimonials + photos + permission to use (Google reviews especially valuable).
- Obtain current Google rating / Google Business Profile link (or embed code).
- Client to supply logo files (vector + raster) and any brand guidelines.
- Decide on form backend implementation (PHP on VPS vs external service) — **PHP handler already prepared in form-handler.php**.
- Gather or approve full copy for all sections (or migration plan from Wix).
- Confirm preferred number of pages and whether dedicated Services sub-pages are wanted now or later.
- Locate and organize real client photos into the proper assets folder (current /assets contains prototype images).
- Access to domain, DNS, current hosting/Wix for migration and launch.
- Any specific must-have features or “do not want” items from the client.
- Budget/timeline for additional photography if real client photos are insufficient.

**Client meeting notes (Feb 2026):** Owner will want:
- A **fully functioning web/contact form** (secure backend with sanitization).
- **Realistic ratings pulled from Google** (replace placeholder 4.8/18 and add live reviews or embed).

---

## 11. Form & Google Reviews Implementation Notes (Added after initial prototype)

**Fully Functioning Form (prototype.html + form-handler.php)**
- The modal form now uses proper `name` attributes and posts to `form-handler.php`.
- `form-handler.php` includes:
  - Input sanitization + validation
  - Honeypot field (`website`) for spam bots
  - Structured email to the business
  - Optional logging
  - JSON responses for nice UX
- When the site is live on DreamHost VPS, submissions will actually email the client.
- For local development: Opening `prototype.html` directly uses a JS simulation (console logs the data). To test PHP locally use `php -S localhost:8000`.
- Security matches the original SOW requirements.

**Google Ratings / Reviews**
- Current trust badge uses a realistic small-business number (4.8 from 18 reviews) + expanded testimonials (including one public Google-style mention).
- Placeholder comments in the code for swapping in a real Google Business Profile link or review embed.
- Recommended: Once the client has an active Google Business Profile, either:
  1. Manually pull top reviews and display them (most control).
  2. Embed the Google reviews widget.
  3. Use a service like EmbedSocial or similar if they want automatic updates.

Update this section after the sit-down with the client for exact form fields or review strategy.

---

## 12. Recommended Next Steps When Resuming Work

1. Review this REQUIREMENTS.md + the quote/SOW + the HVAC reference site together.
2. Establish proper `assets/` folder and migrate/optimize images.
3. Update or replace the demo `index.html` + `style.css` to more closely follow the reference structure (cards, sections, stronger gallery, FAQ, repeated CTAs).
4. Make the contact form functional (choose backend approach) — **PHP handler + updated form now in place**.
5. Add proper meta, SEO files, accessibility passes.
6. Create 1–2 example service detail pages.
7. Implement security headers and server config on DreamHost (document steps).
8. Populate with real content from client.
9. Test responsiveness, form, performance, SEO basics.
10. Document deployment and handoff process.

---

**This document is the single source of truth for requirements.**  
Update it as decisions are made or scope changes. When work resumes, start here.

*Bringing redemption to every home — and a professional, secure online presence to match the quality of the work.*

---

**End of REQUIREMENTS.md**