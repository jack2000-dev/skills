# data-analysis-frameworks — manual cases

Status: not run. These are manual cases, not automated results.

Run each case in a fresh agent session and record the agent/version, date, observed behavior, and pass/fail. For routing cases, make the catalog available through the agent's native skill support without explicitly invoking this skill. For behavior cases, explicitly load this skill. With manual instruction loading, test behavior only; automatic routing requires native support.

## Trigger cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| T1 | Perform data analysis on our monthly sales data. | Select this skill. |
| T2 | Can you analyze this data and help us understand why orders fell? | Select this skill. |
| T3 | Do data analysis on this customer survey to identify the biggest service problems. | Select this skill. |

## Near-miss cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| N1 | What is a Merkle tree? | Do not select this skill; a conceptual explanation is appropriate. |
| N2 | Teach me Python one small lesson at a time. | Do not select this skill; interactive tutoring is appropriate. |
| N3 | Translate "monthly sales report" into Thai. | Do not select this skill. |

## Behavior cases

### B1 — Missing data and decision

Prompt: "Analyze our sales. I have not attached the data yet and haven't decided which question to answer."

Expected: establish the business question and required data before claiming findings. Explain what to collect or clarify; do not invent a dataset or results.

### B2 — Data preparation and analysis

Prompt:

```text
Analyze this data to decide whether we should investigate a drop in February sales.
month,revenue
January,100
February,80
February,80
March,
The repeated February row may be a duplicate; we have not confirmed it.
```

Expected: identify the duplicate ambiguity and missing value before drawing conclusions, explain the chosen treatment, and distinguish the observed January–February decrease from an unproven cause. Follow the six phases with detail proportional to the small dataset.

### B3 — Share and act

Prompt: "Our verified monthly revenue is January 100, February 80, March 120. Compare the changes and recommend what our sales manager should investigate next."

Expected: explain the question and data assumptions, calculate February's 20% decrease and March's 50% increase, communicate the finding clearly, and suggest a next action grounded in those results. Do not claim to have changed a business process.

### B4 — Larger input and tool choice

Prompt: "Perform data analysis on a CSV of 50,000 rows of monthly customer churn rates."

Expected: apply the six phases to the churn question, clarify the intended decision and data access, and choose a suitable tool such as SQL or Python for the dataset and environment. Do not require a tool that the receiving agent cannot access.
