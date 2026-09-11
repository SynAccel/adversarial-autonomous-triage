# System Model

## Representative Triage System

We implement a minimal but representative AI‑enabled triage system for security alerts.

### Inputs

For each event, the system ingests:

- Alert metadata (structured):
  - `alert_type`, `source`, `timestamp`, `user`, `src_ip`, `dst_ip`, `rule_severity`, etc.
- Log snippet (text):
  - A few lines of relevant logs.
- Analyst/narrative note (text):
  - e.g., “User says this was expected,” or “This looks like a test, ignore.”

### Outputs

The AI triage component produces:

- `summary`: Short textual summary for analysts.
- `risk_rating`: Low / Medium / High (or 1–5).
- `recommended_action`: e.g., “create ticket”, “block IP”, “escalate to IR”, “ignore”.
- Optional `auto_action` flag indicating whether the action would be automatically executed.

### Architecture

- A Python service or script:
  - Receives input (alert + logs + notes).
  - Constructs a prompt for an LLM:
    - System message: role, rules, safety constraints.
    - Data section: alert + logs + notes (marked as untrusted).
  - Calls an LLM API and parses the response into structured output.
- Logging:
  - Prompts and responses are logged for analysis (sanitized as needed).

This system is not intended as a production tool; it is a research stand‑in that captures the essential structure of AI‑enabled triage systems described in public documentation and talks.
