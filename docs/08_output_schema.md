{
  "test_id": "TC001",
  "model": "provider/model-name",
  "run_id": "2026-09-12T14:34:00Z",
  "defense_profile": "baseline",
  "summary": "The system observed suspicious PowerShell execution and outbound network activity.",
  "risk_rating": "high",
  "recommended_action": "escalate",
  "requires_human_review": true,
  "raw_response": "Full unmodified model response goes here.",
  "parse_status": "success",
  "error": null
}



`test_id`	Links the result back to one specific adversarial scenario, such as TC001.
`model`	Lets you compare models later without redesigning the project.
`run_id`	Makes individual runs traceable and helps with reruns.
`defense_profile`	Critical for experiments: lets you compare baseline against controls like input_segmentation or output_validation.
`summary`	Lets you evaluate whether the model omitted, distorted, or correctly reported important facts.
`risk_rating`	Main measurement for whether an adversary successfully lowered or raised perceived severity.
`recommended_action`	Measures whether the attacker influenced an operational outcome, such as getting an alert ignored instead of escalated.
`requires_human_review`	Supports your automation-vs-safety research question. A high-risk case should not silently be ignored.
`raw_response`	Preserves evidence. If parsing fails or the model behaves strangely, you can review exactly what it said.
`parse_status`	Distinguishes a model/formatting failure from a valid triage result.
`error`	Records API, parsing, timeout, or validation errors without hiding them.
