# skills

Agent-neutral workflows by jack2000-dev, written in the open [Agent Skills format](https://agentskills.io/specification). Each skill contains Markdown instructions that a compatible agent can load and follow.

## Install

With [Node.js 22.20 or later](https://nodejs.org/), run:

```bash
npx skills add jack2000-dev/skills
```

Choose the skills and agents in the installer. Installation is scoped to the current project by default. The [skills CLI](https://github.com/vercel-labs/skills) supports many agents; see its [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) for native installation paths and compatibility.

```bash
# Browse the catalog without installing
npx skills add jack2000-dev/skills --list

# Choose one skill
npx skills add jack2000-dev/skills --skill super-explainer

# Install across projects for your chosen agents
npx skills add jack2000-dev/skills -g
```

## Skills

| Skill | Domain | When to use |
|-------|--------|-------------|
| [data-analysis-frameworks](skills/data/data-analysis-frameworks/SKILL.md) | data | Analyze data through ask, prepare, process, analyze, share, and act |
| [invest-mud](skills/finance/invest-mud/SKILL.md) | finance | Build a personal finance and life plan through an interview and analysis |
| [super-explainer](skills/learning/super-explainer/SKILL.md) | learning | Get a structured explanation with motivation, prerequisites, applications, and sources |
| [hand-held-teacher](skills/learning/hand-held-teacher/SKILL.md) | learning | Learn interactively through assessment, short lessons, hints, and a quiz |

## Use with other agents

The instructions do not require a particular model or vendor. Automatic discovery and activation depend on the receiving agent's skill support; behavior and available tools vary by agent.

If the installer does not support your agent:

1. Clone or download this repository.
2. Copy the **complete skill folder** into the agent's documented skill directory, keeping the folder name and any bundled resources. Some agents support the shared `.agents/skills/` convention; check your agent's documentation.
3. If the agent has no native skill support, attach the skill instructions or ask it to load them explicitly:

   ```text
   Read <path-to-skill>/SKILL.md and follow its instructions for this request: <your task>.
   ```

For agents without file access, paste the instructions and any resources needed for the task into the conversation. This provides the workflow, but does not add automatic discovery, missing tools, or permissions.

## Update or remove

```bash
# Inspect installed skills and available updates
npx skills list
npx skills check

# Update installed skills (choose the scope when prompted)
npx skills update

# Remove a project skill
npx skills remove super-explainer

# Remove a global skill
npx skills remove super-explainer -g
```

Updates are user-triggered. Changes published to GitHub do not automatically change installed skills. To browse and select newly added skills, run the `add` command again. See the [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for agent selection, private repositories, and other options.

## Develop a skill

Use `/skill-creator` for all skill creation, edits, and evaluation work, as required by [the contributor instructions](AGENTS.md).

### 1. Choose the purpose, domain, and name

Define what the skill should produce, when it should activate, and which similar requests it should leave alone. Pick a domain such as `data`, `finance`, or `learning`, or add one when needed.

For example, a skill that turns meeting notes into decisions and action items could live in `skills/writing/meeting-summary/`. The following steps use this example; substitute your own domain and skill name.

### 2. Create it through skill-creator

Open this repository in an agent with skill-creator available. Invoke it using the agent's supported syntax, for example `/skill-creator`, and provide a request like:

```text
Use skill-creator to create an agent-neutral skill named meeting-summary
in skills/writing/meeting-summary/.

Purpose: turn supplied meeting notes into a concise summary of decisions,
action items with owners and deadlines when stated, and open questions.
Use it when I ask to summarize meeting notes or extract meeting actions.
Do not use it for scheduling meetings or summarizing unrelated documents.
Do not invent missing owners, deadlines, or decisions.

Use templates/skill/SKILL.md.template as a starting point, removing unused
scaffolding. Create SKILL.md and evals/cases.md with trigger, near-miss,
and behavior cases. Keep the instructions independent of any agent vendor
or tool. Add the real skill to the README catalog and validate its format.
```

If skill-creator is unavailable, set it up in your authoring agent before creating or modifying skills here. The published skills themselves do not require skill-creator to run.

### 3. Review the generated files

The minimum repository layout for the example is:

```text
skills/writing/meeting-summary/
  SKILL.md
  evals/
    cases.md
```

`SKILL.md` needs YAML frontmatter followed by the actual workflow instructions. A minimal frontmatter example is:

```yaml
---
name: meeting-summary
description: "Summarize supplied meeting notes into decisions, action items, and open questions. Use for meeting summaries and action extraction, not scheduling or unrelated document summaries."
---
```

- Make `name` match the folder name, using lowercase letters, digits, and hyphens, with at most 64 characters.
- Keep `description` non-empty and at most 1,024 characters. Explain both the capability and when to use it.
- Write the workflow, expected output, and useful examples below the frontmatter. Remove all unfinished template text.
- Add `scripts/`, `references/`, or `assets/` only when the workflow needs them, and link resources with paths relative to the skill folder.
- Keep instructions agent-neutral. State any real environment or tool requirements instead of assuming they are available everywhere.

### 4. Validate and test locally

Ask skill-creator to run its format validator and review the folder/name match, references, and trigger description. From this repository's root, preview discovery and install only the new skill:

```bash
npx skills add . --list
npx skills add . --skill meeting-summary
```

Choose a test project or isolated agent environment for testing. To install into a different project, run the following from that project's directory, using the absolute path to this repository:

```bash
npx skills add /absolute/path/to/this/repo --skill meeting-summary
```

Run the prompts in `evals/cases.md` in fresh agent sessions. Include requests that should activate the skill, similar requests that should not, and cases that check the output and handling of missing information. For this example, check that action owners and deadlines are not invented.

Record the agent/version, date, observed result, and pass/fail. These are manual tests: successful format validation or installation does not prove behavior. Automatic trigger tests require the receiving agent's native skill support; explicit instruction loading can test the workflow itself.

### 5. Add it to the catalog and publish

Add a row to the Skills table above with the actual skill name, domain, purpose, and link to its `SKILL.md`. Then review and publish your changes. For the example, on `main`:

```bash
git diff --check
git diff
git status --short
git add README.md skills/writing/meeting-summary/
git diff --cached
git commit -m "Add meeting-summary skill"
git push origin main
```

Review the new files as well as the diff before committing. After the push, confirm discovery from GitHub and install the published skill:

```bash
npx skills add jack2000-dev/skills --list
npx skills add jack2000-dev/skills --skill meeting-summary
```

The installer discovers new skill folders automatically; no package registration, custom npm release, or server is needed. Users select a newly added skill with `add`; `update` refreshes skills they already installed.
