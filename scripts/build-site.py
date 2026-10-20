#!/usr/bin/env python3
"""Build the bilingual static GitHub Pages site from dsh-book.md and en/dsh-book.md.

The site is intentionally static and self-contained:
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
<meta name="theme-color" content="#b45309">
<title>DeepSeek Harness 入门 · 从第一次对话到自己的插件</title>
<meta name="description" content="给 0 基础用户的 DeepSeek Harness 使用指南：模型、工作区、权限、会话、工具、技能、Preset、插件与创造模式。">
<meta property="og:title" content="DeepSeek Harness 入门">
<meta property="og:description" content="给 0 基础用户的 DeepSeek Harness 使用指南。">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="{og_locale}">
<link rel="canonical" href="{page_url}">
<link rel="alternate" hreflang="zh-CN" href="https://leether.github.io/dsh-book/">
<link rel="alternate" hreflang="en" href="https://leether.github.io/dsh-book/en/">
<link rel="alternate" hreflang="x-default" href="https://leether.github.io/dsh-book/">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{asset_prefix}favicon.svg" type="image/svg+xml">
<style>
:root {
  --bg: #f7f4ed;
  --paper: #fffefa;
  --ink: #20211f;
  --muted: #6b6a63;
  --line: #e3ded2;
  --accent: #b45309;
  --accent-2: #0f766e;
  --accent-soft: #fff3e0;
  --code: #f2eee5;
  --shadow: 0 24px 60px rgba(60, 40, 20, .12);
  --max: 1120px;
  --prose: 760px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #111214;
    --paper: #1a1b1e;
    --ink: #f1efe9;
    --muted: #a7a49b;
    --line: #303136;
    --accent: #f2a35e;
    --accent-2: #5eead4;
    --accent-soft: #2a2118;
    --code: #24252a;
    --shadow: 0 24px 60px rgba(0, 0, 0, .35);
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
html, body { max-width: 100%; overflow-x: hidden; }
body {
  margin: 0;
  background:
    radial-gradient(900px 520px at 8% -8%, rgba(180, 83, 9, .10), transparent 62%),
    radial-gradient(800px 520px at 100% 0%, rgba(15, 118, 110, .08), transparent 62%),
    var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Noto Sans SC", "Microsoft YaHei", sans-serif;
  font-size: 17px;
  line-height: 1.85;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-underline-offset: 3px; }
a:hover { text-decoration-thickness: 2px; }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 4px; }
::selection { background: var(--accent); color: #fff; }

.progress {
  display: none;
  position: fixed;
  inset: 0 0 auto 0;
  height: 3px;
  z-index: 100;
  background: linear-gradient(90deg, var(--accent), #f59e0b, var(--accent-2));
  transform-origin: 0 50%;
  transform: scaleX(0);
}
@supports (animation-timeline: scroll()) {
  .progress {
    display: block;
    animation: reading-progress linear;
    animation-timeline: scroll(root block);
  }
}
@keyframes reading-progress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 80;
  border-bottom: 1px solid var(--line);
  background: var(--bg);
}
@supports (background: color-mix(in srgb, #fff 80%, transparent)) {
  .topbar {
    background: color-mix(in srgb, var(--bg) 88%, transparent);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
  }
}
.topbar-inner {
  max-width: var(--max);
  flex-wrap: wrap;
  margin: 0 auto;
  padding: 13px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  letter-spacing: .01em;
}
.brand-mark {
  display: inline-grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--ink);
  color: var(--bg);
  font-size: 9px;
  letter-spacing: .08em;
}
.topbar-links { display: flex; flex-wrap: wrap; gap: 20px; align-items: center; min-width: 0; font-size: 14px; }
.topbar-links a { color: var(--muted); text-decoration: none; }
.topbar-links a:hover { color: var(--accent); }

.hero {
  max-width: var(--max);
  margin: 0 auto;
  padding: 82px 24px 54px;
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(260px, .88fr);
  gap: 56px;
  align-items: center;
}
.hero-copy { min-width: 0; }
.badge {
  display: inline-block;
  margin: 0 0 18px;
  padding: 5px 11px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper);
  color: var(--muted);
  font-size: 12px;
  letter-spacing: .06em;
}
.hero h1 {
  margin: 0;
  font-size: clamp(42px, 6.4vw, 76px);
  line-height: 1.04;
  letter-spacing: -.045em;
  font-weight: 800;
  text-wrap: balance;
}
.subtitle {
  margin: 16px 0 0;
  color: var(--muted);
  font-size: clamp(20px, 2.3vw, 28px);
  line-height: 1.35;
}
.lede {
  max-width: 34em;
  margin: 20px 0 0;
  color: var(--muted);
  font-size: 16px;
  line-height: 1.8;
}
.chips {
  max-width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 24px 0 0;
  padding: 0;
  list-style: none;
}
.chips li {
  padding: 5px 10px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--paper);
  color: var(--muted);
  font-size: 12px;
  overflow-wrap: anywhere;
}
.actions { max-width: 100%; display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px; }
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--paper);
  color: var(--ink);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: transform .16s ease, border-color .16s ease;
}
.button:hover { transform: translateY(-1px); border-color: var(--accent); }
.button.primary { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.button.primary:hover { background: var(--accent); border-color: var(--accent); color: #fff; }

.hero-cover { display: flex; justify-content: center; }
.cover {
  position: relative;
  width: min(100%, 330px);
  aspect-ratio: 3 / 4;
  display: flex;
  flex-direction: column;
  padding: 30px 28px 26px 36px;
  border-radius: 5px 18px 18px 5px;
  background:
    radial-gradient(300px 240px at 100% 0%, rgba(242, 163, 94, .20), transparent 65%),
    linear-gradient(148deg, #2b241d 0%, #151310 58%, #0b0a09 100%);
  color: #f8f1e7;
  box-shadow: var(--shadow), 0 2px 0 rgba(255,255,255,.18) inset;
  transform: rotate(2.4deg);
  overflow: hidden;
}
.cover::before {
  content: "";
  position: absolute;
  left: 15px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: rgba(255, 255, 255, .16);
}
.cover::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    repeating-linear-gradient(0deg, transparent 0 27px, rgba(255,255,255,.035) 28px),
    radial-gradient(240px 200px at 85% 85%, rgba(15, 118, 110, .22), transparent 70%);
  pointer-events: none;
}
.cover-label {
  position: relative;
  z-index: 1;
  color: #d9a66e;
  font-size: 10px;
  letter-spacing: .22em;
  text-transform: uppercase;
}
.cover-title {
  position: relative;
  z-index: 1;
  margin-top: auto;
  font-size: clamp(34px, 4.3vw, 48px);
  line-height: 1.05;
  letter-spacing: -.035em;
  font-weight: 800;
}
.cover-title em { color: #f0b47b; font-style: normal; }
.cover-sub {
  position: relative;
  z-index: 1;
  margin-top: 16px;
  color: #c9b8a6;
  font-size: 12px;
  line-height: 1.7;
}
.cover-foot {
  position: relative;
  z-index: 1;
  margin-top: 22px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, .16);
  color: #a99988;
  font-size: 10px;
  letter-spacing: .08em;
}

.layout {
  max-width: var(--max);
  margin: 0 auto;
  padding: 18px 24px 72px;
  display: grid;
  grid-template-columns: 250px minmax(0, 1fr);
  gap: 58px;
  align-items: start;
}
.sidebar {
  position: sticky;
  top: 84px;
  min-width: 0;
}
.sidebar-inner {
  max-height: calc(100vh - 108px);
  overflow: auto;
  padding: 4px 16px 18px 0;
  border-right: 1px solid var(--line);
  scrollbar-width: thin;
}
.sidebar-kicker {
  margin: 0 0 4px;
  color: var(--accent);
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
}
.sidebar h2 {
  margin: 0 0 14px;
  font-size: 17px;
  letter-spacing: -.01em;
}
.chapter-list { margin: 0; padding: 0; list-style: none; }
.chapter-list li { margin: 2px 0; }
.chapter-list a {
  display: flex;
  gap: 10px;
  align-items: baseline;
  padding: 6px 8px;
  border-radius: 7px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.45;
  text-decoration: none;
}
.chapter-list a:hover { background: var(--accent-soft); color: var(--ink); }
.chapter-list .num {
  flex: 0 0 1.7em;
  color: var(--accent);
  font-size: 10px;
  font-variant-numeric: tabular-nums;
  letter-spacing: .04em;
}
.sidebar-note {
  margin: 18px 0 0;
  padding-top: 14px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 11px;
  line-height: 1.6;
}

.book {
  min-width: 0;
  max-width: var(--prose);
  font-size: 17.5px;
  line-height: 1.92;
}
.book h1 {
  position: relative;
  margin: 4.2rem 0 1rem;
  padding: 1.5rem 0 0 20px;
  border-top: 1px solid var(--line);
  font-size: clamp(28px, 3.8vw, 38px);
  line-height: 1.3;
  letter-spacing: -.025em;
  scroll-margin-top: 96px;
}
.book h1::before {
  content: "";
  position: absolute;
  left: 0;
  top: 1.55rem;
  bottom: .2rem;
  width: 4px;
  border-radius: 2px;
  background: var(--accent);
}
.book h1:first-child { margin-top: 0; padding-top: 0; border-top: 0; }
.book h1:first-child::before { top: .2rem; }
.book h2 {
  margin: 2.6rem 0 .8rem;
  font-size: clamp(22px, 2.6vw, 27px);
  line-height: 1.35;
  letter-spacing: -.015em;
  scroll-margin-top: 96px;
}
.book h3 { margin: 1.8rem 0 .6rem; font-size: 19px; line-height: 1.45; }
.book p { margin: .9rem 0; }
.book ul, .book ol { padding-left: 1.55em; }
.book li { margin: .35rem 0; }
.book strong { font-weight: 700; }
.book blockquote {
  margin: 1.3rem 0;
  padding: 12px 18px;
  border-left: 4px solid var(--accent);
  border-radius: 0 9px 9px 0;
  background: var(--accent-soft);
}
.book blockquote p { margin: .3rem 0; }
.book code {
  padding: .15em .35em;
  border-radius: 5px;
  background: var(--code);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  font-size: .88em;
}
.book pre {
  margin: 1.15rem 0;
  padding: 17px 18px;
  overflow-x: auto;
  background: var(--code);
  border: 1px solid var(--line);
  border-radius: 11px;
  line-height: 1.55;
}
.book pre code { padding: 0; background: transparent; font-size: 13.5px; }
.book pre, .book table { max-width: 100%; }
.book table {
  display: block;
  width: 100%;
  margin: 1.25rem 0;
  overflow-x: auto;
  border-collapse: collapse;
  font-size: 14.5px;
  line-height: 1.65;
}
.book th, .book td {
  padding: 9px 11px;
  border: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}
.book th { background: var(--code); white-space: nowrap; font-weight: 600; }
.book tr:nth-child(even) td { background: color-mix(in srgb, var(--code) 42%, transparent); }
.book hr { margin: 2.8rem 0; border: 0; border-top: 1px solid var(--line); }
.book img { max-width: 100%; height: auto; border-radius: 8px; }
.chapter-meta {
  margin: 8px 0 1.5rem 20px;
  color: var(--muted);
  font-size: 12px;
  letter-spacing: .03em;
}
.chapter { margin-bottom: 1.8rem; }
.pager {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin: 40px 0 0;
  padding-top: 20px;
  border-top: 1px solid var(--line);
}
.pager a {
  display: block;
  min-width: 0;
  padding: 13px 15px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--paper);
  color: var(--ink);
  text-decoration: none;
  font-size: 13px;
  line-height: 1.45;
  transition: border-color .16s ease, transform .16s ease;
}
.pager a:hover { border-color: var(--accent); transform: translateY(-1px); }
.pager small { display: block; margin-bottom: 3px; color: var(--muted); font-size: 10px; letter-spacing: .08em; }
.pager .next { text-align: right; grid-column: 2; }
.pager .next span { display: block; }
.pager .prev span { display: block; }
.chapter-list a span:last-child { min-width: 0; overflow-wrap: anywhere; }

footer {
  max-width: var(--max);
  margin: 0 auto;
  padding: 28px 24px 56px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 13px;
  line-height: 1.7;
}
footer p { margin: .35rem 0; }
footer a { color: var(--muted); }
footer a:hover { color: var(--accent); }

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
  font-size: 19px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, .08);
  z-index: 60;
}
.top-link:hover { border-color: var(--accent); color: var(--accent); }

@media (max-width: 980px) {
  .hero { grid-template-columns: 1fr; gap: 36px; padding-top: 56px; }
  .hero-cover { display: none; }
  .layout { grid-template-columns: 1fr; gap: 34px; }
  .sidebar { position: static; }
  .sidebar-inner {
    max-height: none;
    overflow: visible;
    padding: 0 0 18px;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }
  .chapter-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2px 14px;
  }
  .sidebar-note { display: none; }
}
@media (max-width: 620px) {
  body { font-size: 16px; }
  .topbar-inner { padding: 11px 16px; }
  .topbar-links { gap: 12px; }
  .topbar-links a:nth-child(2) { display: none; }
  .hero { padding: 40px 16px 38px; }
  .hero h1 { font-size: clamp(36px, 11vw, 54px); }
  .layout { padding: 8px 16px 48px; }
  .book { font-size: 16.5px; }
  .chapter-list { grid-template-columns: 1fr; }
  .book table { font-size: 13.5px; }
  .pager { grid-template-columns: 1fr; }
  .pager .next { grid-column: auto; }
  .top-link { right: 12px; bottom: 12px; width: 38px; height: 38px; }
  footer { padding-left: 16px; padding-right: 16px; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
  .progress { display: none; }
}
@media print {
  :root {
    --bg: #fff; --paper: #fff; --ink: #000; --muted: #444;
    --line: #ccc; --code: #f2f2f2; --accent: #000;
  }
  body { background: #fff; font-size: 11pt; }
  .topbar, .progress, .sidebar, .hero-cover, .top-link, .pager { display: none; }
  .hero { display: block; padding: 0 0 12mm; }
  .hero h1 { font-size: 28pt; }
  .layout { display: block; padding: 0; }
  .book { max-width: none; font-size: 11pt; }
  .book h1 { break-before: page; }
  .book h1:first-child { break-before: auto; }
  .book h1::before { display: none; }
  .book a { color: #000; text-decoration: none; }
  .book pre, .book table { break-inside: avoid; }
}
</style>
</head>
<body id="top">
<div class="progress" aria-hidden="true"></div>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#top"><span class="brand-mark">DSH</span><span>入门</span></a>
    <nav class="topbar-links" aria-label="快速导航">
      <a href="#toc">目录</a>
      <a href="#start">开始阅读</a>
      <a href="{repo_url}">GitHub</a>
      {language_switch}
    </nav>
  </div>
</header>
<header class="hero">
  <div class="hero-copy">
    <p class="badge">非官方指南 · 无 Cookie · 无统计</p>
    <h1>DeepSeek Harness 入门</h1>
    <p class="subtitle">从第一次对话到自己的插件</p>
    <p class="lede">给 0 基础用户的实用指南。先学会用，再理解原理，最后扩展它。</p>
    <ul class="chips">
      <li>{chapter_count} 章 + 附录</li>
      <li>约 {total_words} 万字</li>
      <li>约 {total_minutes} 分钟</li>
      <li>DSH Desktop 0.2.1-rc.2</li>
    </ul>
    <div class="actions">
      <a class="button primary" href="#start">开始阅读</a>
      <a class="button" href="{repo_url}">GitHub 仓库</a>
    </div>
  </div>
  <div class="hero-cover" aria-hidden="true">
    <div class="cover">
      <span class="cover-label">DSH Field Guide</span>
      <span class="cover-title">DeepSeek<br>Harness<br><em>入门</em></span>
      <span class="cover-sub">从第一次对话<br>到自己的插件</span>
      <span class="cover-foot">0 基础 · {chapter_count} 章 + 附录</span>
    </div>
  </div>
</header>
<main class="layout" id="start">
  <aside class="sidebar">
    <div class="sidebar-inner" id="toc">
      <p class="sidebar-kicker">Contents</p>
      <h2>本书地图</h2>
      <ol class="chapter-list">
{toc}
      </ol>
      <p class="sidebar-note">非官方学习材料 · MIT License<br>无 JavaScript / 无 Cookie / 无第三方请求</p>
    </div>
  </aside>
  <article class="book">
{body}
  </article>
</main>
<a class="top-link" href="#top" aria-label="回到顶部">↑</a>
<footer>
  <p>非官方学习材料，不代表 DeepSeek 官方；DSH / DeepSeek 名称与商标归其权利人。</p>
  <p>基于 DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · 无 JavaScript / 无 Cookie / 无第三方请求</p>
  <p><a href="{repo_url}">GitHub</a> · <a href="{page_url}">GitHub Pages</a></p>
</footer>
</body>
</html>
"""


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def short_title(value: str, limit: int = 18) -> str:
    value = value.strip()
    return value if len(value) <= limit else value[:limit].rstrip() + "…"

LANGUAGES = [
    {
        "key": "zh",
        "source": "dsh-book.md",
        "output": "docs/index.html",
        "lang": "zh-CN",
        "page_url": SITE_URL,
        "asset_prefix": "",
        "og_locale": "zh_CN",
        "strip_title": re.compile(r"^第\s*\d+\s*章\s*[　\s]*"),
        "appendix_prefix": "附录",
        "appendix_number": "附",
        "meta": "约 {minutes} 分钟 · {value:,} 字 · {sections} 个小节",
        "count_mode": "chars",
        "divisor": 500,
        "short_limit": 18,
        "prev_small": "上一章",
        "next_small": "下一章",
        "back_small": "返回",
        "end_small": "结束",
        "contents": "目录",
        "chapter_nav": "章节导航",
        "top": "回到顶部",
        "switch": '<a href="en/" hreflang="en" lang="en">English</a>',
        "static": {},
    },
    {
        "key": "en",
        "source": "en/dsh-book.md",
        "output": "docs/en/index.html",
        "lang": "en",
        "page_url": f"{SITE_URL}en/",
        "asset_prefix": "../",
        "og_locale": "en_US",
        "strip_title": re.compile(r"^Chapter\s+\d+\s*[—–-]\s*", re.IGNORECASE),
        "appendix_prefix": "appendix",
        "appendix_number": "A",
        "meta": "{minutes} min read · {value:,} words · {sections} sections",
        "count_mode": "words",
        "divisor": 220,
        "short_limit": 26,
        "prev_small": "Previous",
        "next_small": "Next",
        "back_small": "Back",
        "end_small": "End",
        "contents": "Contents",
        "chapter_nav": "Chapter navigation",
        "top": "Back to top",
        "switch": '<a href="../" hreflang="zh-CN" lang="zh-CN">中文</a>',
        "static": {
            '<html lang="zh-CN">': '<html lang="en">',
            "<title>DeepSeek Harness 入门 · 从第一次对话到自己的插件</title>":
                "<title>DeepSeek Harness: A Beginner's Guide</title>",
            '<meta name="description" content="给 0 基础用户的 DeepSeek Harness 使用指南：模型、工作区、权限、会话、工具、技能、Preset、插件与创造模式。">':
                '<meta name="description" content="A practical, beginner-friendly guide to DeepSeek Harness: models, workspaces, permissions, sessions, tools, skills, presets, plugins, and Creator mode.">',
            '<meta property="og:title" content="DeepSeek Harness 入门">':
                '<meta property="og:title" content="DeepSeek Harness: A Beginner\'s Guide">',
            '<meta property="og:description" content="给 0 基础用户的 DeepSeek Harness 使用指南。">':
                '<meta property="og:description" content="A practical, beginner-friendly guide to DeepSeek Harness.">',
            "<span>入门</span>": "<span>Guide</span>",
            'aria-label="快速导航"': 'aria-label="Quick navigation"',
            '<a href="#toc">目录</a>': '<a href="#toc">Contents</a>',
            '<a href="#start">开始阅读</a>': '<a href="#start">Start reading</a>',
            '<p class="badge">非官方指南 · 无 Cookie · 无统计</p>':
                '<p class="badge">Unofficial guide · No cookies · No tracking</p>',
            "<h1>DeepSeek Harness 入门</h1>": "<h1>DeepSeek Harness</h1>",
            '<p class="subtitle">从第一次对话到自己的插件</p>':
                '<p class="subtitle">A Beginner\'s Guide</p>',
            '<p class="lede">给 0 基础用户的实用指南。先学会用，再理解原理，最后扩展它。</p>':
                '<p class="lede">A practical guide for complete beginners. Learn to use it, understand it, then extend it.</p>',
            "<li>{chapter_count} 章 + 附录</li>": "<li>{chapter_count} chapters + appendix</li>",
            "<li>约 {total_words} 万字</li>": "<li>~{total_words} words</li>",
            "<li>约 {total_minutes} 分钟</li>": "<li>~{total_minutes} min read</li>",
            '<a class="button primary" href="#start">开始阅读</a>':
                '<a class="button primary" href="#start">Start reading</a>',
            '<a class="button" href="{repo_url}">GitHub 仓库</a>':
                '<a class="button" href="{repo_url}">GitHub repository</a>',
            "<em>入门</em>": "<em>Guide</em>",
            '<span class="cover-sub">从第一次对话<br>到自己的插件</span>':
                '<span class="cover-sub">From your first conversation<br>to your own plugin</span>',
            '<span class="cover-foot">0 基础 · {chapter_count} 章 + 附录</span>':
                '<span class="cover-foot">Beginner-friendly · {chapter_count} chapters + appendix</span>',
            "<h2>本书地图</h2>": "<h2>Book map</h2>",
            '<p class="sidebar-note">非官方学习材料 · MIT License<br>无 JavaScript / 无 Cookie / 无第三方请求</p>':
                '<p class="sidebar-note">An unofficial guide · MIT License<br>No JavaScript / cookies / third-party requests</p>',
            'aria-label="回到顶部"': 'aria-label="Back to top"',
            "<p>非官方学习材料，不代表 DeepSeek 官方；DSH / DeepSeek 名称与商标归其权利人。</p>":
                "<p>An unofficial guide. Not affiliated with DeepSeek. DSH / DeepSeek names and trademarks belong to their owners.</p>",
            "<p>基于 DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · 无 JavaScript / 无 Cookie / 无第三方请求</p>":
                "<p>Based on DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · No JavaScript / cookies / third-party requests</p>",
        },
    },
]


def build_site(cfg: dict) -> None:
    text = (ROOT / cfg["source"]).read_text(encoding="utf-8")
    start_marker = "# 第 1 章" if cfg["key"] == "zh" else "# Chapter 1"
    start = text.find(start_marker)
    if start == -1:
        raise SystemExit(f"cannot find {start_marker!r} in {cfg['source']}")
    body_md = text[start:]

    parser = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )
    body_html = parser.convert(body_md)

    matches = list(re.finditer(r'<h1 id="([^"]+)">(.*?)</h1>', body_html, flags=re.S))
    if not matches:
        raise SystemExit(f"no chapter headings found in {cfg['source']}")

    chapters = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body_html)
        chunk = body_html[match.start():end]
        raw_title = strip_tags(match.group(2))
        title = cfg["strip_title"].sub("", raw_title).strip() or raw_title
        plain = re.sub(r"\s+", "", strip_tags(chunk))
        if cfg["count_mode"] == "words":
            value = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’_-]*", strip_tags(chunk)))
        else:
            value = len(plain)
        sections = len(re.findall(r"<h2\b", chunk))
        minutes = max(1, round(value / cfg["divisor"]))
        is_appendix = title.lower().startswith(cfg["appendix_prefix"])
        number = cfg["appendix_number"] if is_appendix else f"{index + 1:02d}"
        chapters.append({
            "anchor": match.group(1),
            "title": title,
            "number": number,
            "value": value,
            "minutes": minutes,
            "sections": sections,
            "html": chunk,
            "is_appendix": is_appendix,
        })

    body_parts = []
    for index, chapter in enumerate(chapters):
        meta = cfg["meta"].format(
            minutes=chapter["minutes"],
            value=chapter["value"],
            sections=chapter["sections"],
        )
        chunk = chapter["html"].replace(
            "</h1>",
            f'</h1>\n<p class="chapter-meta">{meta}</p>',
            1,
        )

        if index == 0:
            prev_href, prev_small, prev_label = "#toc", cfg["back_small"], cfg["contents"]
        else:
            previous = chapters[index - 1]
            prev_href = f'#{previous["anchor"]}'
            prev_small, prev_label = cfg["prev_small"], short_title(previous["title"], cfg["short_limit"])

        if index + 1 < len(chapters):
            following = chapters[index + 1]
            next_href = f'#{following["anchor"]}'
            next_small, next_label = cfg["next_small"], short_title(following["title"], cfg["short_limit"])
        else:
            next_href, next_small, next_label = "#top", cfg["end_small"], cfg["top"]

        pager = (
            f'<nav class="pager" aria-label="{cfg["chapter_nav"]}">\n'
            f'  <a class="prev" href="{prev_href}"><small>{prev_small}</small><span>{html.escape(prev_label)}</span></a>\n'
            f'  <a class="next" href="{next_href}"><small>{next_small}</small><span>{html.escape(next_label)}</span></a>\n'
            "</nav>"
        )
        body_parts.append(f'<section class="chapter">\n{chunk}{pager}\n</section>')

    toc = "\n".join(
        f'        <li><a href="#{html.escape(chapter["anchor"])}">'
        f'<span class="num">{chapter["number"]}</span>'
        f'<span>{html.escape(chapter["title"])}</span></a></li>'
        for chapter in chapters
    )

    total_value = sum(chapter["value"] for chapter in chapters)
    total_minutes = sum(chapter["minutes"] for chapter in chapters)
    main_chapters = sum(1 for chapter in chapters if not chapter["is_appendix"])
    total_words = (
        f"{total_value / 10000:.1f}"
        if cfg["count_mode"] == "chars"
        else f"{total_value:,}"
    )

    page = (
        TEMPLATE.replace("{language_switch}", cfg["switch"])
        .replace("{asset_prefix}", cfg["asset_prefix"])
        .replace("{page_url}", cfg["page_url"])
        .replace("{og_locale}", cfg["og_locale"])
    )
    for old, new in cfg["static"].items():
        page = page.replace(old, new)
    page = page.replace("{repo_url}", REPO_URL)

    page = (
        page.replace("{chapter_count}", str(main_chapters))
        .replace("{total_words}", total_words)
        .replace("{total_minutes}", str(total_minutes))
        .replace("{toc}", toc)
        .replace("{body}", "\n".join(body_parts))
    )

    unresolved = [token for token in (
        "{repo_url}", "{language_switch}", "{asset_prefix}", "{page_url}",
        "{og_locale}", "{chapter_count}", "{total_words}", "{total_minutes}",
        "{toc}", "{body}",
    ) if token in page]
    if unresolved:
        raise SystemExit(f"unresolved placeholders in {cfg['output']}: {unresolved}")

    # Privacy guard: the Pages build must stay static and self-contained.
    lowered = page.lower()
    forbidden = ("<script", "google-analytics", "googletagmanager", "plausible.io", "umami")
    for token in forbidden:
        if token in lowered:
            raise SystemExit(f"refusing to write {cfg['output']} containing {token!r}")

    # Keep the English page English: the only Han characters allowed are the
    # language-switch label "中文".
    if cfg["lang"] == "en":
        check = page.replace("中文", "")
        if re.search(r"[\u4e00-\u9fff]", check):
            found = sorted(set(re.findall(r"[\u4e00-\u9fff]+", check)))[:12]
            raise SystemExit(f"untranslated Chinese in English page: {found}")

    output = ROOT / cfg["output"]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8")
    print(
        f"wrote {cfg['output']} "
        f"({len(page):,} chars, {len(chapters)} chapters, {total_value:,} {cfg['count_mode']})"
    )


def main() -> None:
    for cfg in LANGUAGES:
        build_site(cfg)


if __name__ == "__main__":
    main()
