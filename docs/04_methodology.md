# Methodology

## Overview

We define a set of adversarial test cases, run them against the triage system, and measure how often the attacker’s intended effect is achieved. We then evaluate defensive patterns and measure their impact on these success rates.

## Test Case Categories

1. Direct instruction injection
2. Risk manipulation narratives
3. Conflicting signals
4. Data leakage / exfil framing
5. AI‑assisted variants

## Metrics

- Risk manipulation success rate
- Fact omission / distortion rate
- Action manipulation success rate
- Confidence / explanation quality (qualitative)

## Process

1. Define test cases in `lab/test_cases/`.
2. Run tests via `scripts/run_tests.py`.
3. Compute metrics via `scripts/compute_metrics.py`.
4. Record results in `lab/results/`.
5. Analyze and document findings in `docs/05_results.md` and `docs/06_defensive_patterns.md`.
