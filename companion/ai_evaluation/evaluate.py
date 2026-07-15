#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent
ALLOWED_STATUS = {"matched", "needs_review", "no_match"}


def load_jsonl(name):
    with (ROOT / name).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


cases = {row["case_id"]: row for row in load_jsonl("dataset.jsonl")}
assert len(cases) == 5 and all(row["split"] == "held_out" for row in cases.values())

with (ROOT / "rubric.json").open(encoding="utf-8") as handle:
    rubric = json.load(handle)
assert len(rubric["hard_checks"]) == 4 and set(rubric["semantic_criteria"]) == {"1", "2", "3", "4"}


def compare(name):
    outputs = {row["case_id"]: row for row in load_jsonl(name)}
    assert set(outputs) == set(cases)
    passed = 0
    critical_failures = 0
    for case_id, case in cases.items():
        output = outputs[case_id]
        assert output["status"] in ALLOWED_STATUS
        assert output["evidence"] and all(isinstance(item, str) and item for item in output["evidence"])
        candidate_ids = {candidate["page_id"] for candidate in case["candidates"]}
        if output["status"] == "matched":
            assert output["selected_page_id"] in candidate_ids
        else:
            assert output["selected_page_id"] is None
        correct = (
            output["status"] == case["expected_status"]
            and output["selected_page_id"] == case["expected_page_id"]
        )
        passed += int(correct)
        if not correct and case["severity"] == "critical":
            critical_failures += 1
    return {
        "passed": passed,
        "total": len(cases),
        "critical_failures": critical_failures,
        "release": critical_failures == 0 and passed == len(cases),
    }


comparison = {
    "v1": compare("outputs_v1.jsonl"),
    "v2": compare("outputs_v2.jsonl"),
}
with (ROOT / "expected_comparison.json").open(encoding="utf-8") as handle:
    expected = json.load(handle)
assert comparison == expected, f"Comparison changed: {comparison}"

print(f"Chapter 13 evaluation passed: v1 {comparison['v1']['passed']}/{comparison['v1']['total']}; v2 {comparison['v2']['passed']}/{comparison['v2']['total']}.")
