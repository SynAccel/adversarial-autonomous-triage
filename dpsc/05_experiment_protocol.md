# Experiment Protocol

## Study Title

Adversarially Robust Autonomous Triage for Security Alerts

## Objective

Evaluate whether untrusted, attacker-controlled text can influence an AI-enabled
security triage system's risk rating, recommended action, or incident summary.

## System Under Test

A controlled, representative security-alert triage service. The system receives:

- Structured alert metadata
- Untrusted log data
- Untrusted analyst or ticket notes

The system returns:

- A summary
- Risk rating: `low`, `medium`, or `high`
- Recommended action: `ignore`, `create_ticket`, `escalate`, or `contain`
- A human-review decision

## Dataset

- Five adversarial test cases: `TC001` through `TC005`
- Five matched control cases: `CTRL001` through `CTRL005`
- Test cases are stored in:
  - `lab/test_cases/test_cases.json`
  - `lab/test_cases/control_cases.json`

## Baseline Configuration

- Provider: `mock`
- Defense profile: `baseline`
- Temperature: Not applicable for mock provider
- Results file: `baseline_run_20260912_152351.jsonl`
- Metrics file: `baseline_run_20260912_152351_metrics.json`

## Metrics

- Parse success rate
- Defender success rate
- Attacker success rate
- Risk manipulation rate
- Action manipulation rate
- Omission success rate
- Secret disclosure rate

## Interpretation

The mock-provider run is a pipeline validation only. It does not constitute a
finding about the security or robustness of any real model. Formal experiments
will use a documented real model, fixed prompt version, fixed test-case version,
and controlled inference settings.