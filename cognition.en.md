## Start with the decision sequence

The most expensive Agent mistakes are rarely a bad line of code. They are:

- building a plugin where a CLI or Skill would do;
- writing implementation before defining the contract;
- translating every CLI command into a tool;
- shipping write operations without confirmation or rollback;
- testing only the happy path;
- publishing code that works but also publishes things that should never leave the workbench.

This article draws on the GetNote Toolbox project,[[3]](#ref3) but the subject is a transferable sequence:

> **Decide whether to build; define the contract; start read-only; verify before publishing.**

## 1. Decide whether a plugin should exist

Not every CLI deserves a plugin, and not every workflow deserves a tool.

| Situation | Better fit |
| --- | --- |
| Frequent, structured, safety-sensitive | Tool |
| Infrequent, complex, judgement-heavy | CLI or Skill |
| One-off task or fixed script | Script |
| Read-only diagnostics or environment management | CLI or Skill |
| Cross-application integration | Evaluate MCP or another protocol before rewriting |

A useful question: **what does this Tool take off the model's plate?**

If the answer is only "it renames a command", it probably should not be a Tool. A Tool earns its place by providing at least one of:

- structured arguments and validation;
- a safety boundary such as confirmation, timeouts, or output limits;
- normalization of IDs, limits, or errors;
- version compatibility;
- discoverability and routing.

**Ask the Agent to do this first**:

```text
Do not write code yet.
Produce a capability audit:
1. What commands, inputs, outputs, and side effects does the CLI have?
2. Which are frequent, structured, or safety-sensitive?
3. Which should stay in the CLI or a Skill?
4. Which operations are inverses of each other?
5. Where do versions and output formats differ?
```

## 2. Define the contract before the implementation

A Tool is not a collection of function names. It is a contract between the model and an external capability.[[1]](#ref1)[[2]](#ref2)

Every Tool should state:

- its name and when to use it;
- argument types, required/optional fields, and limits;
- the high-signal result;
- the errors it can return;
- its side effects;
- what the model should do next after a failure.

GetNote Toolbox ended up with 15 tools covering search, save, read, update, delete, tags, knowledge bases, and quotas. **Fifteen was not the goal.** It was the result of following workflows and contract boundaries.

Principles that survived:

- Prefix tool names with a domain name, such as `getnote_search`, not a global `search`;
- Group related actions under one tool when that reduces ambiguity;
- Pair inverse operations such as add and remove;
- Leave low-frequency, fast-changing operations in the CLI or a Skill;
- Never add a generic `run_command` or arbitrary HTTP passthrough.

**Ask the Agent for this next**:

```text
Do not implement yet.
For each candidate Tool, write the contract:
- argument schema
- result fields
- error types
- side effects
- permission/confirmation requirements
- verification method
```

## 3. IDs, limits, and errors must be reliable

### Why a snowflake ID cannot be treated as a JavaScript number

GetNote note IDs are 19-digit snowflake IDs.[[4]](#ref4) A snowflake ID is a 64-bit integer generated across machines, usually with a layout like:

```text
0 | 41-bit millisecond timestamp | 10-bit machine ID | 12-bit sequence
```

The timestamp makes IDs roughly time-ordered; the machine and sequence bits let multiple IDs be generated within the same millisecond. A 64-bit integer usually has 19 decimal digits.

JavaScript `Number` is IEEE 754 binary64: it has only 53 bits of precision. The largest safe integer is:

```text
2^53 - 1 = 9,007,199,254,740,991
```

A 19-digit ID is already outside that range.[[5]](#ref5) Around `1.9 × 10^18`, representable integers are about 256 apart, and the low bits of a snowflake carry machine and sequence information.

So:

```js
JSON.parse('{"note_id":1900000000000000001}')
// { note_id: 1900000000000000000 }
```

This is not simple string truncation. It is precision loss and rounding when a decimal integer is converted to binary64. A reviver receives the already-rounded Number; converting it to `BigInt` afterwards cannot recover the lost bits.

The correct contract is: **IDs are strings.**

```json
{ "note_id": "1900000000000000001" }
```

If you must parse numeric JSON, use a lossless parser, or quote integer literals above the safe range before `JSON.parse`. The compatibility layer in GetNote Toolbox does the latter; it is a patch, not a universal parser.

### Normalize limits and errors too

Older CLIs may ignore `--limit`. Returning the raw page makes the model believe the limit applied. A safer plugin truncates the parsed result and reports the count it actually returned.

Errors should be actionable, not just `exit code 1`:

- not logged in: suggest the login command;
- unsupported version: state the minimum version and upgrade path;
- invalid argument: name the argument and valid range;
- timeout: show the timeout and how to change it;
- output cap: explain the limit and how to narrow the request;
- business failure: keep the CLI message and relevant context.

> IDs, counts, and errors must be usable by the model's next action.

## 4. The tool surface is not a 1:1 CLI mirror

A common mistake is to expose 50 CLI commands as 50 tools.

More tools mean more choices, more context, and more chances to pick the wrong one. Organize the tool surface around workflows:

- prioritize frequent reads and writes;
- isolate destructive operations;
- pair inverse operations;
- leave low-frequency capabilities to the CLI or a Skill;
- merge related actions instead of creating near-duplicates.

GetNote Toolbox stopped at 15 tools. Not because more were impossible, but because every new tool had to justify itself.

**Ask the Agent to draw the surface first**:

```text
Draw the tool surface before writing code:
- Which operations should be merged?
- Which are inverses?
- Which are out of scope for now?
- Which model decision does each new Tool remove?
```

## 5. Design write operations for failure

A read failure may produce a wrong answer. A write failure can damage a user's data.

For every write operation, answer:

- What is the worst thing that can happen?
- Does it need explicit confirmation?
- Can the impact be previewed?
- How can it be rolled back?
- Is it idempotent or retry-safe?
- Does the result make it clear that it actually succeeded?

GetNote Toolbox chose:

- deleting a note requires `confirm: true`;
- deleting a tag requires a tag ID, not a guessed tag name;
- tag updates are documented as replacement semantics;
- removing notes from a knowledge base does not delete the notes;
- write tests create test data and clean it up.

**Ask the Agent before any write**:

```text
Before executing a write:
1. What will be changed?
2. What is the worst-case impact?
3. How will we confirm success?
4. How do we roll back?
5. If confirmation is missing, stop.
```

## 6. Authentication, permissions, and trust boundaries

GetNote Toolbox never reads, caches, or echoes an API key. It calls a logged-in local CLI.

That is intentional:

- the plugin does not store credentials;
- the CLI owns login and expiry;
- users can diagnose with `getnote auth status`;
- keys never enter the model context.

But "does not touch keys" is not the same as "has no trust boundary":

- the child process inherits the Host environment;[[6]](#ref6)
- an `npx` fallback may download the latest CLI, creating version drift and supply-chain risk;
- the local CLI must itself be trusted;
- permissions, sandboxing, and confirmation still need separate design.

When reproducibility matters, pin the local CLI with `binaryPath` instead of silently depending on `latest`.

## 7. Test in two layers

### A fake CLI protects the contract

Unit tests use a fake CLI and never touch a real account:

- 19-digit IDs;
- nested responses;
- old-version flag fallback;
- tag add/remove followed by a re-read;
- knowledge-base add/remove;
- delete confirmation.

These tests are fast, stable, repeatable, and cannot leak real notes.

### The real CLI protects the environment

Then run a read-only smoke test with the real CLI:

- is it logged in?
- what does the real output look like?
- do the tool calls work end to end?
- are the errors actionable?

Real output can contain note titles and excerpts, so it must not be pasted into an issue, chat, or commit. Prefer synthetic fixtures; when real data is unavoidable, create test notes, clean them up, and keep reports local and gitignored.

**Ask the Agent for evidence**:

```text
Do not just say "done".
Show:
- which paths were tested;
- what used a fake CLI and what used the real one;
- which failure paths were covered;
- where the evidence is;
- what remains unverified.
```

## 8. Version compatibility must be diagnosable

CLI differences are part of plugin design, not an edge case.

Real examples:

- 19-digit IDs are sometimes numbers and sometimes strings;
- older CLIs ignore `limit`;
- `note update` and `kb remove` need `-y` in newer versions, while older versions reject the flag;
- saving a URL may return a nested `data.note`.

You can support old versions or require a new one, but make it explicit:

- which versions are supported;
- the recommended minimum;
- what error appears when the version is unsupported;
- whether there is a fallback path;
- where the CLI path is pinned.

Compatibility is not "support everything". It is making failure explainable and actionable.

## 9. Run a reverse review before publishing

Code that runs is not the same as code that is safe to publish.

Before release, ask what should **not** leave the workbench:

- Do eval reports contain real note IDs, titles, or excerpts?
- Do internal drafts contain local paths, account details, or plans?
- Does Git history contain a personal email?[[8]](#ref8)
- Does the package scope expose a local username?
- Does the npm package include tests, `.env` files, or internal documents?[[7]](#ref7)
- Does the public README contain "planned", "placeholder", or TODO language?
- Is the repository a deliverable, or is it still a workbench?

GetNote Toolbox handled these before publication: removed eval outputs and internal drafts, started a clean Git history, replaced the local package scope, removed local environment details, and kept only reviewed source, tests, licenses, and public documentation.

**Ask the Agent for a reverse review**:

```text
Before publishing:
1. Scan for keys, tokens, emails, absolute paths, and .env files.
2. Check eval output and real-note data.
3. Inspect the package contents, not just the working tree.
4. Check README/site for internal planning language.
5. Give a "safe to publish / not safe" conclusion with evidence.
```

## 10. A decision table

| Fork | Safer choice | Cost |
| --- | --- | --- |
| Should this be a plugin? | Audit capabilities first | More upfront time |
| Wrap a CLI or call the API? | Reuse the CLI's auth when it fits | Must adapt to CLI versions |
| Mirror the CLI or design a tool surface? | Design around workflows | Requires judgment and deletion |
| More tools or the minimum useful set? | Minimum useful set | Some low-frequency gaps |
| Return raw JSON or normalize? | Return high-signal fields | Adaptation work |
| Casual deletes or explicit confirmation? | Explicit confirmation | One more step |
| Plugin manages keys or delegates to CLI? | Delegate to CLI | Depends on CLI login |
| Unit tests only or two layers? | Fake CLI plus real acceptance | More test cost |
| Newest CLI only or compatibility? | Explicit support matrix | More branches |
| Publish first or review first? | Review first | Slower release |

## 11. An execution checklist for the Agent

Before asking an Agent to build a plugin, tool, or automation, make it answer:

1. Does this capability really need to be a Tool?
2. Which contract, guard, or normalization does it add?
3. Are IDs, counts, errors, and results reliable?
4. What is the worst-case write, and how is it confirmed and rolled back?
5. Where do authentication and secrets live, and what is the trust boundary?
6. What did the fake CLI test, and what did the real CLI verify?
7. When the CLI version changes, is the failure actionable?
8. What data must never leave the workbench before publication?

If the Agent cannot answer, do not let it write code yet.

## 12. Conclusion

The key to better Agent work is not more tools. It is clearer boundaries:

- decide whether to build;
- define the contract before the implementation;
- read-only before writes;
- test before release;
- review before publishing.

Tools are capability interfaces. Skills are operating knowledge. Permissions are action boundaries. When all three are clear, the Agent is doing work rather than guessing.

## References

1. <a id="ref1"></a>[DeepSeek Harness plugin development](https://deepseek-harness.github.io/deepseek-harness/en/develop/basic/)
2. <a id="ref2"></a>[DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)
3. <a id="ref3"></a>[GetNote Toolbox](https://github.com/leether/getnote-toolbox)
4. <a id="ref4"></a>[Twitter Snowflake (archived repository)](https://github.com/twitter-archive/snowflake)
5. <a id="ref5"></a>[MDN: Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
6. <a id="ref6"></a>[Node.js: child_process](https://nodejs.org/api/child_process.html)
7. <a id="ref7"></a>[npm publish documentation](https://docs.npmjs.com/cli/v11/commands/npm-publish)
8. <a id="ref8"></a>[Git documentation](https://git-scm.com/docs)

> All links are public sources; product behavior may change between versions.
