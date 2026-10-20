#!/usr/bin/env python3
"""Build the bilingual, per-chapter GitHub Pages site.

Sources:
  dsh-book.md      -> Chinese pages under docs/
  en/dsh-book.md   -> English pages under docs/en/

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
SITE_URL = "https://leether.github.io/dsh-book/"
REPO_URL = "https://github.com/leether/dsh-book"
STYLE_FILE = "style.css"

LANGUAGES = [
    {
        "key": "zh",
        "source": "dsh-book.md",
        "out_dir": "docs",
        "lang": "zh-CN",
        "locale": "zh_CN",
        "asset_prefix": "",
        "source_start": "# 第 1 章",
        "strip_title": re.compile(r"^第\s*\d+\s*章\s*[　\s]*"),
        "appendix_prefix": "附录",
        "appendix_number": "附",
        "count_mode": "chars",
        "divisor": 500,
        "short_limit": 18,
        "book_title": "DeepSeek Harness 入门",
        "book_short": "DSH 入门",
        "subtitle": "从第一次对话到自己的插件",
        "badge": "非官方指南 · 无 Cookie · 无统计",
        "lede": "给 0 基础用户的实用指南。先学会用，再理解原理，最后扩展它。",
        "start": "开始阅读",
        "github": "GitHub 仓库",
        "contents": "目录",
        "contents_kicker": "Contents",
        "book_map": "本书地图",
        "contents_intro": "10 章 + 附录。可以按顺序读，也可以直接跳到需要的一章。",
        "chapter_label": "第 {n} 章",
        "appendix_label": "附录",
        "appendix_short": "附",
        "meta": "约 {minutes} 分钟 · {value:,} 字 · {sections} 个小节",
        "prev_small": "上一章",
        "next_small": "下一章",
        "back_small": "返回",
        "end_small": "结束",
        "top_label": "回到顶部",
        "paths_title": "三条阅读路线",
        "paths": [
            ("日常使用", "第 1–7 章：先把工作区、权限、上下文和工具用熟。"),
            ("装插件/技能", "第 1–8 章：理解 Plugin、Bundle、Profile 和 Preset。"),
            ("做插件", "第 1–9 章：进入创造模式，完成一次最小扩展。"),
        ],
        "about_title": "关于这本书",
        "about_text": "这是一本非官方的 DSH 入门书，写给第一次让 Agent 读写文件、执行任务的人。它不追求讲完所有 API，而是先帮你建立正确的工作方式：小工作区、先只读、先计划、再验收。",
        "about_meta": "基于 DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License",
        "blurbs": [
            "先分清模型、Harness 和 Agent，知道 DSH 到底在做什么。",
            "从桌面入口、模型连接和一个小工作区开始。",
            "用“目标 + 输入 + 约束 + 验收”完成第一个任务。",
            "看懂工作区边界、审批和破坏性操作。",
            "理解 Session、上下文窗口，以及为什么它会忘事。",
            "认识工具、计划、子代理和 Skill 的分工。",
            "标准、创造、PTC、极简，什么时候用哪个。",
            "Plugin、Bundle、Profile 三层，以及怎么安装。",
            "创造模式能做什么，以及它的安全边界。",
            "常见错误、成本控制和安全清单。",
            "术语表、提示词模板和速查表。",
        ],
        "nav_quick": "快速导航",
        "chapter_nav": "章节导航",
        "switch_label": "English",
        "switch_lang": "en",
        "cover_word": "入门",
        "cover_sub": "从第一次对话<br>到自己的插件",
        "footer": [
            "非官方学习材料，不代表 DeepSeek 官方；DSH / DeepSeek 名称与商标归其权利人。",
            "基于 DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · 无 JavaScript / 无 Cookie / 无第三方请求",
        ],
    },
    {
        "key": "en",
        "source": "en/dsh-book.md",
        "out_dir": "docs/en",
        "lang": "en",
        "locale": "en_US",
        "asset_prefix": "../",
        "source_start": "# Chapter 1",
        "strip_title": re.compile(r"^Chapter\s+\d+\s*[—–-]\s*", re.IGNORECASE),
        "appendix_prefix": "appendix",
        "appendix_number": "A",
        "count_mode": "words",
        "divisor": 220,
        "short_limit": 26,
        "book_title": "DeepSeek Harness",
        "book_short": "DSH Guide",
        "subtitle": "A Beginner's Guide",
        "badge": "Unofficial guide · No cookies · No tracking",
        "lede": "A practical guide for complete beginners. Learn to use it, understand it, then extend it.",
        "start": "Start reading",
        "github": "GitHub repository",
        "contents": "Contents",
        "contents_kicker": "Contents",
        "book_map": "Book map",
        "contents_intro": "10 chapters + appendix. Read in order, or jump straight to the chapter you need.",
        "chapter_label": "Chapter {n}",
        "appendix_label": "Appendix",
        "appendix_short": "A",
        "meta": "{minutes} min read · {value:,} words · {sections} sections",
        "prev_small": "Previous",
        "next_small": "Next",
        "back_small": "Back",
        "end_small": "End",
        "top_label": "Back to top",
        "paths_title": "Three reading paths",
        "paths": [
            ("Everyday use", "Chapters 1–7: get comfortable with workspaces, permissions, context, and tools."),
            ("Plugins and skills", "Chapters 1–8: understand Plugin, Bundle, Profile, and Preset."),
            ("Build a plugin", "Chapters 1–9: enter Creator mode and build one small extension."),
        ],
        "about_title": "About this book",
        "about_text": "An unofficial, practical introduction to DSH for people who are about to let an Agent read files, run tasks, and change real things. It does not try to document every API. It builds the right habits first: use a small workspace, start read-only, plan before executing, and ask for evidence before accepting. This English edition was edited for natural English usage; corrections are welcome.",
        "about_meta": "Based on DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License",
        "blurbs": [
            "Separate the model, the harness, and the Agent.",
            "Connect a model, pick a workspace, and start your first conversation.",
            "Turn a vague request into a verifiable task.",
            "Understand workspace boundaries, approvals, and destructive actions.",
            "Learn why the Agent forgets, and how to work with context.",
            "Tools, plans, subagents, and Skills — who does what.",
            "Standard, Creator, PTC, and Minimal — when to use each.",
            "Plugin, Bundle, Profile, and how installation works.",
            "What Creator mode can do, and where its safety boundary is.",
            "Common failures, cost control, and a safety checklist.",
            "Glossary, prompt templates, and a one-page cheat sheet.",
        ],
        "nav_quick": "Quick navigation",
        "chapter_nav": "Chapter navigation",
        "switch_label": "中文",
        "switch_lang": "zh-CN",
        "cover_word": "Guide",
        "cover_sub": "From your first conversation<br>to your own plugin",
        "footer": [
            "An unofficial guide. Not affiliated with DeepSeek. DSH / DeepSeek names and trademarks belong to their owners.",
            "Based on DeepSeek Harness Desktop 0.2.1-rc.2 · MIT License · No JavaScript / cookies / third-party requests",
        ],
    },
]

LANG_BY_KEY = {lang["key"]: lang for lang in LANGUAGES}


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def short_title(value: str, limit: int) -> str:
    value = value.strip()
    return value if len(value) <= limit else value[:limit].rstrip() + "…"


def page_url(lang: dict, slug: str) -> str:
    base = SITE_URL if lang["key"] == "zh" else f"{SITE_URL}en/"
    return base if slug == "index.html" else f"{base}{slug}"


def switch_href(lang: dict, slug: str) -> str:
    if lang["key"] == "zh":
        return "en/" if slug == "index.html" else f"en/{slug}"
    return "../" if slug == "index.html" else f"../{slug}"


def parse_chapters(lang: dict) -> list[dict]:
    text = (ROOT / lang["source"]).read_text(encoding="utf-8")
    start = text.find(lang["source_start"])
    if start == -1:
        raise SystemExit(f"cannot find {lang['source_start']!r} in {lang['source']}")
    body_md = text[start:]

    parser = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )
    body_html = parser.convert(body_md)
    matches = list(re.finditer(r'<h1 id="([^"]+)">(.*?)</h1>', body_html, flags=re.S))
    if not matches:
        raise SystemExit(f"no chapter headings found in {lang['source']}")

    chapters = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body_html)
        chunk = body_html[match.start():end]
        raw_title = strip_tags(match.group(2))
        title = lang["strip_title"].sub("", raw_title).strip() or raw_title
        plain = re.sub(r"\s+", "", strip_tags(chunk))
        if lang["count_mode"] == "words":
            value = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’_-]*", strip_tags(chunk)))
        else:
            value = len(plain)
        sections = len(re.findall(r"<h2\b", chunk))
        minutes = max(1, round(value / lang["divisor"]))
        is_appendix = title.lower().startswith(lang["appendix_prefix"])
        number = lang["appendix_number"] if is_appendix else f"{index + 1:02d}"
        slug = "appendix.html" if is_appendix else f"ch{index + 1:02d}.html"
        label = lang["appendix_label"] if is_appendix else lang["chapter_label"].format(n=index + 1)
        chapters.append({
            "anchor": match.group(1),
            "title": title,
            "label": label,
            "number": number,
            "value": value,
            "minutes": minutes,
            "sections": sections,
            "html": chunk,
            "is_appendix": is_appendix,
            "slug": slug,
        })
    return chapters


def head(lang: dict, title: str, description: str, slug: str) -> str:
    canonical = page_url(lang, slug)
    zh_url = page_url(LANG_BY_KEY["zh"], slug)
    en_url = page_url(LANG_BY_KEY["en"], slug)
    return f"""<!doctype html>
<html lang="{lang['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#b45309">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{lang['locale']}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{zh_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{zh_url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{lang['asset_prefix']}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{lang['asset_prefix']}{STYLE_FILE}">
</head>
<body id="top">
<div class="progress" aria-hidden="true"></div>
"""


def topbar(lang: dict, slug: str, contents_href: str, start_href: str) -> str:
    switch = switch_href(lang, slug)
    return f"""<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html"><span class="brand-mark">DSH</span><span>{html.escape(lang['book_short'].replace('DSH ', ''))}</span></a>
    <nav class="topbar-links" aria-label="{html.escape(lang['nav_quick'])}">
      <a href="{contents_href}">{html.escape(lang['contents'])}</a>
      <a href="{start_href}">{html.escape(lang['start'])}</a>
      <a href="{REPO_URL}">GitHub</a>
      <a class="lang-switch" href="{switch}" hreflang="{lang['switch_lang']}" lang="{lang['switch_lang']}">{html.escape(lang['switch_label'])}</a>
    </nav>
  </div>
</header>
"""


def footer(lang: dict, slug: str) -> str:
    url = page_url(lang, slug)
    return f"""<footer>
  <p>{html.escape(lang['footer'][0])}</p>
  <p>{html.escape(lang['footer'][1])}</p>
  <p><a href="{REPO_URL}">GitHub</a> · <a href="{url}">GitHub Pages</a></p>
</footer>
<a class="top-link" href="#top" aria-label="{html.escape(lang['top_label'])}">↑</a>
</body>
</html>
"""


def chapter_list(lang: dict, chapters: list[dict], current_slug: str) -> str:
    rows = []
    for chapter in chapters:
        current = ' aria-current="page"' if chapter["slug"] == current_slug else ""
        rows.append(
            f'        <li><a href="{chapter["slug"]}"{current}>'
            f'<span class="num">{chapter["number"]}</span>'
            f'<span>{html.escape(chapter["title"])}</span></a></li>'
        )
    return "\n".join(rows)


def chapter_meta(lang: dict, chapter: dict) -> str:
    return lang["meta"].format(
        minutes=chapter["minutes"],
        value=chapter["value"],
        sections=chapter["sections"],
    )


def landing_page(lang: dict, chapters: list[dict], total_value: int, total_minutes: int) -> str:
    main_chapters = [chapter for chapter in chapters if not chapter["is_appendix"]]
    chapter_count = len(main_chapters)
    total_words = (
        f"{total_value / 10000:.1f}"
        if lang["count_mode"] == "chars"
        else f"{total_value:,}"
    )
    cards = []
    for index, chapter in enumerate(chapters):
        extra = " appendix" if chapter["is_appendix"] else ""
        blurb = lang["blurbs"][index] if index < len(lang["blurbs"]) else ""
        cards.append(
            f"""      <a class="chapter-card{extra}" href="{chapter["slug"]}">
        <span class="num">{chapter["number"]}</span>
        <h3>{html.escape(chapter["title"])}</h3>
        <p>{html.escape(blurb)}</p>
        <span class="meta">{html.escape(chapter_meta(lang, chapter))}</span>
      </a>"""
        )

    paths = "\n".join(
        f"""      <div class="path">
        <strong>{html.escape(title)}</strong>
        <span>{html.escape(description)}</span>
      </div>"""
        for title, description in lang["paths"]
    )

    chip_chapters = (
        f"{chapter_count} 章 + 附录"
        if lang["key"] == "zh"
        else f"{chapter_count} chapters + appendix"
    )
    chip_words = (
        f"约 {total_words} 万字"
        if lang["key"] == "zh"
        else f"~{total_words} words"
    )
    chip_minutes = (
        f"约 {total_minutes} 分钟"
        if lang["key"] == "zh"
        else f"~{total_minutes} min read"
    )
    cover_foot = (
        f"0 基础 · {chapter_count} 章 + 附录"
        if lang["key"] == "zh"
        else f"Beginner-friendly · {chapter_count} chapters + appendix"
    )

    title = f"{lang['book_title']} · {lang['subtitle']}" if lang["key"] == "zh" else f"{lang['book_title']}: {lang['subtitle']}"
    description = lang["lede"]

    body = f"""<header class="hero">
  <div class="hero-copy">
    <p class="badge">{html.escape(lang['badge'])}</p>
    <h1>{html.escape(lang['book_title'])}</h1>
    <p class="subtitle">{html.escape(lang['subtitle'])}</p>
    <p class="lede">{html.escape(lang['lede'])}</p>
    <ul class="chips">
      <li>{html.escape(chip_chapters)}</li>
      <li>{html.escape(chip_words)}</li>
      <li>{html.escape(chip_minutes)}</li>
      <li>DSH Desktop 0.2.1-rc.2</li>
    </ul>
    <div class="actions">
      <a class="button primary" href="ch01.html">{html.escape(lang['start'])}</a>
      <a class="button" href="{REPO_URL}">{html.escape(lang['github'])}</a>
    </div>
  </div>
  <div class="hero-cover" aria-hidden="true">
    <div class="cover">
      <span class="cover-label">DSH Field Guide</span>
      <span class="cover-title">DeepSeek<br>Harness<br><em>{html.escape(lang['cover_word'])}</em></span>
      <span class="cover-sub">{lang['cover_sub']}</span>
      <span class="cover-foot">{html.escape(cover_foot)}</span>
    </div>
  </div>
</header>
<main class="landing">
  <section class="landing-section" id="contents">
    <div class="section-heading">
      <h2>{html.escape(lang['book_map'])}</h2>
      <p>{html.escape(lang['contents_intro'])}</p>
    </div>
    <div class="book-map">
{chr(10).join(cards)}
    </div>
  </section>

  <section class="landing-section">
    <div class="section-heading"><h2>{html.escape(lang['paths_title'])}</h2></div>
    <div class="reading-paths">
{paths}
    </div>
  </section>

  <section class="landing-section">
    <div class="about-book">
      <div>
        <h2>{html.escape(lang['about_title'])}</h2>
        <p>{html.escape(lang['about_text'])}</p>
      </div>
      <p class="about-meta">{html.escape(lang['about_meta'])}<br><a href="{REPO_URL}">GitHub</a> · <a href="{page_url(lang, 'index.html')}">GitHub Pages</a></p>
    </div>
  </section>
</main>
"""

    page = (
        head(lang, title, description, "index.html")
        + topbar(lang, "index.html", "#contents", "ch01.html")
        + body
        + footer(lang, "index.html")
    )
    return page


def chapter_page(lang: dict, chapters: list[dict], index: int) -> str:
    chapter = chapters[index]
    meta = chapter_meta(lang, chapter)
    content = chapter["html"].replace(
        "</h1>",
        f'</h1>\n<p class="chapter-meta">{html.escape(meta)}</p>',
        1,
    )

    if index == 0:
        prev_href, prev_small, prev_label = "index.html#contents", lang["back_small"], lang["contents"]
    else:
        previous = chapters[index - 1]
        prev_href = previous["slug"]
        prev_small = lang["prev_small"]
        prev_label = short_title(previous["title"], lang["short_limit"])

    if index + 1 < len(chapters):
        following = chapters[index + 1]
        next_href = following["slug"]
        next_small = lang["next_small"]
        next_label = short_title(following["title"], lang["short_limit"])
    else:
        next_href, next_small, next_label = "index.html#contents", lang["end_small"], lang["contents"]

    pager = f"""<nav class="pager" aria-label="{html.escape(lang['chapter_nav'])}">
  <a class="prev" href="{prev_href}"><small>{html.escape(prev_small)}</small><span>{html.escape(prev_label)}</span></a>
  <a class="next" href="{next_href}"><small>{html.escape(next_small)}</small><span>{html.escape(next_label)}</span></a>
</nav>"""

    toc = chapter_list(lang, chapters, chapter["slug"])
    body = f"""<main class="layout" id="start">
  <aside class="sidebar">
    <div class="sidebar-inner" id="toc">
      <p class="sidebar-kicker">{html.escape(lang['contents_kicker'])}</p>
      <h2>{html.escape(lang['book_map'])}</h2>
      <ol class="chapter-list">
{toc}
      </ol>
      <p class="sidebar-note">{html.escape(lang['footer'][0])}<br>{html.escape(lang['footer'][1])}</p>
    </div>
  </aside>
  <article class="book">
    <p class="breadcrumb"><a href="index.html#contents">{html.escape(lang['contents'])}</a> / {html.escape(chapter['label'])}</p>
    <section class="chapter">
{content}
{pager}
    </section>
  </article>
</main>
"""

    label = chapter["label"]
    title = f"{label} · {chapter['title']} · {lang['book_title']}"
    description = f"{label}: {chapter['title']} — {lang['subtitle']}"
    page = (
        head(lang, title, description, chapter["slug"])
        + topbar(lang, chapter["slug"], "index.html#contents", "ch01.html")
        + body
        + footer(lang, chapter["slug"])
    )
    return page


def build_language(lang: dict) -> None:
    chapters = parse_chapters(lang)
    total_value = sum(chapter["value"] for chapter in chapters)
    total_minutes = sum(chapter["minutes"] for chapter in chapters)
    out_dir = ROOT / lang["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    landing = landing_page(lang, chapters, total_value, total_minutes)
    (out_dir / "index.html").write_text(landing, encoding="utf-8")

    for index, chapter in enumerate(chapters):
        page = chapter_page(lang, chapters, index)
        (out_dir / chapter["slug"]).write_text(page, encoding="utf-8")

    # Privacy guard: every page must stay static and self-contained.
    pages = [out_dir / "index.html", *[out_dir / chapter["slug"] for chapter in chapters]]
    for path in pages:
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for token in ("<script", "google-analytics", "googletagmanager", "plausible.io", "umami"):
            if token in lowered:
                raise SystemExit(f"refusing to keep {path} containing {token!r}")
        if lang["lang"] == "en":
            check = text.replace("中文", "")
            found = sorted(set(re.findall(r"[\u4e00-\u9fff]+", check)))
            if found:
                raise SystemExit(f"untranslated Chinese in {path}: {found[:8]}")

    print(
        f"wrote {lang['out_dir']}/index.html + {len(chapters)} chapter pages "
        f"({total_value:,} {lang['count_mode']})"
    )


def main() -> None:
    for lang in LANGUAGES:
        build_language(lang)


if __name__ == "__main__":
    main()
