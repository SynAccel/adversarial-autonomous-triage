import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from lab.triage_service.triage import triage_event

TEST_CASE_FILES = [
    PROJECT_ROOT / "lab" / "test_cases" / "test_cases.json",
    PROJECT_ROOT / "lab" / "test_cases" / "control_cases.json",
]

RESULTS_DIR = PROJECT_ROOT / "lab" / "results"


def load_test_cases() -> list[dict]:
    all_test_cases = []
    seen_ids = set()

    for test_file in TEST_CASE_FILES:
        if not test_file.exists():
            raise FileNotFoundError(f"Test case file not found: {test_file}")

        with test_file.open("r", encoding="utf-8") as file:
            test_cases = json.load(file)

        if not isinstance(test_cases, list):
            raise ValueError(
                f"{test_file.name} must contain a JSON array of test cases."
            )

        for test_case in test_cases:
            test_id = test_case.get("id")

            if not test_id:
                raise ValueError(
                    f"A test case in {test_file.name} is missing an 'id'."
                )

            if test_id in seen_ids:
                raise ValueError(f"Duplicate test ID found: {test_id}")

            seen_ids.add(test_id)
            all_test_cases.append(test_case)

    return all_test_cases


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
    prompt_version = "baseline_v1"

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
            prompt_version=prompt_version,
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
