#!/usr/bin/env python3
"""Build the static GitHub Pages site from dsh-book.md.

The site is intentionally one self-contained HTML file:
- no JavaScript
- no cookies or analytics
- no external fonts, styles, images, or CDNs
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "dsh-book.md"
OUTPUT = ROOT / "docs" / "index.html"
REPO_URL = "https://github.com/leether/dsh-book"
SITE_URL = "https://leether.github.io/dsh-book/"

TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>DeepSeek Harness 入门 · 从第一次对话到自己的插件</title>
<meta name="description" content="给 0 基础用户的 DeepSeek Harness 使用指南：模型、工作区、权限、会话、工具、技能、Preset、插件与创造模式。">
<meta property="og:title" content="DeepSeek Harness 入门">
<meta property="og:description" content="给 0 基础用户的 DeepSeek Harness 使用指南。">
<meta property="og:type" content="website">
<meta property="og:url" content="{site_url}">
<meta name="twitter:card" content="summary">
<style>
:root {
  --bg: #fbfaf7;
  --paper: #ffffff;
  --ink: #1f2328;
  --muted: #667085;
  --line: #e5e1d8;
  --accent: #b45309;
  --accent-soft: #fff4e5;
  --code: #f4f1ea;
  --max: 920px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #151515;
    --paper: #1d1d1f;
    --ink: #ececec;
    --muted: #a3a3a3;
    --line: #333333;
    --accent: #f0a35e;
    --accent-soft: #2b2118;
    --code: #262626;
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Noto Sans SC", "Microsoft YaHei", sans-serif;
  font-size: 17px;
  line-height: 1.8;
  text-rendering: optimizeLegibility;
}
a { color: var(--accent); text-underline-offset: 3px; }
a:hover { text-decoration-thickness: 2px; }
.hero {
  max-width: var(--max);
  margin: 0 auto;
  padding: 72px 24px 32px;
  border-bottom: 1px solid var(--line);
}
.badge {
  display: inline-block;
  margin: 0 0 14px;
  padding: 4px 10px;
  border: 1px solid var(--line);
  border-radius: 999px;
  color: var(--muted);
  font-size: 13px;
  letter-spacing: .04em;
}
.hero h1 {
  margin: 0;
  font-size: clamp(34px, 6vw, 56px);
  line-height: 1.15;
  letter-spacing: -0.02em;
}
.subtitle {
  margin: 12px 0 0;
  color: var(--muted);
  font-size: clamp(18px, 2.4vw, 24px);
}
.meta {
  margin: 18px 0 0;
  color: var(--muted);
  font-size: 14px;
}
.links { margin: 18px 0 0; font-size: 15px; }
.links a { margin-right: 16px; }
main {
  max-width: var(--max);
  margin: 0 auto;
  padding: 8px 24px 64px;
}
.toc {
  margin: 36px 0 8px;
  padding: 22px 24px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 14px;
}
.toc h2 { margin: 0 0 12px; font-size: 18px; }
.toc ol {
  margin: 0;
  padding-left: 1.3em;
  columns: 2;
  column-gap: 36px;
}
.toc li { break-inside: avoid; margin: 4px 0; }
.book { padding-top: 12px; }
.book h1 {
  margin: 3.4rem 0 1rem;
  padding-top: 1.6rem;
  border-top: 1px solid var(--line);
  font-size: clamp(26px, 4vw, 34px);
  line-height: 1.3;
  scroll-margin-top: 24px;
}
.book h1:first-child { border-top: 0; padding-top: 0; margin-top: 1.4rem; }
.book h2 {
  margin: 2.2rem 0 .8rem;
  font-size: clamp(21px, 3vw, 25px);
  line-height: 1.35;
  scroll-margin-top: 24px;
}
.book h3 { margin: 1.7rem 0 .6rem; font-size: 19px; }
.book p { margin: .8rem 0; }
.book ul, .book ol { padding-left: 1.6em; }
.book li { margin: .35rem 0; }
.book blockquote {
  margin: 1.2rem 0;
  padding: 10px 16px;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 8px 8px 0;
}
.book blockquote p { margin: .3rem 0; }
.book code {
  padding: .15em .35em;
  border-radius: 5px;
  background: var(--code);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  font-size: .9em;
}
.book pre {
  margin: 1.1rem 0;
  padding: 16px;
  overflow-x: auto;
  background: var(--code);
  border: 1px solid var(--line);
  border-radius: 10px;
  line-height: 1.55;
}
.book pre code { padding: 0; background: transparent; font-size: 14px; }
.book table {
  display: block;
  width: 100%;
  margin: 1.2rem 0;
  overflow-x: auto;
  border-collapse: collapse;
  font-size: 15px;
}
.book th, .book td {
  padding: 8px 10px;
  border: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}
.book th { background: var(--code); white-space: nowrap; }
.book hr { margin: 2.6rem 0; border: 0; border-top: 1px solid var(--line); }
.book img { max-width: 100%; height: auto; }
.top-link {
  position: fixed;
  right: 18px;
  bottom: 18px;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper);
  color: var(--ink);
  text-decoration: none;
  font-size: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,.08);
}
footer {
  max-width: var(--max);
  margin: 0 auto;
  padding: 28px 24px 56px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 14px;
}
footer p { margin: .35rem 0; }
@media (max-width: 680px) {
  body { font-size: 16px; }
  .hero { padding-top: 48px; }
  .toc ol { columns: 1; }
  main { padding-left: 18px; padding-right: 18px; }
  .book table { font-size: 14px; }
  .top-link { right: 12px; bottom: 12px; }
}
@media print {
  :root { --bg: #fff; --paper: #fff; --ink: #000; --muted: #444; --line: #ccc; --code: #f2f2f2; }
  body { font-size: 11pt; }
  .hero { padding-top: 0; }
  .toc, .top-link { display: none; }
  .book h1 { break-before: page; }
  .book h1:first-child { break-before: auto; }
  a { color: #000; text-decoration: none; }
}
</style>
</head>
<body id="top">
<header class="hero">
  <p class="badge">非官方指南 · 无 Cookie · 无统计</p>
  <h1>DeepSeek Harness 入门</h1>
  <p class="subtitle">从第一次对话到自己的插件</p>
  <p class="meta">给 0 基础用户的实用指南 · 2026-10 · 基于 DSH Desktop 0.2.1-rc.2</p>
  <p class="links">
    <a href="{repo_url}">GitHub 仓库</a>
    <a href="#toc">目录</a>
    <a href="{repo_url}/issues">反馈</a>
  </p>
</header>
<main>
  <nav class="toc" id="toc" aria-label="目录">
    <h2>目录</h2>
    <ol>
{toc}
    </ol>
  </nav>
  <article class="book">
{body}
  </article>
</main>
<a class="top-link" href="#top" aria-label="回到顶部">↑</a>
<footer>
  <p>非官方学习材料，不代表 DeepSeek 官方；DSH / DeepSeek 名称与商标归其权利人。</p>
  <p>基于 DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · 无 JavaScript / 无 Cookie / 无第三方请求</p>
  <p><a href="{repo_url}">GitHub</a> · <a href="{site_url}">GitHub Pages</a></p>
</footer>
</body>
</html>
"""


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    start = text.find("# 第 1 章")
    if start == -1:
        raise SystemExit("cannot find '# 第 1 章' in dsh-book.md")
    body_md = text[start:]

    parser = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )
    body_html = parser.convert(body_md)

    chapters = re.findall(r'<h1 id="([^"]+)">(.*?)</h1>', body_html, flags=re.S)
    if not chapters:
        raise SystemExit("no chapter headings found in generated HTML")
    toc = "\n".join(
        f'      <li><a href="#{html.escape(anchor)}">{html.escape(strip_tags(title))}</a></li>'
        for anchor, title in chapters
    )

    page = (
        TEMPLATE.replace("{site_url}", SITE_URL)
        .replace("{repo_url}", REPO_URL)
        .replace("{toc}", toc)
        .replace("{body}", body_html)
    )

    # Privacy guard: the Pages build must stay static and self-contained.
    lowered = page.lower()
    forbidden = ("<script", "google-analytics", "googletagmanager", "plausible.io", "umami")
    for token in forbidden:
        if token in lowered:
            raise SystemExit(f"refusing to write site containing {token!r}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(page):,} chars, {len(chapters)} chapters)")


if __name__ == "__main__":
    main()
