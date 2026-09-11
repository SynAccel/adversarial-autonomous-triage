# Threat Model

## Attacker Capabilities

- Can craft untrusted text that will be ingested by the triage system, such as:
  - Log lines
  - Ticket or incident notes
  - Analyst comments
- May know that the triage system uses an AI/LLM component.
- May use AI tools to help craft adversarial inputs.

## Attacker Goals

- Cause high‑severity incidents to be rated as low‑severity or ignored.
- Cause low‑severity noise to be escalated (to create distraction).
- Make the system consistently miss certain TTPs or indicators.
- Influence recommended or automated actions (e.g., “ignore” instead of “escalate”).

## Trust Boundaries

- The system trusts some structured fields (e.g., rule‑generated severity) more than free‑text notes.
- Free‑text fields (logs, notes) are treated as untrusted and potentially adversarial.
- We experiment with different trust weightings and input segmentation strategies.
