# hand-held-teacher — manual cases

Status: not run. These are manual cases, not automated results.

Run each case in a fresh agent session and record the agent/version, date, observed behavior, and pass/fail. For routing cases, make the catalog available through the agent's native skill support without explicitly invoking this skill. Include super-explainer when testing their boundary. For behavior cases, explicitly load this skill. With manual instruction loading, test behavior only; automatic routing requires native support.

## Trigger cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| T1 | Teach me JavaScript promises one small lesson at a time. | Select this skill. |
| T2 | I'm new to geography. Can you tutor me interactively on reading maps? | Select this skill. |
| T3 | I want to learn recursion. Guide me with questions and hints over several turns. | Select this skill. |

## Near-miss cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| N1 | What is recursion? Give me a standalone explanation. | Prefer super-explainer; do not begin a tutoring interview. |
| N2 | How do I install Node.js on macOS? | Do not select this skill; provide installation guidance. |
| N3 | Fix this JavaScript error: TypeError: x is not a function. | Do not select this skill; handle debugging directly. |

## Behavior cases

### B1 — Assessment before teaching

Prompt: "Teach me JavaScript promises."

Expected first reply: ask about prior knowledge and the technical environment, with at most three short questions. Do not teach a lesson yet.

Then reply: "I know callbacks but not promises. I use Node.js and want to understand async code."

Expected next reply: outline a small lesson plan, teach only the first chunk, and wait after a check-in question. Do not dump all chunks or the quiz at once.

### B2 — Hints and explicit answer requests

Start a short tutoring session. At a check-in question, say: "I'm stuck; give me a hint."

Expected: offer a useful hint or smaller question without revealing the entire answer.

Then say: "Just tell me the answer."

Expected: give the answer with a short reason; do not continue withholding it. At the end of the lesson, offer real further reading and a short quiz without answers. If the learner asks to skip the quiz, provide a brief recap.

### B3 — Standalone installation and changed preference

Install or load only hand-held-teacher. Prompt: "Teach me how maps work, interactively."

After the assessment, reply: "Actually, I'd rather have the whole thing as a reference explanation."

Expected: confirm the switch if needed and provide a standalone explanation. Do not require super-explainer to be installed, claim it was loaded when unavailable, or stop because another skill is missing.
