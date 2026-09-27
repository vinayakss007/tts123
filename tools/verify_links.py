"""Verify the static site: no local href/src points at a missing file."""
import os
import re
import sys
import glob
import urllib.parse
from collections import defaultdict

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
HTML = sorted(glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True))
FILES = {os.path.relpath(p, ROOT).replace(os.sep, "/")
         for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True) if os.path.isfile(p)}
FRAGS = defaultdict(set)

for p in FILES:
    if not p.endswith(".html"):
        continue
    txt = open(os.path.join(ROOT, p), encoding="utf-8", errors="ignore").read()
    FRAGS[p] = set(re.findall(r'\bid="([^"]+)"', txt))

EXTERNAL_BLOG = re.compile(r'^https://abetworks\.in/blogs')
SKIP_PREFIX = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")
broken = defaultdict(list)
bad_frag = defaultdict(list)
checked = 0

for path in HTML:
    rel_path = os.path.relpath(path, ROOT).replace(os.sep, "/")
    dirpath = os.path.dirname(path)
    txt = open(path, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r'(?:href|src)=(["\'])([^"\']+)\1', txt):
        url = m.group(2)
        if url.startswith(SKIP_PREFIX):
            continue
        if "{{" in url or "{%" in url:
            broken[rel_path].append(("TEMPLATE-LEFTOVER", url))
            continue
        bare, _, frag = url.partition("#")
        bare = bare.split("?")[0]
        checked += 1
        if not bare:
            continue
        cand = urllib.parse.unquote(bare).strip()
        if cand.startswith("/"):
            broken[rel_path].append(("ROOT-ABSOLUTE", url))
            continue
        p = os.path.normpath(os.path.join(dirpath, cand)).replace(os.sep, "/")
        p = os.path.relpath(p, ROOT).replace(os.sep, "/")
        if p not in FILES:
            broken[rel_path].append(("MISSING", url))
        elif frag and p in FRAGS and frag and frag not in FRAGS[p] and p.endswith(".html"):
            bad_frag[rel_path].append(url)

print(f"files scanned: {len(HTML)}   local refs checked: {checked}")

# Attributes whose value swallows markup because a quote is missing, e.g.
# href="foo.png title="Bar" -> the browser eats the title attribute.
unterminated = defaultdict(list)
for path in HTML:
    rel_path = os.path.relpath(path, ROOT).replace(os.sep, "/")
    txt = open(path, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r'(?:href|src|alt|title)=(["\'])[^"\'>]*>', txt):
        unterminated[rel_path].append(m.group(0))

total = sum(len(v) for v in broken.values())
print(f"BROKEN local refs: {total}")
for f in sorted(broken):
    for kind, u in broken[f][:8]:
        print(f"  [{kind}] {f} -> {u}")
    if len(broken[f]) > 8:
        print(f"     ... +{len(broken[f]) - 8} more in {f}")
tf = sum(len(v) for v in bad_frag.values())
tu = sum(len(v) for v in unterminated.values())
print(f"attributes swallowing markup (missing quote): {tu}")
for f in sorted(unterminated):
    for u in unterminated[f][:5]:
        print(f"  {f} -> {u[:90]}")

print(f"\nlinks to a missing #fragment on an existing page: {tf}")
for f in sorted(bad_frag):
    for u in bad_frag[f][:6]:
        print(f"  {f} -> {u}")
