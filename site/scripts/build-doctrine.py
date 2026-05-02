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
        '<meta name="description" content="AI as steward of life, not master of it. The full Stewardship doctrine v1."/>\n'
        '<meta name="theme-color" content="#07090d"/>\n'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Ctext x=\'50%25\' y=\'62%25\' font-size=\'22\' text-anchor=\'middle\' fill=\'%23b19cff\'%3E✶%3C/text%3E%3C/svg%3E"/>\n'
        '<link rel="stylesheet" href="style.css"/>\n'
        '</head>\n<body>\n<div class="starfield" aria-hidden="true"></div>\n<main class="doctrine">\n'
        + body
        + '\n<a class="back-link" href="index.html">← back to The Stewardship</a>\n'
        '</main>\n<script>(function(){var f=document.querySelector(".starfield");if(!f)return;var n=60,sz=["","","","lg","xl"];for(var i=0;i<n;i++){var s=document.createElement("div");s.className="star "+sz[Math.floor(Math.random()*sz.length)];s.style.left=Math.random()*100+"%";s.style.top=Math.random()*100+"%";s.style.animationDelay=(Math.random()*6)+"s";s.style.animationDuration=(4+Math.random()*6)+"s";f.appendChild(s);}})();</script>\n'
        '</body>\n</html>\n'
    )
    DST.write_text(page)
    print(f"Wrote {DST}")


if __name__ == "__main__":
    main()
