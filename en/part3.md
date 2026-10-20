# Chapter 7 — Modes and Presets: Same Model, Different Ways to Work

## What You Will Learn

- Understand that a Preset is neither a model nor a separate app;
- Distinguish Standard, Creator, PTC, and Minimal;
- Choose the right mode for a task;
- Understand how to customize a Preset;
- Avoid treating a mode as a security sandbox.

---

## 7.1 A Useful Metaphor: A Loadout

The same model can work in different ways:

- Everyday coding and file work;
- Extending DSH itself;
- Batch tool calls and data analysis;
- A minimal setup for quick questions.

These ways of working are **Presets**.

Think of a Preset as a character loadout:

```text
Same Agent engine
  + different tools
  + different prompt
  + different Skills
  + different policies
= a different mode
```

It does **not** switch the model, the runtime, or the sandbox. It selects which capabilities this Agent gets.

---

## 7.2 Standard Mode

The everyday default. Good for:

- Coding;
- Reading and writing files;
- Web research;
- Document work;
- Spreadsheets;
- General multi-step tasks.

It usually includes:

- File read/write;
- Terminal;
- Web search/fetch;
- Subagents;
- Plans, todos, goals;
- File delivery;
- Skills.

If you do not know what to choose, choose Standard.

---

## 7.3 Creator Mode

Creator is not "Standard but smarter." It is the mode for **extending DSH itself**.

It usually adds:

- **Runtime inspection**: inspect services, Config, tools, Skills, and UI slots;
- **Plugin management**: install, enable, disable, and remove plugins;
- **Authoring guidance**: Cordis plugins, Bundles, and Presets.

Use it for:

- Building a DSH plugin;
- Adding a tool or UI panel;
- Creating a custom Preset;
- Debugging why a plugin did not load.

Do not use it for:

- Everyday coding;
- Routine file work;
- Tasks that do not extend DSH.

It adds tools and permissions, which cost context and raise risk. Standard is lighter and safer for daily work.

---

## 7.4 PTC Mode

PTC stands for **Programmatic Tool Calling**. It organizes tool calls through code.

Good for:

- Batch tool calls;
- Filtering, deduplicating, and summarizing results;
- Loops, conditions, and composition;
- Data analysis.

It is not automatically faster or cheaper. For everyday work, Standard is fine.

---

## 7.5 Minimal Mode

Minimal keeps only a few tools. Use it for:

- Quick questions;
- Small reads and writes;
- Reducing tool and context noise.

Its capability boundary is narrow. Switch back to Standard for complex work.

---

## 7.6 Which Mode Should I Use?

| Task | Suggestion |
| --- | --- |
| Everyday coding and file work | Standard |
| Building DSH plugins or presets | Creator |
| Batch tool calls and data analysis | PTC |
| Quick questions and small tasks | Minimal |
| Unsure | Standard |

---

## 7.7 What a Preset Actually Is

In DSH, a Preset is a **list of child plugins for one Agent**, plus metadata such as name, description, and order.

It looks roughly like:

```yaml
id: standard
name: Standard
order: 1
plugins:
  - persona
  - tool-bash
  - tool-fs
  - tool-web
  - ...
```

Key points:

- It is declared by the `@deepseek-ai/dsh-agent-preset` plugin;
- It is managed by `agent-preset-registry`;
- Each Session selects one Preset;
- Definitions activate eagerly;
- Edits affect newly created Agents;
- Running Agents keep the revision they started with;
- Subagents usually inherit the parent's Preset.

### It is not

- A model;
- A sandbox;
- A separate process;
- A "more advanced model."

### It is not a security boundary

A Preset can isolate tools and services, but it is **not a security sandbox**.

- Plugin code still runs in the Host process;
- File permissions, approvals, and sandboxing are separate mechanisms;
- Do not assume switching modes removes risk.

---

## 7.8 Custom Presets

You can create modes such as:

- "Code review mode": read-only, report first, do not edit;
- "Writing mode": fixed voice and output structure;
- "Data mode": read data and run analysis only.

The correct path is usually:

1. Describe the mode in Creator;
2. Have the Agent generate a Bundle patch;
3. Install it with Plugin Manager;
4. Select it when creating a new task.

Avoid:

- Hand-editing the legacy `~/.dsh/.agent-presets/` directory;
- Editing the profile's `package.json` directly;
- Copying a built-in Preset and never merging updates.

> A user override replaces the entire child list. New built-in tools will not appear automatically. Review it periodically.

---

## 7.9 Common Misconceptions

- **"Creator is smarter."** No; it has extra tools and knowledge for extending DSH.
- **"Switching Preset changes the model."** No; the model is configured separately.
- **"A Preset is a security sandbox."** No; security comes from permissions and sandboxing.
- **"More Presets is better."** No; each one costs maintenance.
- **"Custom Presets follow built-in updates automatically."** No; override replaces the whole list.

---

## Try It

1. Create a task in Standard;
2. Ask: "Which tools do you have? Which are read-only?"
3. Create another task in Creator;
4. Ask the same question and compare;
5. Do not install or modify anything yet.

---

## Summary

- A Preset is an Agent capability composition, not a model or sandbox.
- Standard is the daily default; Creator is for extending DSH; PTC is for programmatic tool use; Minimal is for small tasks.
- Running Agents keep their starting Preset revision.
- Customize Presets through Bundles and Plugin Manager, not legacy directories.
- A Preset is not a security boundary.

---

# Chapter 8 — Plugins, Bundles, and Profiles: Giving DSH New Powers

## What You Will Learn

- Distinguish Plugin, Bundle, and Profile;
- Understand how a plugin gets installed;
- Use Plugin Manager to install, enable, disable, and remove;
- Understand the trust boundary of third-party plugins;
- Troubleshoot "installed but not working."

---

## 8.1 Three Words, Three Layers

> **Plugin is capability. Bundle is the installer package. Profile is the environment.**

| Term | Think of it as | Answers |
| --- | --- | --- |
| **Plugin** | A pluggable capability module | What runs? |
| **Bundle** | An installable patch package | What configuration and code ship together? |
| **Profile** | An installation environment | Which Bundles are installed here? |

### Plugin

A Plugin is the runtime unit. It can:

- Register tools;
- Register services;
- Register Skills;
- Add UI;
- Listen to events;
- Change Agent behavior.

### Bundle

A Bundle is an npm package that usually contains:

- A `cordis.patch.yml`, or a list of patch files;
- Plugin code;
- Possibly Skills, UI assets, or icons.

It packages "which plugins to add and how to configure them" so a user can install it in one step. Its rows remain patchable by higher layers.

One Bundle can mount many Plugins; one Plugin can be referenced by different Bundles.

### Profile

A Profile is an installation environment:

- `desktop`: the desktop app;
- `web`: the browser;
- `headless`: a one-shot command-line run.

It contains:

- Installed Bundle list;
- Its own `cordis.patch.yml`;
- Third-party plugin dependencies.

The Profile decides what this environment installs; the Bundle decides what the installation contains; the Plugin decides what actually runs.

---

## 8.2 How They Relate to Presets

```text
Profile (desktop)
 ├─ Bundle A (dsh-base)
 ├─ Bundle B (dsh-web-app)
 │    └─ declares Presets: standard / creator / ...
 └─ Bundle C (your plugin)
      └─ mounts Plugin: your tools

Preset (standard / creator)
 └─ selects a set of Plugins for one Agent
```

- A Bundle can declare Presets;
- A Preset chooses which Plugins an Agent gets;
- A Profile chooses which Bundles the environment installs;
- A Plugin is the capability that runs.

---

## 8.3 Installing with Plugin Manager

In Desktop, open the **Plugin Manager** (or Plugins page).

Typical flow:

1. Open the plugin page;
2. Search or select a Bundle;
3. Read the description, permissions, and dependencies;
4. Confirm install;
5. Restart or reload if prompted;
6. Check whether tools, Skills, or UI appeared.

### Before installing

- Is the source trustworthy?
- What permissions does it request?
- Does it depend on an external CLI or service?
- Does it run install scripts?
- Does it conflict with an existing plugin?
- Can it be uninstalled?

### After installing

- Is it enabled?
- Are the new tools present?
- Are the new Skills visible?
- Are there errors or warnings?
- Does it require a restart?

---

## 8.4 Why "Installed but Not Working"

| Symptom | Possible cause |
| --- | --- |
| Listed but no tools | Not enabled; restart required; missing dependency |
| Startup error | Version mismatch; missing peer dependency; bad config |
| Tool name conflict | Another plugin uses the same name |
| Needs login/CLI | External dependency missing or not authenticated |
| Only in some modes | Tool is preset-scoped, not global |
| Code changes do nothing | Server plugin needs a reload; HMR may not apply |

### Troubleshooting order

1. Check Plugin Manager status and errors;
2. Check whether a restart is needed;
3. Check dependencies and versions;
4. Check for conflicts;
5. Check whether the tool is scoped to a Preset;
6. Check logs and diagnostics.

---

## 8.5 Configuring a Plugin

Many plugins expose settings:

- Binary path;
- API URL;
- Timeout;
- Output limit.

DSH plugins usually declare these with a Config schema; Plugin Manager renders a form.

Rules:

- Prefer the UI;
- Do not hand-edit the profile's `package.json`;
- Do not hand-edit `cordis.patch.yml` unless you understand layer order;
- Reload/restart after changes;
- Store secrets safely.

---

## 8.6 The Trust Boundary

This is the most important section.

> **A plugin is not just configuration. It may execute code.**

Installing a third-party plugin means letting someone else's code run inside your DSH process. It may:

- Read files;
- Access the network;
- Execute commands;
- Modify configuration;
- Install dependencies;
- Run install scripts.

Therefore:

- Install only trusted sources;
- Review permissions and code;
- Do not grant unnecessary full access;
- Test in a scratch workspace first;
- Make sure you can uninstall or roll back;
- Do not give secrets to an untrusted plugin.

---

## 8.7 Uninstall and Rollback

Before installing, know how to remove it:

- Can Plugin Manager disable/remove it?
- Does it leave configuration or data?
- Does it change the profile's bundle list?
- Does it require a restart?
- Can you roll back the version?

Back up the profile, or at least record the state before installation.

---

## Try It

1. Open Plugin Manager and inspect the installed Bundles;
2. Find the difference between enabled and disabled;
3. Do not install anything yet; read one plugin's permissions;
4. Pick a plugin you use and see which tools/Skills it registers;
5. Write down how you would disable it if it broke.

---

## Common Pitfalls

- **Confusing Plugin and Bundle**: capability vs. installer package.
- **Assuming a Bundle is enabled after install**: check selection, reload, and dependencies.
- **Hand-editing profile config**: easy to break layer order.
- **Ignoring permissions**: plugins can execute code.
- **Not restarting**: many plugins need a reload.

---

## Summary

- Plugin = capability, Bundle = installer package, Profile = environment.
- A Preset chooses which Plugins an Agent uses.
- Install/enable/remove through Plugin Manager; do not hand-edit the profile.
- Third-party plugins are code, not pure configuration.
- If it does not work, check status, reload, dependencies, conflicts, and Preset scope.

---

## Part III Exercises

1. Explain Plugin, Bundle, and Profile to a friend in one sentence each.
2. Open Plugin Manager and count the enabled Bundles.
3. Read one plugin's permissions and dependencies; decide whether you would install it.
4. Explain why a Preset is not a security sandbox.
5. Write a rollback checklist for a broken plugin.
