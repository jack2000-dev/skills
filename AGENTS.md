# skills

This repo is a personal laboratory and installable collection for authoring, testing, and storing agent-neutral skills in the open Agent Skills format.

## Purpose

- Draft and iterate on portable skills
- Store evals alongside each skill
- Version-control skill development

## Structure

```
skills/
  <domain>/
    <skill-name>/
      SKILL.md        # The skill itself
      evals/
        cases.md      # Trigger tests + behavior tests
plugins/
  <skill-name>/
    .codex-plugin/
      plugin.json     # Independent plugin identity and presentation
    skills/
      <skill-name>/   # Generated runtime copy; edit canonical skills/ instead
scripts/
  sync_plugins.py     # Generate plugin skill copies or check for drift
.agents/plugins/
  marketplace.json    # Catalog of independently installable plugins
templates/
  skill/
    SKILL.md.template # Non-installable skeleton for new skills
material/             # Reference PDFs and guides
```

## Domains

| Folder | What goes here |
|--------|---------------|
| `data/` | Data analysis, SQL, statistics |
| `finance/` | Personal finance, investing, life planning |
| `learning/` | Explanations, interactive teaching |

Other domains, such as `dev/` and `writing/`, can be added when needed.

## REQUIRED: Use `/skill-creator` for All Skill Work

**Always invoke the `/skill-creator` skill** when creating, editing, or improving any skill in this repo. Never write or modify a `SKILL.md` file directly without going through `/skill-creator`.

This applies to:
- Creating a new skill
- Updating an existing skill's content, triggers, or description
- Running evals or benchmarking a skill
- Optimizing a skill's trigger description

Reason: `/skill-creator` enforces consistent structure, eval coverage, and trigger accuracy across all skills.

## Workflow

1. Run `/skill-creator` — it will guide skill creation end-to-end
2. Place output at `skills/<domain>/<name>/SKILL.md`; the folder name must match the frontmatter `name`
3. Place evals at `skills/<domain>/<name>/evals/cases.md`
4. Preview with `npx skills add . --list`, then install locally with `npx skills add .` and select the receiving agent
5. For marketplace support, add the plugin manifest and catalog entry as described in README.md; run `python3 scripts/sync_plugins.py` and `python3 scripts/sync_plugins.py --check`
6. Commit canonical source, plugin packages, and catalog changes together

## Notes

- Keep skill instructions agent-neutral; do not assume a vendor, tool name, or installation directory unless the workflow requires it.
- Installed skill locations depend on the receiving agent and project/global scope. Manual installs must copy the complete skill folder.
- Evals are manual test cases, not automated. Run by pasting prompts into fresh sessions of the receiving agent.
