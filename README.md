**English** | [中文](README.zh.md)

# DeepSeek Harness: A Beginner's Guide

## From Your First Conversation to Your Own Plugin

<p align="center"><img src="docs/cover.webp" alt="DeepSeek Harness: A Beginner&#39;s Guide cover" width="280"></p>

**A practical guide for complete beginners**

> **Read online (English)**: <https://leether.github.io/dsh-book/en/>  
> **Chinese edition**: <https://leether.github.io/dsh-book/>  
> **Unofficial guide**: not affiliated with DeepSeek. DSH / DeepSeek names and trademarks belong to their owners.

Version: 2026-10  
Reference environment: DeepSeek Harness Desktop 0.2.1-rc.2  
Full text: [English edition](en/dsh-book.md) · [Chinese edition](dsh-book.md) · Site builder: [scripts/build-site.py](scripts/build-site.py)  
Case-study plugin: [GetNote Toolbox](https://github.com/leether/getnote-toolbox)  
Cover artwork: generated with Dreamina (即梦), stored locally in `docs/cover.webp`.

---

## Who This Book Is For

- People meeting AI Agents for the first time who want to know how a model differs from a harness;
- People who have used chatbots but have never let an AI read files, run commands, or work on a project;
- People who want to install skills and plugins in DSH but feel blocked by Profile, Bundle, and Preset;
- People who want to build a small plugin in Creator mode but do not know where to start.

The first seven chapters assume no programming background. Chapter 8 introduces plugins; Chapter 9 moves into building one, but still focuses on describing goals and reviewing results.

---

## Before You Start

1. Install **DeepSeek Harness Desktop**;
2. Have a model service ready (DeepSeek's official API or another compatible provider);
3. Create a **dedicated folder for the Agent**; do not point it at your entire disk on day one;
4. Remember: **Agents make mistakes. Back up important files and confirm destructive actions.**

---

## Contents

### Chapter 1 — Meet DSH: Models, Harnesses, and Agents

- Agent = Model + Harness
- What DSH is and is not
- Five core terms: Agent, Session, Workspace, Tool, Skill
- Why a harness is necessary
- Desktop, Web, and Headless entry points

### Chapter 2 — First Launch: Desktop, Model, Workspace

- Open Desktop
- Connect a model and API key
- Choose a workspace
- Choose Standard mode
- A map of the interface
- First conversation: read-only and observable

### Chapter 3 — Your First Task: Say What You Mean

- Four elements: goal, input, constraints, acceptance
- Plan before you execute
- Watch tool calls and file changes
- Iterate and verify
- Deliver files with `present`

### Chapter 4 — Workspaces, Files, and Permissions

- What a workspace really is
- What the Agent can read and write
- `workspace-write` vs. `danger-full-access`
- Destructive actions and backups
- Secrets, passwords, and screenshots
- `AGENTS.md`: project rules

### Chapter 5 — Sessions, Context, and Memory

- What a Session is
- Why the Context Window fills up
- DSH does not automatically remember everything
- New Session vs. continuing
- Files, `AGENTS.md`, and Skills as long-term memory
- Context hygiene

### Chapter 6 — Tools and Skills: The Agent's Hands and Mind

- Tool categories: read, write, execute, search, deliver
- Tool cards and approvals
- Plans, todos, subagents, workflows
- What a Skill is, and how it differs from a Tool or Plugin
- Choosing and using Skills
- What `present` means

### Chapter 7 — Modes and Presets: Same Model, Different Ways to Work

- A Preset is a capability composition, not a model
- Standard mode
- Creator mode
- PTC mode
- Minimal mode
- How to choose
- The right way to customize a Preset

### Chapter 8 — Plugins, Bundles, and Profiles: Giving DSH New Powers

- A Plugin is a runtime capability
- A Bundle is an installer package
- A Profile is an installation environment
- How all three relate to Presets
- Installing, enabling, and removing with Plugin Manager
- The trust boundary of third-party plugins
- Common failures

### Chapter 9 — Creator Mode: From User to Extender

- What Creator mode is
- What it adds
- When to use it, and when not to
- A complete plugin-building loop
- Safety: code runs in the Host process
- How non-programmers can participate
- Case study: turning the GetNote CLI into a public DSH plugin

### Chapter 10 — Troubleshooting, Safety, and Next Steps

- A table of common problems
- Reading diagnostics
- Safety checklist
- Cost and usage
- A practice path
- One-page cheat sheet

### Appendix

- Glossary
- Ten reusable prompt templates
- Before-you-start checklist
- Task-completion checklist
- One-page cheat sheet

---

## Reading Paths

| You are | Read |
| --- | --- |
| An everyday user | Chapters 1–7 |
| Installing plugins and skills | Chapters 1–8 |
| Building a plugin | Chapters 1–9 |
| Troubleshooting | Chapter 10, then the relevant chapter |

---

## Read Online and Repository

- **English site**: <https://leether.github.io/dsh-book/en/>
- **Chinese site**: <https://leether.github.io/dsh-book/>
- **Repository**: <https://github.com/leether/dsh-book>
- **Issues**: <https://github.com/leether/dsh-book/issues>

The site is split into per-chapter pages:

```text
/                     cover + contents
/ch01.html … /ch10.html
/appendix.html
/en/                  English cover + contents
/en/ch01.html … /en/ch10.html
/en/appendix.html
```

GitHub Pages serves `main` / `docs` as static HTML. There is no build service.

To update the site:

```bash
cat 00-front.md part1.md part2.md part3.md part4.md > dsh-book.md
cat en/00-front.md en/part1.md en/part2.md en/part3.md en/part4.md > en/dsh-book.md
python3 -m pip install -r requirements.txt
python3 scripts/build-site.py
git add dsh-book.md en/dsh-book.md docs
git commit -m "docs: refresh site"
git push
```

Pages updates within a minute or two.

---

## Site Design

- **Per-chapter pages**: shorter pages, clearer navigation, and a chapter-specific URL;
- **Bilingual switch**: `English / 中文` in the top-right corner; the current chapter is preserved;
- **Cover page**: hero, book cover, chapter cards, and reading paths;
- **Desktop sidebar**: chapter navigation stays visible and highlights the current chapter;
- **Mobile single column**: contents, article, and chapter navigation stack;
- **Reading rhythm**: minutes, word count, and section count per chapter;
- **Chapter navigation**: previous/next at the end of every chapter;
- **CSS-only reading progress**: shown in browsers that support scroll-driven animations;
- **Light/dark theme**: follows `prefers-color-scheme`;
- **Print styles**: hide navigation and paginate by chapter.

No JavaScript, cookies, analytics, external fonts, or third-party asset requests are used.

---

## Repository Layout

```text
.
├── README.md              # this English README (default)
├── README.zh.md           # Chinese README
├── dsh-book.md            # Chinese full text
├── 00-front.md            # Chinese title page
├── part1.md … part4.md    # Chinese chapter sources
├── en/
│   ├── 00-front.md        # English title page
│   ├── part1.md … part4.md
│   └── dsh-book.md        # English full text
├── scripts/build-site.py  # Markdown → bilingual static site
├── docs/                  # GitHub Pages (main /docs)
│   ├── index.html         # Chinese cover
│   ├── ch01.html … ch10.html
│   ├── appendix.html
│   ├── en/index.html      # English cover
│   ├── en/ch01.html … en/appendix.html
│   ├── style.css
│   ├── favicon.svg
│   └── .nojekyll
├── PUBLISHING.md          # release / Pages notes (Chinese)
├── CONTRIBUTING.md        # contribution notes (Chinese)
├── requirements.txt
├── NOTICE.md              # copyright and license scope
├── LICENSE                # CC BY-NC-ND 4.0 (book text)
└── LICENSE-CODE           # MIT (code examples)
```

`dsh-book.md` is `00-front.md` + `part1.md` … `part4.md`.  
The English edition is the same combination under `en/`.  
The English text was edited for natural English usage rather than translated word-for-word; native-speaker corrections are welcome.

---

## Privacy and Public Notes

This repository is public:

- It contains **no** real API keys, passwords, tokens, private files, personal notes, or local absolute paths;
- Project names, file names, and conversation examples in the book are fictional;
- Both the Chinese and English sites are **static HTML**: no JavaScript, cookies, analytics, external fonts, or CDN requests;
- Pages link only to the GitHub repository and to Pages itself;
- This is an **unofficial** learning resource, not DeepSeek documentation or a product promise;
- DSH / DeepSeek names and trademarks belong to their owners;
- UI labels and version behavior may change; use the actual product as the source of truth.

> If you quote this book, keep the source and license. If you find an error, open an issue.

---

## Contributing

Corrections, clearer examples, and English-language improvements are welcome.

- Open an issue with the chapter, your DSH version and platform, the observed behavior, and the expected correction;
- Do not paste API keys, tokens, passwords, private files, customer data, or local absolute paths;
- For source edits, change `part*.md` or `en/part*.md`, rebuild both books, then run `scripts/build-site.py`;
- Do not hand-edit `docs/*.html`; they are generated;
- Do not copy unlicensed images, fonts, or long copyrighted excerpts;
- Keep the "unofficial" framing.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full notes (Chinese).

---

## License

**Book text:** [CC BY-NC-ND 4.0](LICENSE)  
**Code examples:** [MIT](LICENSE-CODE)  
**Scope and commercial licensing:** [NOTICE.md](NOTICE.md)

You may read, share, and redistribute the book text verbatim for noncommercial purposes with attribution. You may not use the text commercially, and you may not publish modified, abridged, or translated versions without written permission. Commercial publication rights are reserved by the copyright holder; for a commercial license, open an issue.

The DSH / DeepSeek names and trademarks are not granted by these licenses.
