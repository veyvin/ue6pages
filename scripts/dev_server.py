#!/usr/bin/env python3
"""Local preview server for the Jekyll docs tree (no Ruby required)."""
from __future__ import annotations

import argparse
import re
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LAYOUT = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
SITE_TITLE = "Unreal Engine 插件与模块文档"


def render_markdown(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    title = SITE_TITLE
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            front, body = parts[1], parts[2]
            match = re.search(r"^title:\s*(.+)$", front, re.M)
            if match:
                title = match.group(1).strip()
    html = LAYOUT
    html = html.replace("{{ content }}", body)
    html = re.sub(r"\{\{\s*page\.title \| default: site\.title\s*\}\}", title, html)
    html = re.sub(r"\{\{\s*'/' \| relative_url\s*\}\}", "/", html)
    html = re.sub(r"\{\{\s*'/assets/style.css' \| relative_url\s*\}\}", "/assets/style.css", html)
    html = re.sub(r"\{\{\s*'/assets/main.js' \| relative_url\s*\}\}", "/assets/main.js", html)
    return html.encode("utf-8")


def resolve_page(url_path: str) -> Path | None:
    path = unquote(url_path)
    if path in ("/", "/index.html", "/index.md"):
        return ROOT / "index.md"
    if path.endswith("/"):
        candidate = ROOT / path.strip("/") / "index.md"
        if candidate.is_file():
            return candidate
    raw = path.lstrip("/")
    if raw.endswith(".html"):
        raw = raw[:-5] + ".md"
    elif not raw.endswith(".md"):
        raw = raw + ".md"
    candidate = ROOT / raw
    if candidate.is_file():
        return candidate
    return None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        page = resolve_page(parsed.path)
        if page is not None:
            data = render_markdown(page)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
            return
        return super().do_GET()

    def log_message(self, fmt: str, *args) -> None:
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4000)
    args = parser.parse_args()
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving {ROOT} at http://{args.host}:{args.port}/")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
