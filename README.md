# Adversarially Robust Autonomous Triage

This research lab studies the adversarial robustness of AI-assisted security-alert triage. It contains test cases, scripts, and a reference triage service for controlled evaluation.

## Research question

Can attacker-controlled text in logs, ticket notes, or telemetry cause an AI-based alert-triage assistant to under-rate a real event, mishandle it, or omit relevant evidence? The project evaluates that risk and tests defenses intended to reduce its influence.

## Components

- `lab/triage_service/` — Reference implementation of an AI-enabled triage system with an alert summarizer, risk scorer, and action recommender.
- `lab/test_cases/` — Adversarial test cases in JSON and CSV, with intended attacker goals.
- `scripts/run_tests.py` — Runs the test cases against the triage service.
- `scripts/compute_metrics.py` — Computes manipulation success rates, omission rates, and related metrics.
- `docs/` — Research documentation and draft paper sections.

## Status

Work in progress for applied security research. Results are experimental and should not be treated as evidence that an automated triage system is safe for production use.

## License

MIT
