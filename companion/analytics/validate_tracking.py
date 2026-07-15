#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
TYPE_MAP = {"string": str, "integer": int}

with (ROOT / "tracking_plan.json").open(encoding="utf-8") as handle:
    plan = json.load(handle)

contracts = {event["name"]: event for event in plan["events"]}
assert len(contracts) == len(plan["events"])
assert all(event["trigger"] and event["decision"] and event["owner"] for event in plan["events"])


def validate(event):
    contract = contracts.get(event.get("event_name"))
    if not contract:
        return False
    try:
        datetime.fromisoformat(event["observed_at"].replace("Z", "+00:00"))
    except (KeyError, TypeError, ValueError):
        return False
    properties = event.get("properties", {})
    for name, type_name in contract["required_properties"].items():
        value = properties.get(name)
        expected_type = TYPE_MAP[type_name]
        if type(value) is not expected_type:
            return False
    return True


cases = []
with (ROOT / "event_cases.jsonl").open(encoding="utf-8") as handle:
    for line in handle:
        if line.strip():
            cases.append(json.loads(line))

assert cases and any(case["expected_valid"] for case in cases) and any(not case["expected_valid"] for case in cases)
for case in cases:
    actual = validate(case["event"])
    assert actual is case["expected_valid"], f"Unexpected result for {case['case_id']}: {actual}"

print("Chapter 6 tracking validation passed.")
