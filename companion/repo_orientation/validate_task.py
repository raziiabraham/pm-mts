#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
TOY = ROOT / "toy_repo"

with (ROOT / "expected_orientation.json").open(encoding="utf-8") as handle:
    expected = json.load(handle)

for relative in expected["files_inspected"]:
    assert (ROOT / relative).is_file(), f"Missing orientation file: {relative}"

design = (TOY / "docs/design/uploads.md").read_text(encoding="utf-8")
validator = (TOY / "src/validateUpload.ts").read_text(encoding="utf-8")
test = (TOY / "tests/document-cover.spec.ts").read_text(encoding="utf-8")

documented = re.search(r"Maximum file size communicated to users: (\d+) MB", design)
implemented = re.search(r"MAX_UPLOAD_BYTES = (\d+) \* 1024 \* 1024", validator)
tested = re.search(r"oneByteOverThreeMb = (\d+) \* 1024 \* 1024", test)

assert documented and implemented and tested
documented_mb = int(documented.group(1))
implemented_mb = int(implemented.group(1))
tested_mb = int(tested.group(1))
assert documented_mb == 5
assert implemented_mb == tested_mb == 3
assert documented_mb != implemented_mb
assert expected["contradiction"] and expected["repo_cannot_answer"] and expected["decision"]

print(f"Chapter 16 repo-orientation validation passed: documented {documented_mb} MB; implemented {implemented_mb} MB.")
