---
name: super-explainer
description: Explain any topic, concept, technology, theory, or idea using a structured 5-part format that leads with WHY the user should care, names prerequisites and difficulty, gives a jargon-free introduction, ends with a practical real-world application, and finishes with origin, sources, and a glossary. Trigger this skill whenever the user asks to understand or explain something — phrases like "[X] explained," "what is [X]," "explain [X]," "tell me about [X]," "how does [X] work," "what's the deal with [X]," "[X] for beginners," "[X] in simple terms," "I don't understand [X]," or "help me understand [X]." Trigger even when the user is asking about something seemingly basic — the skill's value is the structured format, not just the content. Do NOT trigger for narrow factual lookups (e.g., "what's today's weather"), code-debugging questions, step-by-step tutorials ("how do I install X"), or interactive tutoring requests ("teach me X one step at a time").
---

# Super-Explainer

Structured topic explanations that lead with motivation, respect prerequisites, and end with usable knowledge.

## Why This Format Exists

Most explanations fail in predictable ways: they assume context the reader doesn't have, dump jargon up front, omit the reason the topic matters, or stop before showing how to apply the idea. This skill enforces a fixed structure that fixes those failures. The structure is opinionated on purpose — readers should always know what's coming next, and the writer should never skip the parts that are easy to skip (motivation, prerequisites, real-world adaptation, glossary).

## Output Structure

ALWAYS produce these sections in this exact order. Headings stay as written below.

### 1. Why This Matters

Lead with motivation, not definition.

- **Why you should know this** — concrete benefits (career, decision-making, conversations, mental models)
- **Why you might NOT need this** — be honest. If the topic is niche, say so. Saves the reader's time.
- **How you'll use it** — practical adaptation in real work or life
- **Category** — what bucket this belongs to (e.g., "Statistics → Bayesian methods," "Cryptography → Asymmetric primitives," "Macroeconomics → Monetary policy")

Keep this section to 4–8 short bullets. Do not pad.

### 2. Prerequisites & Difficulty

| Field | Value |
|-------|-------|
| Difficulty | Beginner / Intermediate / Advanced |
| Prerequisites | List of concepts/skills the reader needs first |
| Time to grasp basics | Rough estimate (e.g., "30 min reading," "a weekend project") |
| Time to mastery | Rough estimate (e.g., "6 months of practice") |

If a prerequisite is itself non-obvious, link or briefly define it in one line.

### 3. The Explanation (Plain English)

Introduce the topic in simple English. Rules:

- **No jargon on first encounter.** If a technical term is unavoidable, define it the first time it appears, in one short clause.
- **Use analogies sparingly.** Analogies leak — they help intuition but mislead on edge cases. Use one when it earns its place. Never stack two.
- **Be concise.** A good explanation is short, not exhaustive. Aim for the minimum content that gets the reader to "ah, I get it."
- **Show the shape before the details.** Give the high-level picture in 2–3 sentences before drilling into mechanics.

If the topic has natural sub-parts, use sub-headings. If not, prose is fine.

### 4. Core Takeaways → Conclusion → Practical Adaptation

Three labeled mini-sections:

**Core Takeaways** — 3–5 bullets. The things the reader should still remember a week from now.

**Conclusion** — 2–4 sentences synthesizing the explanation. What it means, what it doesn't mean, what to be careful of.

**Practical Adaptation** — concrete ways to use this in the real world. Examples:
- A decision the reader can now make better
- A conversation they can now follow
- A small experiment, project, or exercise to lock the idea in
- A heuristic or rule of thumb extracted from the topic

This section is where the explanation becomes useful. Do not skip it.

### 5. Origin, Sources, and Glossary

Three sub-sections, in this order:

**Origin & Timeline**

A short narrative or table covering: who developed the idea, when, what problem it was originally solving, and key milestones since. Date precision matters — use years.

| Year | Event | Who |
|------|-------|-----|
| ... | ... | ... |

**Further Reading**

3–6 high-quality sources. Prefer:
- Original papers or primary sources
- Well-regarded textbooks
- Authoritative articles (e.g., Stanford Encyclopedia of Philosophy, established technical blogs, official docs)

Format: `Title — Author/Org (year) — short description of why this source`

Avoid linking content the reader cannot verify (dead links, paywalls without alternatives, AI-generated summaries).

**Glossary**

Every term that needed defining in the explanation, plus any other technical terms the reader is now equipped to encounter. Format:

| Term | Meaning |
|------|---------|
| ... | ... |

---

## Tables — When and How

Use tables when the content is comparative, parametric, or list-with-attributes. Common cases:
- Comparing approaches (e.g., "TCP vs UDP")
- Summarizing parameters or variants
- Timeline of events
- Glossary

Avoid tables for narrative explanation — prose carries cause-and-effect better than rows.

## HTML Visualizations — Use CSS

When the explanation calls for an HTML visualization (a diagram, layout sketch, interactive demo, styled comparison), always pair the markup with CSS — either a `<style>` block or a linked stylesheet. Reason: inline `style="..."` attributes repeat the same declarations on every element, bloating the output and wasting tokens. A single CSS rule targeting a class scales for free.

Concretely:
- Define classes once in `<style>`, apply via `class="..."` on elements.
- Prefer semantic class names (`.node`, `.edge`, `.highlight`) over presentational ones (`.red-box`).
- Use CSS variables for repeated values (colors, spacing) so changes stay local.
- Skip inline styles unless a value is genuinely unique to one element.

This keeps the HTML compact, the visualization easier to scan, and the token cost lower for the reader's context.

## Tone & Style

- Direct, plain, friendly. Like a knowledgeable colleague at lunch, not a lecturer.
- Honest about uncertainty. If the topic has open debates, say so in one line — don't fake consensus.
- No flattery. Don't say "great question." Just answer.
- Active voice. Short sentences. Concrete examples beat abstract framing.

## Length Guidance

Total length depends on topic complexity:

| Topic complexity | Target length |
|------------------|---------------|
| Simple (e.g., "what is a cookie") | 400–700 words |
| Moderate (e.g., "what is Bayesian inference") | 800–1500 words |
| Complex (e.g., "what is general relativity") | 1500–2500 words |

If the topic genuinely needs more, go longer — but justify the length by content density, not padding.

## Examples

### Example 1 — Trigger phrasing

**Input:** "What is a Merkle tree?"

**Output:** Full 5-section structure. Section 1 explains why Merkle trees matter (blockchains, Git, file integrity verification). Section 2 lists prerequisites: hashing, basic tree data structures. Section 3 explains the structure in plain English with one analogy (e.g., a tournament bracket where each match's winner is a hash of the two below). Section 4 gives takeaways and a real-world adaptation (e.g., "next time you `git commit`, you're building a Merkle tree"). Section 5 includes Ralph Merkle (1979 patent), Git/Bitcoin/IPFS as adoption milestones, links to the original paper, glossary of "hash function," "leaf node," "root hash."

### Example 2 — "Explained" phrasing

**Input:** "Compound interest explained"

**Output:** Full 5-section structure. Section 1 leads with the financial impact and why ignoring compounding is the most expensive mistake people make. Difficulty: Beginner. No prerequisites beyond basic multiplication. Section 3 explains in plain English with a 2-sentence shape ("Interest earns interest. So your growth is curved, not linear.") before the formula. Section 4 includes a heuristic (Rule of 72). Section 5 traces back to medieval banking, references Einstein's apocryphal quote with appropriate skepticism, and glosses "principal," "compounding period," "APY."

### Example 3 — Edge case (skill should NOT trigger)

**Input:** "How do I install Node.js on macOS?"

**Output:** Skill does NOT trigger. This is a step-by-step tutorial request, not a conceptual explanation. The agent handles it directly with its available tools.

---

## Common Failure Modes to Avoid

- **Skipping Section 1 motivation** — diving straight into the definition. Always start with WHY.
- **Filling Section 2 with fake prerequisites** — only list what's actually needed.
- **Stacking analogies in Section 3** — pick one or zero. Two analogies confuse more than they clarify.
- **Generic Section 4 takeaways** — "this is important to know" is not a takeaway. Be specific.
- **Empty Section 5 sources** — if you cannot name 3 real sources, say so honestly rather than fabricating.

## Adapting to the User

If the user gives signals about their background (e.g., "I'm a doctor, explain Bitcoin to me"), tailor:
- Section 2 prerequisites — assume what they already know
- Section 3 analogies — borrow from their domain
- Section 4 practical adaptation — make it relevant to their work

Without signals, write for a smart non-expert.
