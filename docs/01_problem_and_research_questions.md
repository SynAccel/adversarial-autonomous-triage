# Problem and Research Questions

## Problem Statement

Organizations are beginning to deploy AI‑enabled systems to triage security alerts: summarizing events, assigning risk ratings, and recommending or executing responses. If these systems can be manipulated via adversarial inputs (e.g., crafted log lines, analyst notes, or ticket text), attackers can bias or blind defensive operations.

There is little public, systematic work quantifying how vulnerable such triage systems are to adversarial input, or which design patterns most improve robustness.

## Research Questions

1. Vulnerability:
How often do realistic adversarial inputs cause the triage system to misclassify high‑risk events as low‑risk (or vice versa), or to recommend inappropriate actions?

2. AI‑assisted attacks:
How much does AI‑assisted crafting of adversarial inputs improve attack success compared to manually crafted inputs?

3. Defensive patterns:
Which design patterns (e.g., input segmentation, trust boundaries, output validation, human‑in‑the‑loop checkpoints) most reduce successful manipulation, and by how much?

4.  Automation vs. robustness:
How does increasing automation (more actions taken without human review) change the impact of successful manipulation on security outcomes?


