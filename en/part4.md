# Chapter 9 — Creator Mode: From User to Extender

## What You Will Learn

- What Creator mode is and is not;
- What it adds beyond Standard;
- When to use it, and when not to;
- A complete plugin-building loop;
- How non-programmers can participate;
- How to avoid breaking DSH.

---

## 9.1 What Creator Mode Is

Creator mode is an **Agent Preset** in DSH. Its internal id is `cordis`.[[3]](#ref3)

It is not:

- Another model;
- Another runtime;
- Another app;
- "Standard but smarter."

It is:

> **A working mode that adds runtime inspection, plugin management, and plugin/Preset authoring guidance on top of the standard task tools.**

It shares with Standard:

- The same Agent loop;
- The same model;
- The same sandbox and permission system;
- Most task tools.

Only the composition differs.

---

## 9.2 What It Adds

Usually three groups.

### 1. Runtime inspection

It can inspect the real, current:

- Service methods;
- Config schemas;
- Tool schemas;
- Skill list;
- UI slots and theme tokens.

This removes guessing: you do not have to infer APIs from source code.

### 2. Plugin management

It can:

- List installed Bundles;
- Install, enable, disable, and remove;
- Change the profile's plugin selection;
- Read installation results and warnings.

These changes persist in the profile, affect all Sessions, and survive restarts.

### 3. Authoring guidance

Creator mounts authoring Skills that explain:

- How to write a Cordis plugin;
- How to write a Bundle patch;
- How to create or override a Preset;
- How to verify that the plugin actually loaded.

It provides templates and references on demand.

---

## 9.3 When to Use It

Use it for:

- Adding a tool to DSH;
- Adding a UI panel or button;
- Building a custom mode;
- Debugging why a plugin did not load;
- Packaging a workflow as a plugin.

Do not use it for:

- Everyday coding;
- Routine file work;
- Just asking for research;
- Anything that does not extend DSH.

Why not? The extra tools and Skills consume context, and plugin installation is a high-risk operation.

---

## 9.4 Security Boundary: A High-Trust Mode

Creator can do things Standard cannot because:

- Installing a plugin executes code in the Host process;
- Profile changes affect every Session;
- Plugins may read files, access the network, and run commands;
- That code runs outside the workspace sandbox.

Therefore:

- Plugin management usually requires **full access or per-call approval**;
- Do not give an untrusted plugin full access;
- Test in a scratch profile/workspace first;
- Back up important configuration;
- Make sure you can disable or roll back.

> Creator mode is not a "safe mode." It is a high-trust extension mode.

---

## 9.5 A Complete "Build a Plugin" Loop

This flow does not require you to write code, but it does require you to describe the goal and verify the result.

### Step 1: Describe the capability

Do not start with "write me a plugin." Start with:

```text
I want to add this capability to DSH:
- What it does;
- Where it is used (chat / button / panel / tool);
- Inputs;
- Outputs;
- How to verify success;
- What it should not do.
```

### Step 2: Ask it to inspect first

```text
Do not write code yet.
Use runtime inspection to determine:
1. Which layer this belongs to (Host plugin / Preset plugin / pure config);
2. The available Service / Slot / Tool APIs;
3. Whether a new Bundle is needed;
4. Whether a template exists.
List the conclusions and risks.
```

### Step 3: Build the smallest version

```text
Build a minimal working version.
No extra features, no variants.
Give me the file list, installation steps, and verification steps.
```

### Step 4: Install and verify

```text
Install it into the current profile.
After installation, tell me:
- The installation result (applied / warnings);
- Which tools, Skills, or UI were added;
- How to verify;
- How to uninstall.
```

### Step 5: Fix and iterate

Fix only the observed problems. Do not keep adding features.

### Step 6: Close out

```text
Give me:
- Plugin location;
- Install/uninstall steps;
- What was verified;
- What was not verified;
- Known limitations.
```

---

## 9.6 How Non-Programmers Can Participate

You do not have to write the code, but you should:

1. **Describe the goal**: user, scenario, inputs, outputs;
2. **Review the result**: did it do more than asked? Are permissions too broad?
3. **Accept**: run your scenario; give specific feedback.

Ask for:

```text
Do not just tell me "done".
Give me:
- Which files changed;
- Which capabilities were added;
- How I can verify manually;
- How to roll back if it fails.
```

---

## 9.7 Case Study: Turning the GetNote CLI into a DSH Plugin

The previous sections described the method. This section walks through a real project: the **GetNote Toolbox**.

The direct motivation was simple: **when we started, the official `@getnote/dsh-plugin` did not support DSH Desktop**.[[2]](#ref2) Desktop is the entry point most people use every day, so we needed a version that actually worked in a local Desktop profile.

This was not an attempt to replace the official plugin. It was meant to fill the Desktop gap. That is also why the project focuses on the Desktop local bundle, locale/icon display, CLI discovery, and visibility in Plugin Manager.

The goal was not to copy another plugin's tool list. It was to turn the local `getnote` CLI into a set of Host tools that an Agent can use reliably. The source is public:

<https://github.com/leether/getnote-toolbox>

The source is public, and the package is published on npm as `@leether/getnote-toolbox`.[[1]](#ref1)

- GitHub: <https://github.com/leether/getnote-toolbox>
- npm: <https://www.npmjs.com/package/@leether/getnote-toolbox>

Install the npm bundle through DSH Plugin Manager, or link the source locally while developing.

### Step 1: Audit capabilities before writing tools

Start with the CLI's `--help`, inputs and outputs, side effects, authentication, and version differences. Then decide which capabilities deserve to become tools:

- High-frequency operations that need structured arguments or safety guards become Tools;
- Low-frequency, complex, fast-changing, or judgement-heavy operations stay with the CLI or a Skill;
- Reversible operations should exist in pairs, such as add and remove;
- Never add a generic `run_command` or arbitrary HTTP passthrough.

The project ended up with 15 tools covering search, save, read, update, delete, tags, knowledge bases, and quotas. **Fifteen was not the goal.** Every tool had to answer a concrete question: which contract, guard, or normalization does it add?

### Step 2: Turn "it runs" into a contract

The difficult part was not the `spawn` call. It was the details:

- Treat 19-digit note IDs as strings so JSON numbers cannot silently lose precision;
- Some older CLIs ignore `limit`, so the plugin truncates the parsed result itself;
- Deleting a note requires an explicit `confirm: true`; tag deletion requires a tag ID;
- Arguments go to `spawn` as an array, never through a shell;
- Timeouts, output-size limits, and expired logins produce actionable errors;
- A Config schema exposes `binaryPath`, `timeoutMs`, and related fields;
- A bundled Skill tells the Agent when to use which tool.

Only at that point does the plugin stop being a command wrapper and become a usable interface for a model.

### Step 3: Unit-test with a fake CLI, accept with the real one

The test suite does not touch a real account. A fake CLI covers ID precision, nested responses, the old-CLI `-y` fallback, tag re-reads, and knowledge-base add/remove across 28 tests.

Then run a read-only smoke test against the real CLI. Real output can contain note excerpts, so:

- Never paste that output into an issue, chat, or commit;
- Use synthetic IDs in tests;
- For write tests, create a test note first and clean it up afterwards.

### Step 4: Do the privacy and publication review before going public

This is the most important part of the case study. Working code is not the same as code that is safe to publish.

Before publication, we handled:

- **Eval reports**: `evals/results/` contained account-specific note IDs, titles, and comparisons; it must not enter the public repository;
- **Internal drafts**: upstream issue/PR notes under `contrib/` contained local paths and operating plans; they were excluded;
- **Git history**: the old history used a personal email; the public repository starts a fresh history with a noreply author;
- **Package name**: a local username scope was replaced with a public identity scope;
- **Environment details**: lines such as "this machine is already linked to a profile" were removed;
- **Sensitive-data scan**: check for keys, tokens, emails, absolute paths, `.env` files, long numeric IDs, and eval output;
- **File inventory**: keep only reviewed source, tests, licenses, and public documentation.

The rule is simple:

> **Review first, publish second. Do not publish and delete afterwards.**

### Result and boundaries

The plugin is now a public source project with 15 tools and 28 tests, licensed under MIT. It also has clear boundaries:

- It uses the same `getnote_*` tool names as the official `@getnote/dsh-plugin`, so the two cannot be installed together;
- CLI version affects IDs, `limit`, and confirmation flags; pin `binaryPath` and verify the version;
- The `npx` fallback downloads the latest CLI; use a pinned local binary if supply-chain risk matters;
- It is not a universal GetNote plugin; many low-frequency capabilities still belong to the CLI or a domain Skill.

What is reusable here is not the number 15. It is the four-step loop: **audit capabilities, design contracts, test with a fake CLI, and review privacy before publishing.**

---

> Further reading: the Cognition article “From CLI to DSH Plugin: A Decision Guide for Better Agent Work” is published at [cognition.html](cognition.html).

## 9.8 Common Misconceptions

- **"Creator is an advanced Standard."** No; it is an extension mode.
- **"Installing a plugin is just config."** No; it may execute code.
- **"It works immediately."** Not always; a reload or restart may be needed.
- **"A Preset can be a sandbox."** No.
- **"Let the Agent edit profile files directly."** No; use Plugin Manager.
- **"Build everything at once."** Start minimal, then iterate.

---

## Try It

1. Create a Creator task;
2. Do not install anything;
3. Ask it to list the available runtime inspection capabilities;
4. Ask: "If I want to add a read-only tool, which layer should it live in, and why?"
5. Read the answer; do not execute.

---

## Summary

- Creator is the `cordis` Preset, not a model or runtime.
- It adds runtime inspection, plugin management, and authoring guidance.
- Use it to extend DSH, not for daily work.
- Plugin code runs in the Host; have a trust and rollback plan.
- Start minimal, verify, then iterate.
- Real-world case: audit capabilities and contracts, review privacy, then publish.

## References

1. <a id="ref1"></a>[GetNote Toolbox repository](https://github.com/leether/getnote-toolbox)
2. <a id="ref2"></a>[Official GetNote DSH plugin](https://github.com/iswalle/getnote-dsh-plugin)
3. <a id="ref3"></a>[DeepSeek Harness plugin development](https://deepseek-harness.github.io/deepseek-harness/en/develop/basic/)

> All links are public sources; product behavior may change between versions.

---

# Chapter 10 — Troubleshooting, Safety, and Next Steps

## What You Will Learn

- Locate common problems with a table;
- Know where to look for diagnostics;
- Build your own safety checklist;
- Control cost;
- Plan your next practice steps.

---

## 10.1 Common Problems

| Symptom | Check first | Common cause |
| --- | --- | --- |
| Cannot connect to a model | Settings → Models | Wrong key, Base URL, or no credit |
| `401 Invalid API key` | API key | Incomplete, expired, or wrong service |
| Agent does not reply / spins | Model, network, session | Timeout, huge context |
| Agent says it has no tools | Current mode, plugins | Minimal mode, plugin disabled |
| Plugin installed but no tools | Plugin Manager, reload | Not enabled, restart needed, missing dependency |
| Skill does not load | Skill directory, version | Wrong path, description mismatch, conflict |
| File edit denied | Permission/workspace | Outside workspace, sandbox |
| File not found | Workspace, relative path | Wrong current directory, missing file |
| Slower and more expensive over time | Context | Long history, too many files |
| Agent repeats or forgets | Context | Window full, compaction, stale info |
| Tool name conflict | Plugin list | Two plugins registered the same name |
| Version error | Versions | DSH/CLI/plugin mismatch |
| Command hangs | The command | Interactive command, no timeout, network |

---

## 10.2 Reading Diagnostics

### Start with the UI

- Red errors;
- Failed tool cards;
- Plugin Manager warnings;
- Model connection status.

### Then check context

- Is the workspace correct?
- Is the mode correct?
- Is the plugin enabled?
- Is the Session too long?

### Then check logs

Desktop/CLI usually has a log or diagnostics entry. CLI users can run:

```bash
dsh --profile web --dump-config
```

Do not edit profile files until you understand the layer order.

### A general troubleshooting order

```text
1. Minimal reproduction
2. New Session
3. Standard mode
4. Disable the most recently installed plugin
5. Check model/network
6. Check workspace/permissions
7. Read logs/diagnostics
8. Reinstall/roll back only after that
```

---

## 10.3 Safety Checklist

Before an important task:

```text
[ ] Does the workspace contain only what is needed?
[ ] Are important files backed up or committed?
[ ] Can I start read-only?
[ ] Will it delete, overwrite, push, or upload?
[ ] Am I about to expose keys, passwords, or private data?
[ ] Is the plugin source trustworthy?
[ ] Do I really need full access?
[ ] How do I roll back?
```

### Three bottom lines

1. **Secrets never go into chat**;
2. **Back up before destructive actions**;
3. **Do not give untrusted plugins high permissions**.

---

## 10.4 Cost and Usage

Agent cost is mostly tokens:[[2]](#ref2)

- Longer context costs more;
- Large files and long pages cost more;
- Subagents and workflows add model calls;
- Retries add cost.

### Habits that save money

- Read only what is needed;
- Read long documents in sections;
- Summarize to files and start a new Session;
- Do not use subagents when one Agent is enough;
- Choose the right model for the task.

---

## 10.5 Next Steps

### Week 1: Everyday use

- Complete three real tasks in Standard;
- Practice goal + input + constraints + acceptance;
- Learn to read tool cards and approvals.

### Week 2: Workspace and context

- Write an `AGENTS.md`;
- Use `PROJECT.md` and `PROGRESS.md`;
- Practice resuming in a new Session.

### Week 3: Tools and Skills

- Use todos for a multi-step task;
- Try one subagent;
- Read a `SKILL.md`;
- Deliver a file with `present`.

### Week 4: Extension

- Read Chapter 8 and understand Plugin/Bundle/Profile;
- Build one small tool in Creator;
- Install, verify, and uninstall;
- Write your own plugin notes.

---

## 10.6 One-Page Cheat Sheet

```text
Agent = Model + Harness

Everyday work  → Standard
Extending DSH  → Creator
Batch tools    → PTC
Small tasks    → Minimal

Workspace = folder + permission boundary
Session   = one conversation
Context   = working memory; it fills up
Skill     = knowledge/procedure
Tool      = action
Plugin    = runtime capability
Bundle    = installer package
Profile   = installation environment
Preset    = capability composition for one Agent

Good task = goal + input + constraints + acceptance
Read-only first, then write
Plan first, then execute
Back up before destructive actions
Secrets never go into chat
```

---

## Summary

- Troubleshoot from minimal reproduction + new Session + Standard + disable new plugins.
- Three safety rules: secrets, backups, permissions.
- Cost comes from context and model calls.
- Learning path: daily use → workspace → tools/Skills → plugins.
- Use first; extend later. Do not start with a huge plugin.

## References

1. <a id="ref1"></a>[DeepSeek Harness quickstart](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart)
2. <a id="ref2"></a>[DeepSeek API token usage](https://api-docs.deepseek.com/quick_start/token_usage)
3. <a id="ref3"></a>[Git documentation](https://git-scm.com/docs)
4. <a id="ref4"></a>[npm publish documentation](https://docs.npmjs.com/cli/v11/commands/npm-publish)

> All links are public sources; product behavior may change between versions.

---

# Appendix

Tool names and product behavior in this appendix follow the official documentation and the case-study repository.[[1]](#ref1)[[2]](#ref2)[[3]](#ref3)

## A. Glossary

| Term | One-line explanation |
| --- | --- |
| **Agent** | The working assistant: model + harness + current context |
| **Harness** | The Agent's workbench: tools, sessions, permissions, plugins |
| **Model** | The brain: understanding, reasoning, generation |
| **Session** | One continuous conversation |
| **Workspace** | The folder the Agent works in |
| **Context Window** | The maximum text the model can process at once |
| **Compaction** | Compressing context when it fills up |
| **Tool** | An action the Agent can take |
| **Skill** | Knowledge/procedure for how to do something |
| **Preset** | A capability composition for one Agent |
| **Plugin** | A runtime capability extension |
| **Bundle** | An installable package of plugins/configuration |
| **Profile** | An installation environment |
| **Sandbox** | A mechanism limiting file/command access |
| **Approval** | Confirmation before a sensitive action |
| **MCP** | A protocol for connecting external tools/data |
| **PTC** | Programmatic Tool Calling |
| **Creator** | The Preset for extending DSH (internal id `cordis`) |

---

## B. Ten Prompt Templates

### 1. Read-only inventory

```text
Read the current workspace and list files grouped by type.
Do not modify anything or run commands that change files.
At the end, tell me which tools you used.
```

### 2. Plan first

```text
Do not execute yet. Give me a 3–5 step plan:
what each step does, which files it reads/writes, and how to verify.
Wait for my confirmation.
```

### 3. Generate a document

```text
Read [files] and produce [output].
Requirements: [structure/length/language/links].
Do not modify the originals.
After writing, verify the output exists and list the files you read.
```

### 4. Code review

```text
Review this change for bugs, edge cases, and missing tests.
Order findings by severity, with file and line references.
Do not edit code yet; report only.
```

### 5. Debugging

```text
Reproduce the problem, then propose at most three hypotheses.
Test one hypothesis at a time and show evidence.
Do not make broad changes without verification.
```

### 6. Research

```text
Research [topic], preferring primary sources.
Output: conclusions, source links, counterarguments, and open questions.
Do not invent sources.
```

### 7. Data cleanup

```text
Read [input] and convert it to [output format] using [fields].
Do not modify the source data.
Give me the field mapping and cleaning rules first.
```

### 8. Writing

```text
Write a [length] piece on [topic] for [audience], in [tone].
Avoid generic filler; support each claim.
Give me an outline first.
```

### 9. File organization

```text
List the files in [directory] read-only and propose an organization plan.
Do not delete or move anything until I confirm.
Explain where each file goes and why.
```

### 10. Plugin request

```text
I want to add this capability to DSH: [description].
Do not write code yet. Check:
1. Which layer it belongs to;
2. Which APIs/templates are available;
3. What the minimal version is;
4. How to verify and uninstall.
```

---

## C. Before-You-Start Checklist

```text
[ ] Is the goal clear in one sentence?
[ ] Are the input files/folders known?
[ ] Is the output location and format known?
[ ] What is forbidden?
[ ] How will we verify success?
[ ] Do we need a backup or commit?
[ ] Can we start read-only?
[ ] Does it involve secrets or private data?
[ ] Does it require a plugin or elevated permission?
```

---

## D. Task-Completion Checklist

```text
[ ] Does the output file exist?
[ ] Does it meet the requirements?
[ ] Were the originals modified?
[ ] Was any input missed?
[ ] Were any facts or sources invented?
[ ] Is there test/verification evidence?
[ ] Was the final deliverable presented?
[ ] Were temporary files cleaned up?
[ ] Do we know how to roll back?
```

---

## Closing

DSH is not hard to use. The hard part is learning to **control it before it becomes powerful**.

Remember three sentences:

1. **Read-only first, then write.**
2. **Start small, then expand.**
3. **Secrets never go into chat; back up before destructive actions.**

Once those are habits, Presets, Plugins, Bundles, and Creator stop being a pile of nouns. They become a workbench you can compose on demand.

## References

1. <a id="ref1"></a>[DeepSeek Harness official site](https://www.deepseek.com/en/harness/)
2. <a id="ref2"></a>[DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)
3. <a id="ref3"></a>[GetNote Toolbox repository](https://github.com/leether/getnote-toolbox)
4. <a id="ref4"></a>[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

> All links are public sources; product behavior may change between versions.
