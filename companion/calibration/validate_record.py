#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent
EVAL = ROOT.parent / "ai_evaluation"


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path):
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


record = load_json(ROOT / "filled_record.json")
cases = {row["case_id"]: row for row in load_jsonl(EVAL / "dataset.jsonl")}
v1 = {row["case_id"]: row for row in load_jsonl(EVAL / "outputs_v1.jsonl")}
v2 = {row["case_id"]: row for row in load_jsonl(EVAL / "outputs_v2.jsonl")}
expected = load_json(EVAL / "expected_comparison.json")

case = cases[record["case_id"]]
assert record["failure"]["severity"] == case["severity"]
assert record["failure"]["observed_status"] == v1[record["case_id"]]["status"]
assert record["failure"]["observed_page_id"] == v1[record["case_id"]]["selected_page_id"]
assert record["failure"]["expected_status"] == case["expected_status"]
assert record["failure"]["expected_page_id"] == case["expected_page_id"]
assert v2[record["case_id"]]["status"] == case["expected_status"]
assert v2[record["case_id"]]["selected_page_id"] == case["expected_page_id"]

regression = record["regression"]
assert regression["cases"] == len(cases) == expected["v2"]["total"]
assert regression["v1_passed"] == expected["v1"]["passed"]
assert regression["v2_passed"] == expected["v2"]["passed"]
assert regression["v2_critical_failures"] == expected["v2"]["critical_failures"]
assert record["decision"]["conditions"] and record["limits"]

print("Chapter 14 calibration record validation passed.")
