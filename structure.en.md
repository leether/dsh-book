## Four parts

The book is organized by object of study:

- **Part I — Getting Started**: using DSH;
- **Part II — Plugin Design**: designing plugins on DSH;
- **Part III — DSH Internals**: designing DSH itself;
- **Part IV — Decisions**: why we designed things this way.

---

## Part I — Getting Started: Using DSH

**Status: Published · 10 chapters + appendix**

This is the entry point. The goal is not to explain all of DSH, but to help you complete a first real task safely: choose a workspace, connect a model, state the request, watch tool calls, and verify the result.

**After this part, you can**

- Complete a read → process → write task on your own;
- Explain what the workspace, permissions, Session, Tool, and Skill each control;
- Know where to look when something fails, instead of reinstalling blindly.

| Chapter | Topic | Status |
| --- | --- | --- |
| 1 | Meet DSH: Models, Harnesses, and Agents | Published |
| 2 | First Launch: Desktop, Model, Workspace | Published |
| 3 | Your First Task: Say What You Mean | Published |
| 4 | Workspaces, Files, and Permissions | Published |
| 5 | Sessions, Context, and Memory | Published |
| 6 | Tools and Skills: The Agent's Hands and Mind | Published |
| 7 | Modes and Presets: Same Model, Different Ways to Work | Published |
| 8 | Plugins, Bundles, and Profiles: Giving DSH New Powers | Published |
| 9 | Creator Mode: From User to Extender | Published |
| 10 | Troubleshooting, Safety, and Next Steps | Published |
| Appendix | Glossary, prompt templates, checklists, cheat sheet | Published |

[Enter Part I →](index.html#contents)

---

<a id="advanced"></a>

## Part II — Plugin Design

**Status: Planned · plugin design first**

This part is about turning a capability into a reliable DSH plugin. The focus is not an API catalogue, but contracts, boundaries, testing, and release.

**Questions this part will answer**

- When does a capability deserve a Tool, and when should it stay in the CLI or a Skill?
- How should arguments, results, errors, and side effects be designed?
- How should deletion, overwrite, permissions, and confirmation work?
- How do you test with a fake CLI and accept with the real one?
- How do you package and release a plugin without losing version control?

| Chapter | Topic | Status |
| --- | --- | --- |
| II.1 | Plugin design: from workflow to tool contract | Planned |
| II.2 | The tool surface: arguments, results, errors | Planned |
| II.3 | Permissions, confirmation, and destructive actions | Planned |
| II.4 | Config, secrets, and observability | Planned |
| II.5 | Testing: fake CLI, fixtures, and evals | Planned |
| II.6 | Version compatibility, packaging, and release | Planned |
| II.7 | Case study: the GetNote Toolbox design review | Planned |
| II.8 | Anti-patterns and a plugin review checklist | Planned |
| II.9 | Open questions: MCP, UI plugins, memory plugins | Placeholder |

> This part will grow as we build more plugins, hit more failures, and write more reviews. Unverified material will be marked as such.

---

<a id="internals"></a>

## Part III — DSH Internals

**Status: Researching · to be verified**

This part moves from “using plugins” to “understanding DSH itself”: the runtime, plugin lifecycle, services, context, tool execution, permissions, UI, and release.

**Questions this part will answer**

- What problems do Agent, Preset, Plugin, Bundle, and Profile each solve?
- What layers does a request pass through before a tool runs?
- How are tool permissions, sandboxing, and cancellation implemented?
- How are Session, Context, Skills, and UI slots organized?
- Which designs are stable contracts, and which are current implementation details?

| Chapter | Topic | Status |
| --- | --- | --- |
| III.1 | DSH layers: Agent / Preset / Plugin / Bundle / Profile | Planned |
| III.2 | The Cordis runtime and plugin lifecycle | To verify |
| III.3 | Services, Context, and Events | To verify |
| III.4 | Tool execution, permissions, and sandboxing | To verify |
| III.5 | Session and Context management | Planned |
| III.6 | Skill loading and routing | Planned |
| III.7 | Desktop, Web, and Headless differences | Planned |
| III.8 | Release, upgrade, and compatibility | Planned |

> DSH is still evolving. This part will separate confirmed behavior, inference, and open questions instead of presenting implementation details as permanent truth.

---

<a id="decisions"></a>

## Part IV — Decisions

**Status: Companion · continuously updated**

This part is not ordered by difficulty, and it does not need to be read first. It records the judgments behind DSH, our plugins, and this book.

Each entry aims to read like a decision record:

- What problem were we facing?
- What options did we have?
- What did we choose?
- What did it cost?
- What would make us revisit the decision?

| Chapter | Topic | Status |
| --- | --- | --- |
| IV.1 | Why we built a Desktop version of the GetNote plugin | Published (case study) |
| IV.2 | Why the Tool surface is not a 1:1 CLI mapping | Planned |
| IV.3 | Why deletion requires confirmation | Planned |
| IV.4 | Why the book is CC BY-NC-ND and the code is MIT | Published (notice) |
| IV.5 | Why official and independent plugins can conflict | Planned |
| IV.6 | How to tell whether a plugin is actually better | Planned |
| IV.7 | The human role: judgment, acceptance, responsibility | Planned |

> You can read this part out of order, or return to it when a chapter asks “why was this designed this way?”

---

## Updates

1. Unwritten material appears only on this roadmap, not as blank chapter pages.
2. Mark every chapter's status; revisit conclusions when DSH changes.
3. Keep published chapter URLs stable; new material gets new paths.

---

## How to read now

- **New to DSH**: start with Part I, Chapter 1.
- **Preparing to build a plugin**: finish Part I, then read the contract, permission, and testing chapters in Part II.
- **Curious about internals**: read Part II first, then Part III.
- **Looking for a decision**: open Part IV at any time; no sequence required.

The structure will keep growing, but we will not pretend it is complete before it is.
