#!/usr/bin/env python3
"""Render doctrine/doctrine-v1.md into site/doctrine.html (lightweight markdown)."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "doctrine" / "doctrine-v1.md"
DST = ROOT / "site" / "doctrine.html"


def md_to_html(md: str) -> str:
    out: list[str] = []
    in_list: str | None = None
    ol_re = re.compile(r"^\s*\d+\.\s*")
    for line in md.splitlines():
        if line.startswith("# "):
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("### "):
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif re.match(r"^\s*[-*] ", line):
            if in_list != "ul":
                if in_list:
                    out.append(f"</{in_list}>")
                out.append("<ul>")
                in_list = "ul"
            out.append(f"<li>{html.escape(line.strip()[2:])}</li>")
        elif ol_re.match(line):
            if in_list != "ol":
                if in_list:
                    out.append(f"</{in_list}>")
                out.append("<ol>")
                in_list = "ol"
            stripped = ol_re.sub("", line)
            out.append(f"<li>{html.escape(stripped)}</li>")
        elif line.strip() == "---":
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append("<hr/>")
        elif line.strip() == "":
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append("")
        else:
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append(f"<p>{html.escape(line)}</p>")
    if in_list:
        out.append(f"</{in_list}>")
    return "\n".join(out)


def main() -> None:
    body = md_to_html(SRC.read_text())
    page = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>\n'
        '<title>Doctrine v1 — The Stewardship</title>\n'
        '<link rel="stylesheet" href="style.css"/>\n'
        "</head>\n<body>\n<main>\n"
        + body
        + '\n<p style="margin-top:48px"><a href="index.html">← back</a></p>\n'
        "</main>\n</body>\n</html>\n"
    )
    DST.write_text(page)
    print(f"Wrote {DST}")


if __name__ == "__main__":
    main()
