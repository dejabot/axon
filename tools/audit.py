#!/usr/bin/env python3
"""Pre-push audit for the Axon curriculum.

Runs the mechanical half of REVIEWER_SPEC over docs/ so that a bad page cannot
reach GitHub Pages. The judgement half — is the derivation sound, does the
bridge name a real architecture — still needs a reviewer.

    python3 tools/audit.py              # whole site
    python3 tools/audit.py docs/math/02_trigonometry

Exit code is non-zero if any ERROR is found. WARNs do not fail the build.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')

WORD_MIN, WORD_MAX = 1800, 2800

errors, warnings = [], []


def err(path, msg):
    errors.append(f"ERROR  {os.path.relpath(path, ROOT)}: {msg}")


def warn(path, msg):
    warnings.append(f"WARN   {os.path.relpath(path, ROOT)}: {msg}")


def prose_words(text):
    """Word count of prose only.

    Excludes fenced code, SVG markup, HTML tags — and math. LaTeX source counts
    as many "words" (\\begin{aligned}, \\frac, \\text{...}) while representing a
    single equation the reader takes in at a glance, so leaving it in made every
    concept appear to grow when its display math was typeset.
    """
    t = re.sub(r'```.*?```', '', text, flags=re.S)
    t = re.sub(r'\$\$.*?\$\$', '', t, flags=re.S)
    t = re.sub(r'\$[^$\n]+\$', '', t)
    t = re.sub(r'<svg.*?</svg>', '', t, flags=re.S)
    # Require a letter or slash after '<' so that prose like `C < 90°` is not
    # mistaken for a tag. The naive pattern swallowed everything up to the next
    # '>', silently eating whole sections and under-reporting the count.
    t = re.sub(r'</?[a-zA-Z][^>]*>', '', t)
    return len(t.split())


def check_liquid(path, text):
    """Jekyll renders these pages. Unescaped Liquid in a code block kills the build."""
    for token, name in (('{{', 'Liquid output tag'), ('{%', 'Liquid statement tag')):
        if token in text:
            line = text[:text.index(token)].count('\n') + 1
            err(path, f"contains {token} ({name}) at line {line} — breaks the Jekyll build")


def check_math(path, text):
    """Math is rendered by KaTeX, but only from the delimiters kramdown preserves.

    Verified against a built page: `$...$` passes through verbatim and `$$...$$`
    is rewritten to `\\[...\\]`, so both reach KaTeX. Authored `\\(...\\)` and
    `\\[...\\]` do NOT — kramdown strips the backslash and the math renders as
    bare parentheses. That is the main trap this checks for.
    """
    # Blank out code fences and well-formed math, preserving length and newlines
    # so every offset still maps to the original line number. Anything flagged
    # below is therefore genuinely outside a math region.
    def blank(m):
        return re.sub(r'[^\n]', ' ', m.group(0))

    masked = re.sub(r'```.*?```', blank, text, flags=re.S)
    masked = re.sub(r'\$\$.*?\$\$', blank, masked, flags=re.S)
    masked = re.sub(r'\$[^$\n]+\$', blank, masked)

    def line_at(pos):
        return masked[:pos].count('\n') + 1

    # Authored \( or \[ OUTSIDE math. Inside math these are legitimate LaTeX
    # (\\[4pt] is a line break), which is why masking has to happen first.
    for m in re.finditer(r'(?<!\\)\\[\(\[]', masked):
        err(path, f"authored {m.group(0)!r} at line {line_at(m.start())} — kramdown "
                  f"strips the backslash, so KaTeX never sees it. Use $...$ or $$...$$")

    for m in re.finditer(r'\$', masked):
        err(path, f"unpaired $ at line {line_at(m.start())} — an odd delimiter "
                  f"swallows the rest of the paragraph into a math span")
        break

    # Brace sub/superscripts render only via KaTeX; outside math they are literal.
    for m in re.finditer(r'[A-Za-z0-9)\]]([_^])\{[^}]*\}', masked):
        kind = 'subscript' if m.group(1) == '_' else 'superscript'
        err(path, f"LaTeX {kind} {m.group(0)!r} at line {line_at(m.start())} is "
                  f"outside any math delimiter — wrap it in $...$ or use v[i+1]")


def check_emoji(path, text):
    if re.search(r'[\U0001F300-\U0001FAFF\u26A0\u2705\u274C]', text):
        warn(path, "contains a decorative emoji — REVIEWER_SPEC point 1 forbids them")


def check_numbering(path, text):
    """The title must match the directory's number.

    Renumbering a module moves directories and rewrites nav footers and indexes,
    but the `# Concept NN:` heading inside each file and any prose cross-references
    are invisible to a link checker — every link still resolves. This has gone
    stale twice already, so it is checked rather than remembered.
    """
    d = os.path.basename(os.path.dirname(path))
    m_dir = re.match(r'(\d+)_concept_', d)
    m_title = re.match(r'#\s*Concept\s*(\d+)', text.lstrip())
    if m_dir and m_title and m_dir.group(1).lstrip('0') != m_title.group(1).lstrip('0'):
        err(path, f"title says 'Concept {m_title.group(1)}' but the directory is "
                  f"{m_dir.group(1)} — left behind by a renumber")


def check_concept(path, text):
    # Length follows the topic, so both bounds are advisory. A short concept may be
    # perfectly calibrated (linear interpolation has no theorem in it); a long one may
    # be padded with adjacent material. Only a human can tell which, so never fail here.
    n = prose_words(text)
    if n < WORD_MIN:
        warn(path, f"{n} prose words — check this is a genuinely small topic, not an under-derived one")
    elif n > WORD_MAX:
        warn(path, f"{n} prose words — check this is genuine depth, not padding, and whether it splits")

    if '<iframe' not in text:
        err(path, "no embedded demo iframe")
    if 'Math!' not in text:
        warn(path, "no 'Math!' sidebar — REVIEWER_SPEC point 3 expects at least one")
    if not re.search(r'\+---|\|\s*---|\+--|^\s*[|+][-=]{3,}', text, re.M):
        pass  # ASCII-art heuristic is noisy; left to the human reviewer


def check_demo(path, text):
    """The canvas feedback loop that silently blanked 17 demos in this repo."""
    if 'min-height' in text and 'inset: 0' not in text:
        err(path, "canvas container uses min-height without absolute positioning — "
                  "canvas will grow without bound on resize and render blank")
    if 'height: 100%' in text and 'inset: 0' not in text:
        err(path, "canvas is height:100% without absolute positioning — same resize bug")
    if 'assets/theme.js' not in text:
        err(path, "does not load the shared theme.js")
    if 'axon-theme-changed' not in text:
        warn(path, "never repaints on the axon-theme-changed event")
    for m in re.finditer(r'(?:src|href)="(https?://[^"]+)"', text):
        err(path, f"external resource {m.group(1)} — demos must be self-contained")


def check_links(path, text):
    d = os.path.dirname(path)
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)|(?:href|src)="([^"]+)"', text):
        link = m.group(1) or m.group(2)
        if not link or link.startswith(('http', '#', 'mailto:', 'data:')):
            continue
        if '{' in link:          # Liquid-templated, resolved at build time
            continue
        target = os.path.normpath(os.path.join(d, link.split('#')[0]))
        if not os.path.exists(target):
            err(path, f"broken link -> {link}")


def main():
    roots = sys.argv[1:] or [DOCS]
    for root in roots:
        root = os.path.abspath(root)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ('.git', '_site', '_layouts')]
            for fn in filenames:
                if not fn.endswith(('.md', '.html')):
                    continue
                path = os.path.join(dirpath, fn)
                text = open(path, encoding='utf-8').read()

                check_liquid(path, text)
                check_links(path, text)

                if fn == 'README.md':
                    check_math(path, text)
                    check_emoji(path, text)
                    if '_concept_' in dirpath:
                        check_concept(path, text)
                        check_numbering(path, text)
                elif fn == 'demo.html':
                    check_demo(path, text)

    for line in warnings:
        print(line)
    for line in errors:
        print(line)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
