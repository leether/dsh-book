# DeepSeek Harness: A Beginner's Guide

## From Your First Conversation to Your Own Plugin

**A practical guide for complete beginners**

Version: 2026-10  
Reference environment: DeepSeek Harness Desktop 0.2.1-rc.2

---

## Before You Start

This English edition was edited for natural English usage rather than translated word-for-word. It is still an unofficial guide; corrections from native readers are welcome.

This book does not assume you can program.

It aims to help you do three things:

1. Actually use DSH for real work, not just chat with it;
2. Understand why it can read files, run commands, and install plugins — and where the boundaries are;
3. Know what Presets, Plugins, Bundles, and Profiles mean when you want to extend it.

The book is Desktop-first. Web and Headless differences appear in small sidebars; the concepts are the same.

---

## Contents

1. Meet DSH: Models, Harnesses, and Agents
2. First Launch: Desktop, Model, Workspace
3. Your First Task: Say What You Mean
4. Workspaces, Files, and Permissions
5. Sessions, Context, and Memory
6. Tools and Skills: The Agent's Hands and Mind
7. Modes and Presets: Same Model, Different Ways to Work
8. Plugins, Bundles, and Profiles: Giving DSH New Powers
9. Creator Mode: From User to Extender
10. Troubleshooting, Safety, and Next Steps

Appendix: glossary, prompt templates, checklists, one-page cheat sheet

---

## Three Reading Paths

- **Everyday use**: Chapters 1–7.
- **Installing plugins and skills**: Chapters 1–8.
- **Building plugins**: Chapters 1–9.
- **Troubleshooting**: jump to Chapter 10.

---

## One Warning

An Agent can take real actions.

Before you let it delete, overwrite, push, or upload anything, make a backup and confirm the scope.

**Never paste secrets into the chat.**
# Chapter 1 — Meet DSH: Models, Harnesses, and Agents

## What You Will Learn

- Explain DSH in one sentence;
- Tell the difference between a model, a harness, and an agent;
- Understand Session, Workspace, Tool, and Skill;
- Choose between Desktop, Web, and Headless.

---

## 1.1 A Useful Formula: Agent = Model + Harness

Start with one formula:

> **Agent = Model + Harness**

| Term | Think of it as | It handles |
| --- | --- | --- |
| **Model** | The brain | Understanding, reasoning, writing, coding |
| **Harness** | Hands, eyes, workbench, rulebook | Files, commands, web access, sessions, permissions |
| **Agent** | The assistant at work | Model + Harness + current context |

A model alone is like a brilliant person locked in a room. It can think and talk, but it cannot see your files or run your programs.

The harness opens the room. It gives the model files, a terminal, a browser, tools, memory, and rules. That is when chatting becomes doing.

DeepSeek Harness, or **DSH**, is that harness.

---

## 1.2 What DSH Is — and Is Not

### It is

- A workbench for running Agents;
- A host that composes models, tools, skills, and plugins;
- A platform with Desktop, Web, and Headless entry points;
- An extensible system where almost everything is a plugin.

### It is not

- **A model.** DSH does not contain the model's brain; you connect a model service.
- **Just a chat app.** Its focus is reading, writing, executing, and delivering.
- **Only for programmers.** Everyday tasks can be done in natural language.
- **Safe by default.** It can take real actions; permissions and review matter.

In one sentence:

> **DSH is the Agent's workbench, not its brain.**

---

## 1.3 Five Words You Will See Everywhere

### Agent

An Agent is not just a model. It combines the model, the current workspace, the current session, available tools, and the current mode.

The same model can behave differently in a different workspace or mode.

### Session

A Session is one continuous conversation.

- Within a Session, the Agent remembers what was said;
- A new Session does not automatically inherit every previous message;
- One workspace can have many Sessions.

Think of a Session as the minutes of one meeting.

### Workspace

A Workspace is a folder. The Agent reads, writes, and runs commands inside it by default.

- It is the project boundary;
- Many permissions are scoped to it;
- Do not start by pointing it at your entire home directory.

### Tool

A Tool is an action the Agent can take:

- Read a file;
- Write a file;
- Edit a file;
- Run a terminal command;
- Search the web;
- Start a subagent;
- Present a deliverable.

Tools are the Agent's hands.

### Skill

A Skill is an instruction manual. It tells the Agent:

- When to use a certain approach;
- What steps to follow;
- What pitfalls to avoid;
- Which references or scripts are available.

A Skill is knowledge. It does not execute actions itself; it helps the Agent use tools reliably.

> Model is the brain, Tool is the hand, Skill is the procedure, Harness is the workbench.

You will meet Preset, Plugin, Bundle, and Profile later. Chapters 7 and 8 cover them.

---

## 1.4 Why a Harness Is Necessary

A model is smart, but real work needs three things a model does not have by itself:

1. **Perception**: seeing files, folders, web pages, and errors;
2. **Action**: writing files, running commands, calling tools;
3. **Constraints**: knowing what is allowed and how to verify the result.

Suppose you say:

> "Combine the three articles in `notes/` into one summary."

The model can write a summary, but it needs the harness to:

- Find `notes/`;
- Read the three files;
- Write `summary.md`;
- Verify that the file exists;
- Stay inside the permissions you granted.

Without a harness, none of those actions happen.

---

## 1.5 Three Entry Points: Desktop, Web, Headless

| Entry point | Best for | What it feels like |
| --- | --- | --- |
| **Desktop** | Almost everyone | A graphical app; easiest to start |
| **Web** | Browser access, remote servers | A web page with a similar interface |
| **Headless** | Automation, scripts, batch jobs | A one-shot command-line run, no GUI |

All three share the same core ideas: Agent, Session, Workspace, Tool, Skill, Preset, and Plugin.

This book is Desktop-first. Web and Headless differences appear in small sidebars.

---

## 1.6 How to Read This Book

- **Everyday user**: Chapters 1–7 cover most needs.
- **Installing plugins and skills**: add Chapter 8.
- **Building plugins**: add Chapter 9.
- **Troubleshooting**: go straight to Chapter 10.

Do not try to memorize every term. Use first; understand later.

---

## Try It

Write down three things you would like an Agent to do. For each, note:

1. Which files it needs to read;
2. Which files it needs to write;
3. Which commands it needs to run;
4. Which actions should ask you first.

If you cannot answer yet, Chapter 3 will help.

---

## Common Pitfalls

- **Treating DSH as a model**: it is a workbench; connect a model separately.
- **Expecting the Agent to remember everything**: memory outside a Session must be designed.
- **Giving it your whole disk on day one**: start with a small folder.

---

## Summary

- Agent = Model + Harness.
- DSH is the harness, not the model.
- Session is a conversation; Workspace is a folder; Tool is an action; Skill is knowledge.
- Desktop is the easiest entry point; Web and Headless are different surfaces, not different products.

---

# Chapter 2 — First Launch: Desktop, Model, Workspace

## What You Will Learn

- Open DSH Desktop;
- Connect a model;
- Choose a safe workspace;
- Complete a read-only first conversation;
- Read tool cards and approval prompts.

---

## 2.1 Open Desktop

After installation, open **DeepSeek Harness**.

The first screen may show:

- A welcome page;
- Model or account setup;
- Workspace selection;
- A new-task input.

The exact order varies by version, but the flow is usually:

```text
Open app → connect a model → choose a workspace → create a task → start talking
```

If you do not have a model service yet, read the next section.

---

## 2.2 Connect a Model

DSH needs a model to think. There are usually two options:

1. **DeepSeek official account/API**: sign in or enter an API key;
2. **An OpenAI-compatible provider**: enter a Base URL, API key, and model name.

The usual path is:

```text
Settings → Models → add or select a provider
```

Prepare:

- Provider;
- API key;
- Model name (for example `deepseek-chat` or `deepseek-flash`, depending on the provider);
- Optional Base URL.

### How to know it worked

- The settings page shows the model as connected;
- A new task gets a reply;
- There is no `401` or `Invalid API key` error.

### Common error: 401

A `401` almost always means **the key is wrong or not active**.

Check:

- The key was copied completely;
- There are no extra spaces;
- The provider and Base URL match;
- The account has credit and permission;
- You did not paste a key from another service.

> **Never paste an API key into the chat for the Agent to inspect.** Change it in Settings.

---

## 2.3 Choose a Workspace

A workspace is the folder where the Agent works.

For your first session:

1. Create an empty folder such as `dsh-test`;
2. Put one or two unimportant text files inside;
3. Select that folder as the workspace.

Why not use your whole home directory?

- The Agent can see too much and may touch the wrong thing;
- Context becomes noisy;
- Rolling back is harder.

Once selected, the workspace is usually the Agent's current directory. Relative paths resolve from there.

---

## 2.4 Choose Standard Mode

When creating a task, DSH usually asks you to choose an **Agent Preset**.

For your first session, choose **Standard**.

Standard mode includes the everyday tools: file read/write, terminal, web search, subagents, planning, todos, and file delivery.

Do not start with **Creator mode**. Creator is for extending DSH itself. It adds plugin management and runtime inspection, along with more risk. Chapter 7 covers the difference.

---

## 2.5 A Map of the Interface

You do not need to know every button, but you should know where four kinds of information appear:

| Area | What you will see |
| --- | --- |
| **Conversation** | Your task, the Agent's replies, questions, and explanations |
| **Tool cards** | What the Agent actually did: read, run, write |
| **Approval prompts** | Requests to allow or deny sensitive actions |
| **Sidebar/settings** | Sessions, workspace, model, plugins, skills, modes |

The most important habit:

> **Do not read only the final paragraph. Read what the Agent did in between.**

Tool cards show which files it read, which commands it ran, and what it changed.

---

## 2.6 Your First Conversation: Read-Only

Do not change files on the first try. Start with two read-only exercises.

### Exercise 1: Introduce itself

```text
Hello. In three sentences, tell me what you can and cannot do.
Do not read or modify any files yet.
```

Check whether it:

- Describes itself as an Agent;
- Mentions workspace and permissions;
- Does not call tools without being asked.

### Exercise 2: Read-only inventory

```text
Read the current workspace and list its files grouped by type.
Do not modify anything, and do not run commands that change files.
At the end, tell me which tools you used.
```

You should see tool cards such as:

```text
list directory
read file
```

If it tries to write, deny it and say:

```text
This step is read-only. Do not write anything.
```

---

## 2.7 The Goal of the First Conversation

It is not to finish a big task. It is to learn three things:

1. **Where it works**: the workspace;
2. **How it works**: tool calls;
3. **How you control it**: approvals, denials, and follow-up instructions.

---

## Sidebar: Web and Headless

- **Web**: usually started with `dsh --profile web`; open the printed URL in a browser. The interface is similar; useful on a remote server.
- **Headless**: run `dsh --profile headless "your task"` for one-shot execution. No GUI; useful for automation.
- **Desktop**: the desktop app owns the `desktop` profile. Do not hand-edit that profile.

This book stays Desktop-first.

---

## Common Pitfalls

- **Starting without a model**: you will only get errors.
- **Choosing too large a workspace**: start small.
- **Choosing Creator for everyday work**: use Standard.
- **Pasting keys into chat**: use Settings.
- **Reading only the final answer**: tool calls tell the real story.

---

## Summary

- Flow: open app → connect model → choose workspace → choose Standard → start.
- A `401` usually means a key problem.
- Keep the workspace small and reversible.
- Start read-only; watch tool cards.
- Standard is the daily default; Creator is a different job.

---

# Chapter 3 — Your First Task: Say What You Mean

## What You Will Learn

- Describe a task with four elements: goal, input, constraints, acceptance;
- Ask for a plan before execution;
- Inspect tool calls and file changes;
- Give useful feedback;
- Use `present` to deliver a file.

---

## 3.1 Four Elements of a Good Task

Most "the Agent is bad at this" experiences come from vague requests.

A good task contains:

| Element | Question it answers | Example |
| --- | --- | --- |
| **Goal** | What should exist at the end? | A `summary.md` file |
| **Input** | Where does the material come from? | Three files under `notes/` |
| **Constraints** | What must not happen? | Do not modify originals; Chinese; keep links |
| **Acceptance** | How do we know it is done? | All three titles; 3–5 sentences each; opens correctly |

### Bad

```text
Organize my notes.
```

### Better

```text
Read the three Markdown files under notes/ and combine them into notes/summary.md.
Requirements:
1. Keep each original title and source link;
2. Write 3–5 sentences per article;
3. Do not modify the original files;
4. Give me a plan first, then wait for my confirmation;
5. After writing, verify that summary.md exists and tell me which files you read.
```

The difference is not length. It is **completeness**.

---

## 3.2 Plan Before You Execute

For anything beyond a trivial task, ask for a plan:

```text
Do not change files yet. Give me a 3–5 step plan:
what you will read, what you will write, and how you will verify the result.
```

Check whether the plan:

- Covers every input;
- States the output location;
- Includes verification;
- Does not quietly expand the scope.

If the plan is wrong, fix the plan first.

---

## 3.3 Watch the Tool Calls

While the Agent works, inspect the tool cards:

| Tool | What to check |
| --- | --- |
| Read file | Is it the right file? |
| Write file | Where did it write? Did it overwrite? |
| Run command | Is it destructive? |
| Web search | Are the sources credible? |
| Subagent | What was delegated? |

A useful habit:

> **When you see write, delete, overwrite, reset, push, or upload, pause.**

---

## 3.4 Iterate with Specific Feedback

First drafts are rarely perfect. Good feedback is specific.

### Vague

```text
Not good. Rewrite it.
```

### Specific

```text
The second paragraph is too long. Cut it to three sentences.
Keep the three subheadings.
Move each source link to the end of its paragraph.
Do not change the other paragraphs.
```

Specific feedback = location + problem + standard.

---

## 3.5 Verify — Do Not Trust "done"

"Done" is not the same as "correct." Check:

- Does the file exist?
- Does the content meet the requirements?
- Were the originals modified?
- Do the links work?
- Was any input missed?
- Did it invent facts?

Ask for evidence:

```text
List the files you actually read, the files you wrote, and the checks you ran.
Do not just say "done".
```

---

## 3.6 Delivering a File: What `present` Means

When the output is a file, the Agent may call `present`.

`present` means:

> **Declare an existing file as a final deliverable so the interface can show a file card that opens the current file.**

It does not:

- Create the file;
- Upload the file;
- Copy the file contents;
- Put the contents into the model context.

It records paths and optional descriptions.

---

## 3.7 A Complete First Task

### Prepare

Create:

```text
notes/
  a.md
  b.md
  c.md
```

### Ask

```text
Read the three articles under notes/ and combine them into notes/summary.md.
Requirements:
1. Keep each title and source link;
2. Write 3–5 sentences per article;
3. Do not modify the originals;
4. Give me a plan first;
5. After writing, verify that summary.md exists and tell me which files you read.
```

### Review the plan

Make sure it covers all three inputs and does not modify originals.

### Approve and watch

You should see three reads and one write.

### Verify

Open `summary.md`; check titles, links, and length.

### Iterate

If the second summary is too short:

```text
Expand the second summary to four sentences, keep its link, and leave everything else unchanged.
```

---

## Common Pitfalls

- **Task too large**: do one verifiable thing at a time.
- **No acceptance criteria**: the Agent cannot know what "good" means.
- **Ignoring tool calls**: it may edit the wrong file.
- **Saying only "rewrite"**: give location and standard.
- **Treating "done" as "correct"**: ask for evidence.

---

## Summary

- A good task = goal + input + constraints + acceptance.
- Plan before executing.
- Watch write, delete, and command calls.
- Feedback must be specific; verification must be evidence-based.
- `present` is a delivery declaration, not an upload.

---

## Part I Exercises

1. Rewrite a recent request using goal + input + constraints + acceptance.
2. In a test folder, ask the Agent to list files read-only and report the tools it used.
3. Ask it to produce `summary.md`, then check whether the originals changed.
4. Give one specific revision instruction instead of "redo it".
# Chapter 4 — Workspaces, Files, and Permissions

## What You Will Learn

- Why the workspace is a safety boundary;
- What the Agent can read and write;
- The difference between `workspace-write` and `danger-full-access`;
- How to avoid deletion, overwriting, and secret leaks;
- How to use `AGENTS.md` to set project rules.

---

## 4.1 What a Workspace Really Is

A workspace is a folder.

The Agent's current directory is usually that folder. When you say "read `notes/a.md`", it looks for `notes/a.md` inside the workspace.

A workspace does three jobs:

1. **Scope**: the Agent works here by default;
2. **Context**: files and instructions here shape its decisions;
3. **Permission boundary**: many safety policies are scoped to it.

So a workspace is not "just any folder". It is the boundary you draw around the Agent's work.

### Recommendations

- One project, one workspace;
- Do not include your entire home directory;
- Use `git init` for important projects;
- Use a scratch folder such as `dsh-test` for experiments.

---

## 4.2 What the Agent Can Read and Write

The Agent acts through tools:

| Tool | What it does | Risk |
| --- | --- | --- |
| Read file | View content | Low, but it may read sensitive data |
| List/search | Find files | Low |
| Write file | Create or overwrite | High: may overwrite originals |
| Edit file | Replace a section | Medium: may edit the wrong place |
| Run command | Execute programs | Very high: delete, reset, upload |

Reading is not automatically safe. If the workspace contains `.env`, keys, or customer data, the Agent may read it, put it into context, or repeat it.

### Least privilege

- Give it only the folder needed for the task;
- Do not hand it your whole home or repository root;
- For sensitive data, redact or copy into an isolated folder first.

---

## 4.3 Two Common Permission Modes

### `workspace-write`

- Read and write inside the workspace;
- Outside the workspace, usually read-only or approval-required;
- The right default for most daily tasks.

### `danger-full-access`

- Broader access;
- Higher-risk operations;
- Use only when you know exactly what you are doing, such as installing plugins or system-level debugging.

**Do not leave full access on just because it is convenient.** More permission means a larger blast radius.

### Approval prompts

When the Agent wants a sensitive action, DSH may ask:

```text
Allow this operation?
```

You can:

- **Allow once**;
- **Deny**;
- **Stop the task**.

When you see delete, overwrite, reset, push, upload, or install, read the details before clicking.

---

## 4.4 Destructive Operations: Back Up First

Possible dangerous actions:

- Delete files or directories;
- Overwrite existing files;
- `git reset --hard`;
- `git push --force`;
- Modify system configuration;
- Install or uninstall software;
- Upload files to an external service.

### Three rules

1. **Back up important files**;
2. **Use git when possible**: commit before the Agent changes things;
3. **Ask for the impact and rollback plan** before approving.

```text
Before deleting or overwriting anything, list the affected files and tell me how to roll back.
Do not execute until I confirm.
```

### Git is your undo button

```bash
git add -A
git commit -m "before agent changes"
```

If the Agent breaks something:

```bash
git diff
git restore .
```

Do not let an Agent make broad changes to important files without version control.

---

## 4.5 Secrets, Passwords, and Screenshots

This is where most accidents happen.

### Do not

- Paste API keys, passwords, or tokens into chat;
- Copy `.env` contents to the Agent;
- Let it upload files containing secrets;
- Show it screenshots containing keys.

### Do

- Keep secrets in environment variables or a secret manager;
- Let the Agent change variable *names*, not values;
- Show redacted examples;
- If a secret was exposed, stop and rotate it.

> The Agent's context may be logged, replayed, or displayed. **Treat anything pasted into chat as leaked.**

---

## 4.6 `AGENTS.md`: Project Rules

`AGENTS.md` is a project instruction file. The Agent reads it and tries to follow it.

Example:

```markdown
# Project Rules

- Reply in English.
- Do not modify `dist/` or `node_modules/`.
- Read related files before changing code.
- Run `pnpm test` before committing.
- Ask me before deleting any file.
- Do not read `.env`.
```

Use it for:

- Code style;
- Directory rules;
- Forbidden actions;
- Test commands;
- Delivery format;
- Team conventions.

`AGENTS.md` is guidance, not a hard sandbox. It reduces mistakes but does not replace permission controls.

---

## 4.7 Workspace Hygiene

- One task per folder;
- Keep inputs, outputs, and temporary files separate;
- Delete temporary files when done;
- Do not mix test data with personal data;
- Confirm before reading very large files.

---

## Try It

1. Create a `dsh-test` workspace;
2. Add an `AGENTS.md` with three rules;
3. Ask the Agent to read it and repeat what it will follow;
4. Ask it to modify a file and observe the approval prompt;
5. Deny once and see whether it stops.

---

## Common Pitfalls

- **Workspace too broad**: larger blast radius.
- **Permanent full access**: risk accumulates.
- **No backup before delete/change**: no rollback.
- **Pasting keys into chat**: immediate leak.
- **Treating `AGENTS.md` as a sandbox**: it is guidance only.

---

## Summary

- Workspace = scope + context + permission boundary.
- Reading can be risky; keep secrets out of chat.
- `workspace-write` is the daily default; `danger-full-access` requires restraint.
- Back up and confirm before destructive operations.
- `AGENTS.md` sets rules but does not enforce them by itself.

---

# Chapter 5 — Sessions, Context, and Memory

## What You Will Learn

- Understand Session and Context Window;
- Know why the Agent forgets;
- Separate in-session memory from cross-session memory;
- Use files, `AGENTS.md`, and Skills as long-term memory;
- Manage context so the conversation does not become slow or expensive.

---

## 5.1 What a Session Is

A Session is one continuous conversation.

Within a Session:

- Your messages, the Agent's replies, and tool results form a history;
- The Agent can refer to earlier content;
- The history is not infinite.

A new Session usually does not inherit the full chat history. It may read the workspace, `AGENTS.md`, and available Skills, but it starts a new meeting.

Think of a Session as one meeting. A new meeting does not remember every sentence unless you leave notes.

---

## 5.2 Context Window: The Agent's Working Memory

A model can process only a limited amount of text at once. That limit is the **Context Window**.

Context includes:

- System prompt;
- Tool definitions;
- Skill content;
- Your messages;
- Previous replies;
- Tool results;
- File contents that were read.

When the context fills up:

- Responses slow down;
- Cost rises;
- Early information is forgotten;
- Compaction or truncation may occur;
- The Agent may confidently continue with incomplete information.

### Warning signs

- It repeats questions;
- It cites the wrong file;
- It forgets a rule you set;
- Replies become long and unfocused.

---

## 5.3 DSH Does Not Automatically Remember Everything

This is the most common beginner misconception.

DSH keeps a session log, but that is not the same as cross-session long-term memory.

- Within a Session: it remembers the chat;
- A new Session: it usually does not remember every previous message;
- It may read workspace files, `AGENTS.md`, or Skills;
- If you install a memory plugin, you may get extra cross-session recall.

Important information should be written to files:

- Project background → `PROJECT.md`;
- Rules → `AGENTS.md`;
- Progress → `TODO.md` or a task list;
- Decisions → `DECISIONS.md`;
- Deliverables → output files.

> **If a file can remember it, do not rely on the chat to remember it.**

---

## 5.4 New Session vs. Continue

| Situation | Recommendation |
| --- | --- |
| A completely new task | New Session |
| Continuing the same task | Continue the current Session |
| The Session is long and confused | Summarize to a file, then start a new one |
| A different project | Change workspace and start a new Session |
| A quick independent question | New Session, to avoid polluting context |

### For long tasks

1. Ask the Agent to write progress to `PROGRESS.md`;
2. List done / not done / next;
3. Start a new Session;
4. Ask it to read `PROGRESS.md` and `AGENTS.md` first.

This is more reliable than stretching one Session forever.

---

## 5.5 Use Files as Long-Term Memory

A simple structure:

```text
project/
  AGENTS.md        # rules
  PROJECT.md       # background
  DECISIONS.md     # key decisions
  PROGRESS.md      # progress
  TODO.md          # tasks
  notes/           # source material
  output/          # deliverables
```

At the start of a new Session:

```text
Read AGENTS.md, PROJECT.md, and PROGRESS.md first.
Then summarize the current state in three sentences.
Do not modify anything before that summary.
```

Now the Agent does not need to remember the entire chat.

---

## 5.6 Context Hygiene

- Do not read large amounts of unrelated material;
- Search first, then read only what is needed;
- Read long documents in sections;
- Ask for summaries when tool output is large;
- Write conclusions into files;
- Do not mix unrelated tasks in one Session.

Useful prompt:

```text
Read only the three files most relevant to the task.
If you need more, explain why first.
Do not read the entire directory at once.
```

---

## 5.7 Memory Plugins Are Not Magic

Some plugins provide cross-session memory:

- Extract facts automatically;
- Store them locally or in the cloud;
- Recall them in later conversations.

They are useful, but:

- They can recall the wrong thing;
- They can treat old information as current;
- They add context and cost;
- They require privacy and permission review.

For beginners, start with files and `AGENTS.md`. Add a memory plugin only when you have a clear need.

---

## Try It

1. Ask the Agent to write `PROJECT.md` with the current goal and constraints;
2. Start a new Session;
3. Ask it to read `PROJECT.md` and restate the goal;
4. Observe whether it can continue without the old chat history.

---

## Common Pitfalls

- **Expecting a new Session to remember the old one**: it usually does not.
- **Dumping all material into context**: slow and expensive.
- **Changing requirements endlessly in one Session**: context pollution.
- **Saying "remember this" without writing it down**: it will be gone.
- **Trusting memory recall as truth**: recall can be wrong.

---

## Summary

- Session = one conversation; Context Window = working memory.
- Context fills up; when it does, the Agent forgets, slows down, and costs more.
- DSH does not automatically remember everything across Sessions.
- Write important information to files; summarize long tasks before starting a new Session.
- Memory plugins are a supplement, not a replacement.

---

# Chapter 6 — Tools and Skills: The Agent's Hands and Mind

## What You Will Learn

- Recognize the main tool categories;
- Read tool cards and approvals;
- Use planning, todos, subagents, and workflows;
- Understand what a Skill is, and how it differs from a Tool or Plugin;
- Use `present` correctly;
- Avoid tool overload and skill sprawl.

---

## 6.1 Tool Categories

You do not need to memorize every tool name. Know the categories.

| You want to | Tool type | Examples |
| --- | --- | --- |
| Inspect files | Read | Read file, list directory, search contents |
| Change files | Write | Create, overwrite, edit |
| Run programs | Execute | Terminal, tests, builds |
| Find information | Search | Web search, fetch pages |
| Split work | Collaboration | Subagents, workflows |
| Track work | Planning | Plan mode, todos, goals |
| Deliver | Delivery | `present` |
| Ask you | Interaction | Questions, confirmations |

One principle:

> **If read-only is enough, start read-only. If a small step is enough, do not take a big one.**

---

## 6.2 Tool Cards and Approvals

A tool call usually shows:

- Tool name;
- Parameters (path, command);
- Result (success, failure, output);
- Sometimes an approval prompt.

Check:

- Is the path correct?
- Is the command destructive?
- Does the output look wrong?
- Did it ignore a constraint?

### Denial is a skill

If it tries something you did not allow:

```text
Stop. Do not run that step.
Explain why you need it, and whether a read-only alternative exists.
```

---

## 6.3 Plans and Todos

For complex tasks, ask for a plan first:

```text
Enter plan mode. Give me a plan of at most five steps:
what to read/write, and how to verify each step.
Wait for my confirmation.
```

During execution, ask for a todo list:

```text
Break the task into todos and update them as you go.
Do not start everything at once.
```

Benefits:

- You can see progress;
- Steps are less likely to be skipped;
- Long tasks are easier to resume.

---

## 6.4 Subagents and Workflows

### Subagents

A subagent is a separate Agent with its own context. Use it for:

- Independent research;
- Parallel information gathering;
- Keeping large intermediate results out of the main context.

```text
Send a subagent to research these three links and return only key points and sources.
Continue the local file work in the main task.
```

Remember:

- Subagents consume model calls too;
- Their results can be wrong;
- The parent Agent must verify.

### Workflows

Workflows orchestrate multiple subagents with a script. They are useful for batch, parallel, or multi-stage work.

Beginners can skip workflows until subagents feel comfortable.

---

## 6.5 What a Skill Is

A Skill is an instruction manual, usually a folder with `SKILL.md`.

It tells the Agent:

- When to use the skill;
- What steps to follow;
- What pitfalls exist;
- Which references to read;
- Which scripts can be run.

### Skill vs. Tool

| | Tool | Skill |
| --- | --- | --- |
| Nature | Executable action | Knowledge and procedure |
| Example | Read file, run command | "How to do a code review" |
| Executed by | Harness | Agent reads and follows |
| Context | Schema is loaded | Loaded on demand |

### Skill vs. Plugin

- A Skill is knowledge; it usually does not add new tools;
- A Plugin is a runtime extension; it can add tools, services, or UI;
- Some plugins ship with Skills.

### Progressive disclosure

A good Skill does not dump thousands of lines into context. It:

1. Loads only name and description first;
2. Loads `SKILL.md` when the task matches;
3. Reads references or runs scripts only when needed.

That is why you can have many Skills without instantly filling the context.

---

## 6.6 Using Skills

Two common ways:

1. **Automatic**: the Agent chooses a relevant Skill from the task description;
2. **Explicit**: you name the Skill.

If you know the Skill:

```text
Use the `code-review` Skill for this change.
Read its SKILL.md, then follow the steps.
```

If you are unsure:

```text
Which Skills are relevant to this task? List them first; do not execute yet.
```

### Installing Skills

- Only install from trusted sources;
- Inspect scripts and network access;
- Do not put secrets in a Skill;
- Too many Skills consume metadata context;
- Keep versions aligned with the CLI/plugins.

---

## 6.7 `present`: Delivering Files

When the output is a file, the Agent may call `present`.

It means:

> **Declare an existing file as a final deliverable so the UI can show a card that opens the current file.**

It does not create, upload, or copy content. It records paths and descriptions.

Ask for it when needed:

```text
When done, use present for the final file. At most two files; do not present every intermediate artifact.
```

---

## 6.8 Common Tool Mistakes

- **More tools is better**: no; more tools add choice and context cost.
- **Read the whole directory**: search first, read what matters.
- **Treat subagents as free labor**: they cost tokens and can be wrong.
- **Install every Skill**: install only what you need.
- **Ignore tool results**: summaries can hide errors.

---

## Try It

1. Ask the Agent for a three-step plan;
2. Ask it to track execution with todos;
3. Ask it to search first instead of reading a whole directory;
4. Ask it to deliver one final file with `present`;
5. Ask: "Which tools did you use? Which were read-only?"

---

## Summary

- Tools cover read, write, execute, search, collaboration, planning, and delivery.
- Read-only first; small steps; watch tool cards.
- Subagents and workflows split work but are not free.
- Skill = knowledge; Tool = action; Plugin = runtime extension.
- `present` is a delivery declaration, not an upload.

---

## Part II Exercises

1. Write an `AGENTS.md` for your test workspace with three forbidden actions.
2. Start a new Session, read `AGENTS.md` and `PROJECT.md`, and restate the rules.
3. Use todos to complete a three-step task, updating after each step.
4. Ask which Skills are relevant, without executing them.
5. Deliver one file with `present` and observe the card.
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

Creator mode is an **Agent Preset** in DSH. Its internal id is `cordis`.

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

The direct motivation was simple: **when we started, the official `@getnote/dsh-plugin` did not support DSH Desktop**. Desktop is the entry point most people use every day, so we needed a version that actually worked in a local Desktop profile.

This was not an attempt to replace the official plugin. It was meant to fill the Desktop gap. That is also why the project focuses on the Desktop local bundle, locale/icon display, CLI discovery, and visibility in Plugin Manager.

The goal was not to copy another plugin's tool list. It was to turn the local `getnote` CLI into a set of Host tools that an Agent can use reliably. The source is public:

<https://github.com/leether/getnote-toolbox>

The source is public, and the package is published on npm as `@leether/getnote-toolbox`.

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

Agent cost is mostly tokens:

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

---

# Appendix

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
