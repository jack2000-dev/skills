# invest-mud — manual cases

Status: not run. These are manual cases, not automated results. Use fictional data only.

Run each case in a fresh agent session and record the agent/version, date, observed behavior, and pass/fail. For routing cases, make the catalog available through the agent's native skill support without explicitly invoking this skill. For behavior cases, explicitly load this skill. With manual instruction loading, test behavior only; automatic routing requires native support.

## Trigger cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| T1 | Help me with my money. I want a realistic personal financial plan. | Select this skill. |
| T2 | Review my finances and help me clear debt before investing. | Select this skill. |
| T3 | I want to plan my career and money so I can become financially independent. | Select this skill. |

## Near-miss cases

| ID | Prompt | Expected routing |
|----|--------|------------------|
| N1 | Explain how a Merkle tree works. | Do not select this skill. |
| N2 | Teach me JavaScript promises interactively. | Do not select this skill. |
| N3 | Translate "investment portfolio" into Thai. | Do not start a financial interview. |

## Behavior cases

### B1 — Begin the interview

Prompt: "I want to build my first emergency fund and start investing. Help me plan."

Expected: briefly explain the interview process, begin with the current-life-overview category, and ask one category at a time. Do not deliver the full report or a portfolio before gathering the necessary information.

### B2 — Incomplete information and urgent risks

Prompt: "I have expensive credit-card debt and no emergency savings. I don't want the full interview yet; give me a quick partial read on whether aggressive investing makes sense."

Expected: provide a clearly limited partial read, identify missing information, prioritize expensive debt and a safety net, and explain the reasoning. Do not invent balances, returns, or risk capacity, or present the partial answer as a completed comprehensive report.

### B3 — Complete fictional profile

Prompt:

```text
Use this fictional profile to produce the comprehensive report. All amounts are USD equivalents for this exercise; no FX conversion is needed.
1. Life: age 30, Bangkok, single, no dependents, healthy, goal is financial stability and a home deposit.
2. Income: stable salary 6,000/month, no bonus, about 3% annual raises, no side income.
3. Expenses: essentials 3,000/month including a 300 debt payment; discretionary spending 1,000/month. No other expenses.
4. Debt: credit card 6,000 at 20% APR, payment 300/month, no other debts; payoff date not fixed.
5. Assets: 24,000 cash and 10,000 diversified equity ETFs; no other assets or liabilities. Cash is accessible; ETFs are long-term assets.
6. Skills: software developer, five years' experience, strong backend skills, wants to improve communication, no paid course planned.
7. Time: five hours/week for learning, moderate energy, no equipment or language barriers.
8. Behavior: tracks spending monthly, sometimes buys impulsively, no leveraged investments or gambling history.
9. Milestones: clear debt in one year, save a 50,000 home deposit in five years, review retirement planning in ten years.
10. Risk: a 10% portfolio fall would worry me; at 30% I would want to sell; I cannot tolerate a 50% loss. I want modest risk and no leverage.
11. Safety nets: employer health cover, no dependents needing life insurance, no other policies, salary stated after tax; do not assume specific tax deductions or benefits.
```

Expected: cover all 14 report sections using the supplied information. Net worth is 28,000; current monthly surplus is 2,000 and savings rate about 33.3%. Explain the expense basis for runway, distinguish accessible cash from invested assets, state assumptions for forecasts, and respect the lower of risk tolerance and capacity. Avoid inventing tax rules or presenting assumed returns as guaranteed.
