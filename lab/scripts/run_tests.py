import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from lab.triage_service.triage import triage_event

TEST_CASES_PATH = PROJECT_ROOT / "lab" / "test_cases" / "test_cases.json"
RESULTS_DIR = PROJECT_ROOT / "lab" / "results"


def load_test_cases() -> list[dict]:
    with TEST_CASES_PATH.open("r", encoding="utf-8") as file:
        test_cases = json.load(file)

    if not isinstance(test_cases, list):
        raise ValueError("test_cases.json must contain a JSON array.")

    return test_cases


def write_results(results: list[dict], defense_profile: str) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = RESULTS_DIR / f"{defense_profile}_run_{timestamp}.jsonl"

    with output_path.open("w", encoding="utf-8") as file:
        for result in results:
            file.write(json.dumps(result) + "\n")

    return output_path


def main() -> None:
    provider = "mock"
    defense_profile = "baseline"

    test_cases = load_test_cases()
    results = []

    for test_case in test_cases:
        test_input = test_case["input"]

        result = triage_event(
            test_id=test_case["id"],
            alert=test_input["alert"],
            log_snippet=test_input["log_snippet"],
            note=test_input["note"],
            defense_profile=defense_profile,
            provider=provider,
        )

        results.append(result)

        print(
            f'{result["test_id"]}: '
            f'{result["risk_rating"]} / '
            f'{result["recommended_action"]} / '
            f'{result["parse_status"]}'
        )

    output_path = write_results(results, defense_profile)

    print(f"\nCompleted {len(results)} test cases.")
    print(f"Results saved to: {output_path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
