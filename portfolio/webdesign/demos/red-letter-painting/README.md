# Red Letter Painting & Remodeling — Website Demo

Professional, secure, custom website prototype and development workspace for Red Letter Painting & Remodeling (Michel Hunsaker, Kansas City Metro area).

**Tagline direction:** “Bringing Redemption to Every Home”

## Quick Start for Contributors / Future Self

1. Read the requirements first: `docs/REQUIREMENTS.md`
2. Also read `docs/README.md` for how the docs folder is organized.
3. Review the official project quote/SOW: `../quotes/rlp_webdesign_quote.md`
4. Explore the current demo: `index.html` + `style.css`
5. Reference design inspiration: https://frost-and-flame-hvac.com/ (layout, sections, trust signals, gallery emphasis, repeated CTAs, local service aesthetic)

## Current State
- Advanced client-ready prototype at `prototype.html` (Tailwind CDN, fully responsive).
- Strong visual match to the HVAC reference layout (hero + trust, 4 specialties, service cards, heavy "Our Work" gallery, testimonials, FAQ, repeated CTAs).
- 9 realistic AI-generated images in `/assets` (clearly marked as prototypes — replace with real client photos).
- **Fully prepared contact/estimate form**: Posts to `form-handler.php` (secure sanitization, validation, honeypot spam protection). On DreamHost this is a real functioning form. Local preview gives polished success UX.
- Google ratings prepared for real data (currently realistic 4.8/18 + expanded testimonials including public mentions).
- See `ENHANCEMENT_LOG.md` for early upgrade intentions (CertaPro-level polish, real imagery, etc.).

**Next anticipated from client meeting:** Fully functioning web/contact form (structure + PHP handler now in place) and pulling realistic Google ratings/reviews (placeholder ready to swap).

## Project Context (High Level)
- **Platform:** Custom lightweight non-WordPress/non-CMS (HTML/CSS/JS + minimal secure backend for form) on DreamHost VPS Business.
- **Focus:** Security hardening, performance, local SEO, trust-building visuals (especially before/after gallery), easy quote requests.
- **Budget (Friends & Family):** $1,080 project fee (details + ongoing hosting in the quote).
- **Key Pages/Surfaces:** Home (long-scroll with strong sections), About, Services, Gallery/Our Work (critical), Contact + functional secure form. Optional dedicated service detail pages.
- **Branding:** Red-dominant with gold accents. Clean, professional, warm/family-owned feel. Heavy use of authentic project photography.

## Folder Structure (this demo)
```
red-letter-painting/
├── README.md                 # You are here
├── index.html                # Current demo homepage
├── style.css
├── ENHANCEMENT_LOG.md
├── docs/                     # Requirements & planning (start here when resuming)
│   ├── README.md
│   └── REQUIREMENTS.md       # Canonical requirements document
├── assets/                   # Realistic prototype images (replace with real client photos)
├── form-handler.php          # Secure PHP backend for the estimate/contact form (DreamHost ready)
└── (future: additional pages, Google reviews embed, SEO files, etc.)
```

**Note on Assets:** Current `index.html` references `../assets/...`. Establish a proper `assets/` folder (inside this demo or at the webdesign level) and update paths + optimize images.

## Related
- Full quote & SOW: `../quotes/rlp_webdesign_quote.md` (and the styled .html version)
- Portfolio-level notes: `../../README.md`
- Instagram for real business voice & photos: https://www.instagram.com/_redletterpainting_/

## When Resuming
Always begin with the docs/ folder (especially REQUIREMENTS.md). It was created specifically so this project can be picked up cleanly later with full context.

---

*Building a site worthy of the quality of work Red Letter Painting delivers.*