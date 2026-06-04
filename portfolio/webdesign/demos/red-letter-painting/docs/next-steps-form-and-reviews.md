# Next Steps: Form + Google Reviews

**Date:** After initial prototype delivery (Feb 2026)

## Client Meeting Notes (to capture after sit-down with Michel)

The owner mentioned he will want:
- A **fully functioning web/contact form**
- **Realistic ratings pulled from Google** at some point

## What Has Already Been Prepared (Prototype)

### 1. Fully Functioning Contact/Estimate Form
**Files:**
- `prototype.html` — The modal form now has proper `name` attributes, `action="form-handler.php"`, `method="POST"`, and a honeypot field.
- `form-handler.php` — Secure PHP handler with:
  - Sanitization + validation
  - Honeypot spam protection
  - Clean email formatting
  - Optional submission logging (create `logs/` folder on server)
  - JSON responses for nice frontend feedback

**How it works on the live site (DreamHost VPS):**
- Form submissions will actually send an email to `redletterpaint7@rlpremodeling.com`
- The form is ready for the "secure contact form with backend sanitization" requirement from the original SOW.

**Local testing:**
- Opening `prototype.html` directly (file://) uses a graceful JavaScript simulation (data is logged to console).
- To test the real PHP handler locally: Run `php -S localhost:8000` from the demo folder and open `http://localhost:8000/prototype.html`.

**Recommended improvements after client meeting:**
- Ask what exact fields they want (e.g., job address, square footage estimate, how they heard about us, photo upload?).
- Decide on email notification format or whether they want submissions saved to a database / Google Sheet.
- Consider adding reCAPTCHA later for stronger spam protection.

### 2. Google Ratings / Reviews
- Trust badge in the hero is currently set to a realistic small/local business number: **4.8/5 (18 reviews)**.
- Testimonials section includes the original quotes + one additional public-style review.
- Code comments are in place for easy swap to a real Google Business Profile link or embed.

**After the meeting:**
- Get the actual Google Business Profile URL.
- Ask if they want:
  - Manually curated top reviews (recommended for control + quality)
  - Automatic Google reviews embed/widget
  - Or a combination

### Files to Watch
- `prototype.html` (main demo)
- `form-handler.php`
- `docs/REQUIREMENTS.md` (updated with this context)
- `assets/` (all current images are marked as prototypes)

## Suggested Questions for the Client Meeting
1. For the form: What information is most important for you to receive on a lead? (e.g. phone is king for painters, project type, rough size, timeline, photos of the job?)
2. Do you want the form to send you an email, or also save to a spreadsheet / CRM?
3. Do you have (or want to set up) a Google Business Profile? Can we get the link?
4. How many real testimonials / reviews do you currently have that we can use with permission?
5. Any other must-have form fields or "nice to haves"?

---

Once you have answers from the sit-down, we can refine the form fields, make the PHP handler even more tailored, and wire up the real Google rating.

This puts us in a great spot to move fast after the meeting.