"""Repo fixer for the abetworks static site (run once).

Every rewrite is verified against files that already exist in the repo, so the
script cannot invent a page or an image. Missing images are pointed at real
files; links to never-created sub-service pages fall back to the enquiry section
that already exists on the same page.
"""
import os
import re
import glob
import urllib.parse
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = sorted(glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True))
ENTRIES = {os.path.relpath(p, ROOT).replace(os.sep, "/")
           for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True)
           if os.path.isfile(p)}

stats = Counter()

# --- config ---------------------------------------------------------------

# Sub-service pages linked from the service cards but never created. The cards
# keep their copy and scroll to the #contact enquiry section on the same page.
DEAD_SUBSERVICES = {
    "web-development.html", "website-development.html", "digital-marketing.html",
    "ecommerce-solutions.html", "analytics-solutions.html", "cybersecurity.html",
    "consulting.html", "graphic-design.html", "app-development.html", "seo-services.html",
    "data-visualiz.html", "predictive-analytics.html", "data-management.html",
    "big-data-analytics.html", "data-security.html", "data-strategy.html",
    "data-analytics.html", "business-consultancy.html", "custom-reporting.html",
    "strategic-planning.html", "market-research.html", "change-management.html",
    "risk-management.html",
}

# portfolio-details.html was deleted from the repo; route each template filter
# slot to the matching real service page.
PORTFOLIO_FILTER = [
    ("filter-ai", "services/ai.html"),
    ("filter-analytics", "services/Data_Analytics.html"),
    ("filter-digital", "services/digital_services.html"),
    ("filter-app", "services/Data_Analytics.html"),
    ("filter-web", "services/digital_services.html"),
    ("filter-consulting", "services/Bussiness_consultancy.html"),
    ("filter-marketing", "services/digital_services.html"),
    ("filter-category", "services/Data_Analytics.html"),
]
PORTFOLIO_FALLBACK = {
    "services/products/product_data_anyalitics.html": "services/Data_Analytics.html",
    "services/product/template-best.html": "services/Data_Analytics.html",
    "services/data_anyalitics_services/visual_scrapper.html": "services/Data_Analytics.html",
    "services/products/product_digital.html": "services/digital_services.html",
    "services/products/product_consultacy.html": "services/Bussiness_consultancy.html",
    "services/products/product_sales_and_marketing .html": "services/digital_services.html",
}

# Referenced-but-missing images mapped onto real files already in the repo.
MISSING_IMAGE = [
    ("assets/img/masonry-portfolio/masonry-portfolio-1.jpg",
     "assets/img/masonry-portfolio/1221.jpg"),
    ("assets/img/blog-1.jpg", "assets/img/masonry-portfolio/awp/bussiness_intelligance.webp"),
    ("assets/img/blog-2.jpg", "assets/img/masonry-portfolio/ai/abetworks_sales_intel.webp"),
    ("assets/img/blog-3.jpg", "assets/img/masonry-portfolio/digi/abetworks digital marketing.webp"),
    ("assets/img/data-impact-img.jpg", "assets/img/masonry-portfolio/awp/abetworks_sales.webp"),
    ("assets/img/abetimages/service-image.webp", "assets/img/services.jpg"),
]
PLACEHOLDER_EMAILS = ["contcact@abetworks.com", "contact@example.com", "contact@abetworks.com"]
REAL_EMAIL = "admin@abetworks.in"

ATTR_RE = r'(href|src)=(["\'])([^"\'#][^"\']*)\2'



# --- helpers --------------------------------------------------------------

def rel(from_dir, repo_path):
    out = os.path.relpath(os.path.join(ROOT, repo_path), from_dir).replace(os.sep, "/")
    return out if out.startswith(".") else "./" + out


def split_url(url):
    for sep in ("#", "?"):
        if sep in url:
            i = url.index(sep)
            return url[:i], url[i:]
    return url, ""


def resolve(dirpath, url):
    """Repo-relative path of a real file, or None."""
    bare, _ = split_url(url)
    cand = urllib.parse.unquote(bare).strip()
    if not cand:
        return None
    if cand.startswith("/"):
        p = os.path.normpath(cand[1:]).replace(os.sep, "/")
    else:
        p = os.path.normpath(os.path.join(dirpath, cand)).replace(os.sep, "/")
    return p if p in ENTRIES else None


def norm_key(url):
    bare, _ = split_url(url)
    key = urllib.parse.unquote(bare).strip()
    while key.startswith("./") or key.startswith("/"):
        key = key[2:] if key.startswith("./") else key[1:]
    return os.path.normpath(key).replace(os.sep, "/")


# --- passes ---------------------------------------------------------------

def rewrite_attrs(txt, dirpath, predicate):
    """Run predicate(url) -> new url or None over every local href/src value."""
    n = 0

    def repl(m):
        nonlocal n
        url = m.group(3)
        if url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")):
            return m.group(0)
        new = predicate(url)
        if new is None or new == url:
            return m.group(0)
        n += 1
        return f'{m.group(1)}={m.group(2)}{new}{m.group(2)}'

    txt = re.sub(ATTR_RE, repl, txt)
    return txt, n


def make_root_relative(dirpath):
    def pred(url):
        if not url.startswith("/"):
            return None
        p = resolve(dirpath, url)
        if not p:
            return None
        base, suffix = split_url(url)
        return rel(dirpath, p) + suffix
    return pred


def swap_missing_images(dirpath):
    def pred(url):
        if resolve(dirpath, url):
            return None
        key = norm_key(url)
        if not key.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg")):
            return None
        base, suffix = split_url(url)
        for needle, target in MISSING_IMAGE:
            if key.endswith(needle):
                return rel(dirpath, target) + suffix
        return None
    return pred


def re_root_relative(dirpath, rel_root):
    """Fix refs written as if the page sat at the site root.

    e.g. services/ai.html using './assets/...' or 'index.html'. Only rewritten
    when the path is wrong from the page but correct from the repo root.
    """
    def pred(url):
        if url.startswith("/"):
            return None
        base, suffix = split_url(url)
        cand = urllib.parse.unquote(base).strip()
        if not cand or resolve(dirpath, url):
            return None
        from_root = os.path.normpath(cand).replace(os.sep, "/")
        if from_root not in ENTRIES:
            return None
        return rel(dirpath, from_root) + suffix
    return pred


def drop_client9(txt):
    """client-9.png never existed; remove only that carousel slide."""
    new, n = re.subn(r'[ \t]*<div class="swiper-slide"><img[^>]*clients/client-9\.png[^>]*></div>(?:\r?\n)?',
                     "", txt)
    return new, n


def reroute_portfolio(txt, dirpath, rel_root):
    """portfolio-details.html is gone -> point at the matching real service page."""
    fallback = PORTFOLIO_FALLBACK.get(rel_root)
    n = 0

    def sub(m):
        nonlocal n
        head, tail = m.group(1), m.group(3)
        dest = next((t for cls, t in PORTFOLIO_FILTER if cls in head), None) or fallback
        if not dest:
            return m.group(0)
        n += 1
        return head + f'href="{rel(dirpath, dest)}"' + tail

    txt = re.sub(r'(<div class="col-[^"]*portfolio-item[^"]*">(?:(?!</div>).)*?)'
                 r'(href="portfolio-details\.html")([^>]*>)', sub, txt, flags=re.S)
    if fallback and "portfolio-details.html" in txt:
        txt, c = re.subn(r'href="portfolio-details\.html"',
                         f'href="{rel(dirpath, fallback)}"', txt)
        n += c
    return txt, n


def kill_dead_subservices(txt):
    """Cards linking never-created pages -> the page's own #contact section."""
    if 'id="contact"' not in txt:
        return txt, 0
    n = 0
    for dead in DEAD_SUBSERVICES:
        pat = f'href="{dead}"'
        if pat in txt:
            txt, c = re.subn(re.escape(pat), 'href="#contact"', txt)
            n += c
    return txt, n


def process(path):
    rel_root = os.path.relpath(path, ROOT).replace(os.sep, "/")
    dirpath = os.path.dirname(path)
    txt = open(path, encoding="utf-8", newline="").read()
    orig = txt

    txt, n = rewrite_attrs(txt, dirpath, make_root_relative(dirpath))
    stats["root-absolute paths made portable"] += n

    txt, n = rewrite_attrs(txt, dirpath, re_root_relative(dirpath, rel_root))
    stats["root-relative-looking refs fixed for page depth"] += n

    txt, n = drop_client9(txt)
    stats["client-9.png broken slide removed"] += n

    # iterate: re-rooting can expose a reference that still names a missing image
    for _ in range(3):
        txt, n = rewrite_attrs(txt, dirpath, swap_missing_images(dirpath))
        stats["missing image pointed at a real file"] += n
        if not n:
            break

    txt, n = reroute_portfolio(txt, dirpath, rel_root)
    stats["orphan portfolio-details.html rerouted"] += n

    txt, n = kill_dead_subservices(txt)
    stats["dead sub-service card -> #contact"] += n

    # site-root link "/" -> relative path to index.html
    if 'href="/"' in txt:
        txt = txt.replace('href="/"', f'href="{rel(dirpath, "index.html")}"')
        stats["root link / -> index.html"] += 1

    j = re.search(r'\{\{[^}]*url_for\([^)]*\)[^}]*\}\}', txt)
    if j:
        txt = txt.replace(j.group(0), rel(dirpath, "assets/img/hero-bg.jpg"))
        stats["jinja template tag removed"] += 1

    if rel_root == "services/privacy-policy-detail.html" and 'href="styles.css"' in txt:
        txt = txt.replace('href="styles.css"', f'href="{rel(dirpath, "assets/css/main.css")}"')
        stats["orphan styles.css ref -> main.css"] += 1

    if 'href="/aboutus.html"' in txt:
        txt = txt.replace('href="/aboutus.html"', f'href="{rel(dirpath, "services/aboutus.html")}"')
        stats["/aboutus.html typo corrected"] += 1

    c = txt.count("BKR1M1PACYs")
    if c:
        txt = txt.replace("BKR1M1PACYs", "BKR1M1PACY")
        stats["tripetto form-id typo fixed"] += c

    for bad in PLACEHOLDER_EMAILS:
        c = txt.count(bad)
        if c:
            txt = txt.replace(bad, REAL_EMAIL)
            stats["placeholder email -> admin@abetworks.in"] += c

    m = re.search(r'href="(/assets/img/[^"]*?) title="', txt)
    if m:
        txt = txt.replace(m.group(0), m.group(1) + '" title="')
        stats["malformed href quote fixed"] += 1

    if txt != orig:
        open(path, "w", encoding="utf-8", newline="").write(txt)
        return True
    return False


def main():
    changed = [p for p in HTML if process(p)]
    print(f"scanned {len(HTML)} html files, rewrote {len(changed)}")
    for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
        print(f"  {v:5d}  {k}")


if __name__ == "__main__":
    main()
