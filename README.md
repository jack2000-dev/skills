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

- Keep installable skills in `skills/<domain>/<skill-name>/SKILL.md`, with a matching frontmatter `name`.
- Use [the authoring template](templates/skill/SKILL.md.template) as a starting point through skill-creator. It is outside the installable catalog and deliberately has a different filename.
- Store manual trigger and behavior cases in each skill's `evals/cases.md`. Run them in fresh agent sessions; these cases are not automated tests.
- Preview local discovery with `npx skills add . --list`; use `npx skills add .` to install your working copy for local testing.

No custom npm package or server is required to distribute this collection. Publishing skill content to this GitHub repository makes it available to the installer.
