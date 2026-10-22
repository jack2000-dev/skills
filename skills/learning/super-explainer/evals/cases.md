# super-explainer — manual cases

Status: not run. These are manual cases, not automated results.

Run each case in a fresh agent session and record the agent/version, date, observed behavior, and pass/fail. For routing cases, make the catalog available through the agent's native skill support without explicitly invoking this skill. Include hand-held-teacher when testing their boundary. For behavior cases, explicitly load this skill. With manual instruction loading, test behavior only; automatic routing requires native support.

## Trigger cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| T1 | What is a Merkle tree? | Select this skill. |
| T2 | Bayesian inference explained in simple terms. | Select this skill. |
| T3 | I am a doctor. Explain how public-key encryption works. | Select this skill and adapt to the stated background. |

## Near-miss cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| N1 | Teach me recursion interactively, one small lesson at a time. | Prefer hand-held-teacher; do not deliver this skill's full explanation. |
| N2 | How do I install Node.js on macOS? | Do not select this skill; provide installation guidance. |
| N3 | What is 8 multiplied by 7? | Do not select this skill; answer the factual question directly. |

## Behavior cases

### B1 — Complete explanation

Prompt: "What is a Merkle tree?"

Expected: use all five sections in order: motivation; prerequisites and difficulty; plain-English explanation; takeaways, conclusion, and practical adaptation; origin, sources, and glossary. Define hashing before relying on it and provide a concrete use. Sources must be real; disclose uncertainty rather than fabricate them.

### B2 — Adapt to background

Prompt: "I'm a doctor with no programming background. Explain public-key encryption."

Expected: keep prerequisites realistic, define new technical terms, and use a relevant application without assuming programming knowledge. Preserve the five-section structure and avoid piling up analogies.

### B3 — Portable HTML output

Prompt: "Explain how a hash tree works and include a small HTML visualization I can save."

Expected: include the explanation structure and supply usable HTML with CSS classes and a style block or linked stylesheet for repeated styling. Do not assume an agent-specific rendering tool exists. If the agent cannot create files, provide saveable source directly; do not claim a file was created.
