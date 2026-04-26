#!/usr/bin/env python3
"""Merge multiple Markdown files into a single PDF via weasyprint.

Usage:
    python3 md_to_pdf.py -o output.pdf --title "Title" file1.md [file2.md ...]
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

import markdown
from weasyprint import HTML, CSS


EMOJI_MAP = {
    "🥇": '<span class="medal gold">#1</span>',
    "🥈": '<span class="medal silver">#2</span>',
    "🥉": '<span class="medal bronze">#3</span>',
    "🏅": '<span class="medal bronze">#3</span>',
    "🟢": '<span class="dot green">●</span>',
    "🟡": '<span class="dot yellow">●</span>',
    "🔴": '<span class="dot red">●</span>',
    "⭐": "★",
    "✅": '<span class="check ok">✓</span>',
    "❌": '<span class="check no">✗</span>',
    "⚠️": '<span class="warn">!</span>',
    "⚠": '<span class="warn">!</span>',
    "🚀": '<span class="up">↑↑</span>',
    "⬇️": '<span class="down">↓</span>',
    "⬇": '<span class="down">↓</span>',
    "🆕": '<span class="tag">新</span>',
    "🔍": "🔎",
    "⚡": '<span class="bolt">⚡</span>',
    "🎯": '<span class="target">◎</span>',
    "📌": '<span class="pin">▎</span>',
    "📍": '<span class="pin">▎</span>',
    "🚩": '<span class="flag">!</span>',
    "🟠": '<span class="dot orange">●</span>',
    "📊": '<span class="chart">▦</span>',
    "📈": '<span class="chart">↗</span>',
    "📉": '<span class="chart">↘</span>',
    "🔔": '<span class="bell">⌬</span>',
    "💡": '<span class="idea">✦</span>',
    "🏆": '<span class="trophy">♛</span>',
    "📞": '<span class="phone">☎</span>',
    "🇯🇵": '<span class="flag-jp">(JP)</span>',
    "✨": '<span class="sparkle">✦</span>',
    "👉": '→',
    "✓": '<span class="check ok">✓</span>',
    "✗": '<span class="check no">✗</span>',
}
EMOJI_RE = re.compile("|".join(re.escape(k) for k in EMOJI_MAP))


def replace_emojis(html: str) -> str:
    return EMOJI_RE.sub(lambda m: EMOJI_MAP[m.group(0)], html)


CSS_STYLE = """
@page {
    size: A4;
    margin: 20mm 15mm;
    @bottom-center {
        content: counter(page) " / " counter(pages);
        font-family: "Noto Sans CJK TC", sans-serif;
        font-size: 9pt;
        color: #666;
    }
}
@page :first { @bottom-center { content: ""; } }

body {
    font-family: "Noto Sans CJK TC", "Noto Sans", sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #222;
}
h1 { font-size: 20pt; color: #1a3d7c; border-bottom: 2px solid #1a3d7c; padding-bottom: 4pt; margin-top: 18pt; page-break-before: auto; }
h2 { font-size: 15pt; color: #2a5aa0; margin-top: 14pt; border-left: 4px solid #2a5aa0; padding-left: 8pt; }
h3 { font-size: 12pt; color: #333; margin-top: 10pt; }
h4 { font-size: 11pt; color: #444; }

.section-break h1 { page-break-before: always; }

p { margin: 6pt 0; }
strong { color: #1a3d7c; }
code { background: #f2f4f7; padding: 1pt 4pt; border-radius: 3pt; font-size: 9pt; font-family: "DejaVu Sans Mono", monospace; }
pre { background: #f2f4f7; border: 1px solid #d9dde4; border-radius: 4pt; padding: 6pt 10pt; font-size: 8.5pt; overflow-x: auto; page-break-inside: avoid; }
pre code { background: transparent; padding: 0; }
blockquote { border-left: 3px solid #a0b5d5; background: #f7f9fc; margin: 8pt 0; padding: 4pt 10pt; color: #445; }

table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 7.5pt; page-break-inside: avoid; table-layout: auto; }
th { background: #1a3d7c; color: #fff; padding: 3pt 4pt; text-align: left; border: 1px solid #1a3d7c; word-break: keep-all; overflow-wrap: break-word; }
td { padding: 2.5pt 4pt; border: 1px solid #d0d5dd; vertical-align: top; word-break: break-word; overflow-wrap: anywhere; line-height: 1.4; }
tr:nth-child(even) td { background: #f7f9fc; }

/* Emoji -> text markers */
.medal { display: inline-block; min-width: 18pt; padding: 1pt 4pt; border-radius: 8pt; font-weight: bold; font-size: 8pt; color: #fff; text-align: center; }
.medal.gold { background: #d4a017; }
.medal.silver { background: #8a8d93; }
.medal.bronze { background: #a87139; }
.dot { font-size: 10pt; vertical-align: middle; }
.dot.green { color: #2da44e; }
.dot.yellow { color: #d4a017; }
.dot.red { color: #c3343e; }
.check.ok { color: #2da44e; font-weight: bold; }
.check.no { color: #c3343e; font-weight: bold; }
.warn { display: inline-block; background: #f4b740; color: #fff; font-weight: bold; padding: 0 4pt; border-radius: 3pt; font-size: 8pt; }
.up { color: #2da44e; font-weight: bold; }
.down { color: #c3343e; font-weight: bold; }
.tag { display: inline-block; background: #2a5aa0; color: #fff; padding: 0 4pt; border-radius: 3pt; font-size: 8pt; }
.bolt { color: #d4a017; }

ul, ol { margin: 6pt 0; padding-left: 20pt; }
li { margin: 2pt 0; }

img { max-width: 100%; height: auto; display: block; margin: 10pt auto; page-break-inside: avoid; }
svg { max-width: 100%; height: auto; display: block; margin: 10pt auto; page-break-inside: avoid; break-inside: avoid; }
figure { page-break-inside: avoid; margin: 10pt 0; text-align: center; }
figcaption { font-size: 9pt; color: #666; font-style: italic; margin-top: 3pt; text-align: center; }
p > em:only-child { display: block; text-align: center; font-size: 9pt; color: #666; margin-top: -6pt; }

a { color: #2a5aa0; text-decoration: none; }

.cover { text-align: center; padding-top: 80mm; page-break-after: always; }
.cover h1 { font-size: 28pt; border: none; color: #1a3d7c; margin-bottom: 20pt; }
.cover .subtitle { font-size: 14pt; color: #555; margin-bottom: 40pt; }
.cover .meta { font-size: 11pt; color: #777; margin-top: 60pt; }

.toc { page-break-after: always; }
.toc h2 { border: none; color: #1a3d7c; padding: 0; }
.toc ol { list-style: none; padding-left: 0; }
.toc li { padding: 4pt 0; border-bottom: 1px dashed #ddd; font-size: 11pt; }
"""

MD_EXTENSIONS = [
    "extra",
    "tables",
    "fenced_code",
    "toc",
    "sane_lists",
    "nl2br",
]


def build_cover(title: str, subtitle: str, author: str) -> str:
    today = date.today().strftime("%Y-%m-%d")
    return f"""
    <div class="cover">
        <h1>{title}</h1>
        <div class="subtitle">{subtitle}</div>
        <div class="meta">
            報告日期：{today}<br>
            撰寫方：{author}
        </div>
    </div>
    """


def build_toc(files_meta: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'<li>{i+1}. <strong>{title}</strong><br><span style="color:#888;font-size:9pt">{desc}</span></li>'
        for i, (title, desc) in enumerate(files_meta)
    )
    return f'<div class="toc"><h2>目錄</h2><ol>{items}</ol></div>'


SVG_BLOCK_RE = re.compile(r"<svg\b[\s\S]*?</svg>", re.IGNORECASE)


def convert_md(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    # Extract SVG blocks BEFORE markdown so nl2br doesn't inject <br> inside them,
    # then re-insert after. Also strip any <p>...</p> wrapper markdown may add.
    svgs: list[str] = []

    def _stash(m: re.Match) -> str:
        svgs.append(m.group(0))
        return f"\n\n@@SVG_PLACEHOLDER_{len(svgs) - 1}@@\n\n"

    stashed = SVG_BLOCK_RE.sub(_stash, text)
    html = markdown.markdown(stashed, extensions=MD_EXTENSIONS, output_format="html5")
    for i, svg in enumerate(svgs):
        token = f"@@SVG_PLACEHOLDER_{i}@@"
        html = html.replace(f"<p>{token}</p>", svg).replace(token, svg)
    return replace_emojis(html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="Markdown files to merge, in order")
    ap.add_argument("-o", "--output", required=True, help="Output PDF path")
    ap.add_argument("--title", default="研究報告", help="Cover title")
    ap.add_argument("--subtitle", default="", help="Cover subtitle")
    ap.add_argument("--author", default="hv-research", help="Author / team")
    ap.add_argument("--section-titles", nargs="*", default=None,
                    help="Per-file section titles for TOC (same count as files)")
    ap.add_argument("--section-descs", nargs="*", default=None,
                    help="Per-file short descriptions for TOC")
    ap.add_argument("--landscape", action="store_true",
                    help="Use A3 landscape page (for wide tables)")
    ap.add_argument("--no-cover", action="store_true",
                    help="Skip cover and TOC (useful for single-file companion PDFs)")
    args = ap.parse_args()

    paths = [Path(p).resolve() for p in args.files]
    missing = [p for p in paths if not p.exists()]
    if missing:
        print(f"ERROR: files not found: {missing}", file=sys.stderr)
        return 2

    titles = args.section_titles or [p.stem for p in paths]
    descs = args.section_descs or ["" for _ in paths]
    if len(titles) != len(paths) or len(descs) != len(paths):
        print("ERROR: --section-titles / --section-descs count mismatch", file=sys.stderr)
        return 2

    parts = []
    if not args.no_cover:
        parts.append(replace_emojis(build_cover(args.title, args.subtitle, args.author)))
        parts.append(replace_emojis(build_toc(list(zip(titles, descs)))))

    for i, path in enumerate(paths):
        break_class = "section-break" if i > 0 and not args.no_cover else ""
        parts.append(f'<div class="{break_class}">{convert_md(path)}</div>')

    html_body = "\n".join(parts)
    full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"

    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    page_css = CSS_STYLE
    if args.landscape:
        page_css = page_css.replace("size: A4;", "size: A3 landscape;").replace(
            "font-size: 7.5pt;", "font-size: 8.5pt;"
        )

    HTML(string=full_html, base_url=str(paths[0].parent)).write_pdf(
        str(out), stylesheets=[CSS(string=page_css)]
    )
    print(f"OK: wrote {out}  ({out.stat().st_size/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
