"""Repair the contact/enquiry forms on the Abet Works static site.

The service pages ship an empty `<form action="/contact" class="flask-email-form">`
left over from a Flask prototype. This repo has no /contact backend, so that form
renders as a blank box and any enquiry typed into it is lost.

Forms the browser renders empty are replaced with the company's own hosted Zoho
enquiry form (the same one already embedded on services/contact.html), with the
Tripetto form as a fallback link. A form that still has real fields is left
untouched, because it may be wired to a backend outside this repo.
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZOHO = ("https://forms.zohopublic.in/abetworks/form/ClientDetails1/"
        "formperma/Gl3N5EVVlODuugDzy3KawwvQMhQfVDFToAr0jdrg61c")
TRIPESTO = "https://tripetto.app/run/BKR1M1PACY"
EMAIL = "admin@abetworks.in"

CONTACT_FORM_OPEN = re.compile(r'[ \t]*<form[^>]*action="/contact"[^>]*>')
FIELD_RE = re.compile(r'<(?:input|textarea|button)\b')

# index.html nests a comment inside a commented-out block, which is invalid HTML:
# the inner `-->` closes the outer comment early, so the empty form leaks into the
# rendered page together with stray divs. That whole region is rebuilt below.
INDEX_START = '        </div><!-- End Google Maps -->'
INDEX_END = '          </div><!-- End Contact Form -->'


def uncommented(txt):
    """Strip HTML comments, which is what the browser ultimately parses."""
    return re.sub(r"<!--.*?-->", "", txt, flags=re.S)


def classify_contact_form(txt):
    """('none'|'empty'|'filled') for the first rendered action=/contact form."""
    body = uncommented(txt)
    m = CONTACT_FORM_OPEN.search(body)
    if not m:
        return "none", None
    after = body[m.end():]
    # Stop at the </form> the browser honours: a nested <form> start tag is
    # dropped by the parser, but it still marks where this form's own content
    # effectively ends for our purposes.
    stop = re.search(r'</form\s*>|<form\b', after, re.I)
    inner = after[:stop.start()] if stop else after
    fields = len(FIELD_RE.findall(inner))
    return ("filled" if fields else "empty"), fields


def block(indent="            "):
    return (
        f'{indent}<div class="contact-form" data-aos="fade-up">\n'
        f'{indent}  <iframe title="Enquire with Abet Works" loading="lazy" frameborder="0"\n'
        f'{indent}          style="height:520px;width:100%;border:none;" src="{ZOHO}"></iframe>\n'
        f'{indent}  <p class="mt-3 mb-0">Form not loading? '
        f'<a href="{TRIPESTO}" target="_blank" rel="noopener">open the enquiry form in a new tab</a>.</p>\n'
        f'{indent}</div>'
    )


INDEX_REGION = """      <div class="container" data-aos="fade-up">
        <div class="row gy-4">

          <div class="col-lg-4">
            <div class="info-item d-flex">
              <i class="bi bi-geo-alt flex-shrink-0"></i>
              <div>
                <h3>Address</h3>
                <p>301, VS Road</p>
                <p>Mumbai, India</p>
              </div>
            </div><!-- End Info Item -->

            <div class="info-item d-flex">
              <i class="bi bi-envelope flex-shrink-0"></i>
              <div>
                <h3>Email Us</h3>
                <p><a href="mailto:{email}">{email}</a></p>
              </div>
            </div><!-- End Info Item -->

            <div class="info-item d-flex">
              <i class="bi bi-chat-dots flex-shrink-0"></i>
              <div>
                <h3>Tell us about your project</h3>
                <p>Share a few details and we will get back to you.</p>
              </div>
            </div><!-- End Info Item -->
          </div>

          <div class="col-lg-8">
{form}
          </div><!-- End Contact Form -->"""


def rebuild_index_region():
    return INDEX_REGION.format(email=EMAIL, form=block("            "))



def replace_empty_form(txt):
    """Swap the empty action=/contact form (open + its wrapper row) for the block."""
    # Match the opening tag through the </form> that the browser actually honours.
    # (?:(?!<form)...) keeps the match from running past into another form when
    # this page's </form> actually belongs to a different form.
    pattern = re.compile(
        r'[ \t]*<form[^>]*action="/contact"[^>]*>(?:(?!<form\b)[\s\S])*?</form>[ \t]*\n?', re.I)
    new, n = pattern.subn(lambda m: block("            ") + "\n", txt, count=1)
    if n:
        return new
    # Some pages never close the <form>, so it leaks into the footer. Replace
    # only the opening tag; the surrounding <div class="row"> stays balanced.
    return CONTACT_FORM_OPEN.sub(lambda m: block("            "), txt, count=1)


def main():
    changed, skipped = [], []
    for path in sorted(glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)):
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        txt = open(path, encoding="utf-8", newline="").read()
        if 'action="/contact"' not in txt:
            continue
        kind, fields = classify_contact_form(txt)
        if kind == "none":
            continue
        if kind == "filled":
            skipped.append((rel, fields))
            continue

        orig = txt
        if rel == "index.html":
            i = txt.index(INDEX_START)
            j = txt.index(INDEX_END) + len(INDEX_END)
            txt = txt[:i] + rebuild_index_region() + txt[j:]
        else:
            txt = replace_empty_form(txt)

        if txt != orig:
            open(path, "w", encoding="utf-8", newline="").write(txt)
            changed.append(rel)

    print(f"replaced empty contact form on {len(changed)} page(s):")
    for c in changed:
        print("   ", c)
    if skipped:
        print("left untouched (form has real fields; backend may live outside repo):")
        for rel, f in skipped:
            print(f"    {rel}  ({f} fields)")


if __name__ == "__main__":
    main()
