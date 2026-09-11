# Problem and Research Questions

## Problem Statement

Organizations are beginning to deploy AI‑enabled systems to triage security alerts: summarizing events, assigning risk ratings, and recommending or executing responses. If these systems can be manipulated via adversarial inputs (e.g., crafted log lines, analyst notes, or ticket text), attackers can bias or blind defensive operations.

There is little public, systematic work quantifying how vulnerable such triage systems are to adversarial input, or which design patterns most improve robustness.

## Research Questions

1. How often do realistic adversarial inputs cause the triage system to misclassify high‑risk events as low‑risk (or vice versa)?
2. How much does AI‑assisted crafting of adversarial inputs improve attack success compared to manual crafting?
3. Which design patterns (input segmentation, trust boundaries, output validation, human‑in‑the‑loop checkpoints) most reduce successful manipulation?
4. How does increasing automation (more actions taken without human review) change the impact of successful manipulation?
