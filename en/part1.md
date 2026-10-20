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
- **Automatically safe.** It can take real actions; permissions and review matter.

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

Think of a Session as one meeting record.

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
| **Headless** | Automation, scripts, batch jobs | One-shot command line, no GUI |

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

You do not need every button, but you should know where four kinds of information appear:

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

## 3.5 Verify — Do Not Trust "Done"

"Done" is not "correct." Check:

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
