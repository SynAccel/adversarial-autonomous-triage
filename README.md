# Adversarially Robust Autonmous Triage

  This repo contains the lab, test cases, and scripts for SynAccel's research on adversarial robustness of AI-enabled autonomous triage for security alerts.

## Goal 

  Study how adversarial inputs affect an AI-based triage system's risk ratings and recommended actions, and evaluate design patters that improve robustness.

## Mission

Measuring whether attacker-controlled text in logs, ticket notes, or telemetry can cause an LLM-based alert-triage assistant to under-rate, mishandle, or 
hide evidence from a real security event—and then testing defenses that reduce that influence.

## Components 

- `lab/triage_service/` – Reference implementation of an AI‑enabled triage system (alert summarizer + risk scorer + action recommender).
- `lab/test_cases/` – Adversarial test cases (JSON/CSV) with intended attacker goals.
- `scripts/run_tests.py` – Test runner that executes all test cases against the triage service.
- `scripts/compute_metrics.py` – Computes manipulation success rates, omission rates, and other metrics.
- `docs/` – Research documentation and draft paper sections.

## Status

Work in progress by SynAccel (applied security research).

## License

(MIT)
