# Chapter 4 — Workspaces, Files, and Permissions

## What You Will Learn

- Why the workspace is a safety boundary;
- What the Agent can read and write;
- The difference between `workspace-write` and `danger-full-access`;
- How to avoid deletion, overwriting, and secret leaks;
- How to use `AGENTS.md` to set project rules.

---

## 4.1 What a Workspace Really Is

A workspace is a folder.[[1]](#ref1)

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

If the Agent breaks something:[[2]](#ref2)

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

## References

1. <a id="ref1"></a>[DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)
2. <a id="ref2"></a>[Git documentation](https://git-scm.com/docs)

> All links are public sources; product behavior may change between versions.

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

A model can process only a limited amount of text at once. That limit is the **Context Window**.[[1]](#ref1)

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

DSH keeps a session log, but that is not the same as cross-session long-term memory.[[2]](#ref2)

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

## References

1. <a id="ref1"></a>[DeepSeek API token usage](https://api-docs.deepseek.com/quick_start/token_usage)
2. <a id="ref2"></a>[DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)

> All links are public sources; product behavior may change between versions.

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

A Skill is an instruction manual, usually a folder with `SKILL.md`.[[1]](#ref1)

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

When the output is a file, the Agent may call `present`.[[2]](#ref2)

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

## References

1. <a id="ref1"></a>[DeepSeek Harness plugin development](https://deepseek-harness.github.io/deepseek-harness/en/develop/basic/)
2. <a id="ref2"></a>[DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)

> All links are public sources; product behavior may change between versions.
