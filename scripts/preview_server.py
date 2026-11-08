#!/usr/bin/env python3
"""Minimal Jekyll-like preview so gh-pages markdown renders locally."""
from __future__ import annotations

import re
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYOUT = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
PORT = 8080

LIQUID = [
    (re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}"), r"\1"),
    (re.compile(r'\{\{\s*"/([^"]*)"\s*\|\s*relative_url\s*\}\}'), r"/\1"),
]


def render_md(path: Path) -> str | None:
    raw = path.read_text(encoding="utf-8")
    title = path.stem
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[4:end]
            m = re.search(r"^title:\s*(.+)$", fm, re.M)
            if m:
                title = m.group(1).strip()
            body = raw[end + 4 :].lstrip("\n")
    html = LAYOUT.replace("{{ content }}", body)
    html = html.replace("{{ page.title | default: site.title }}", title)
    html = html.replace("{{ page.title }}", title)
    for pat, repl in LIQUID:
        html = pat.sub(repl, html)
    html = re.sub(r"\{\{[^}]+\}\}", "", html)
    return html


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html", "/index.md"):
            md = ROOT / "index.md"
        elif path.endswith(".html"):
            rel = path.lstrip("/")
            md = ROOT / rel.replace(".html", ".md")
        elif path.endswith(".md"):
            md = ROOT / path.lstrip("/")
        else:
            return super().do_GET()
        if md.is_file():
            data = render_md(md).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        return super().do_GET()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Preview: http://127.0.0.1:{PORT}/")
    print(f"Niagara: http://127.0.0.1:{PORT}/plugins/niagara.html")
    httpd.serve_forever()
