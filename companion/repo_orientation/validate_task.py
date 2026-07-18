#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_REPO = ROOT.parents[2] / "noted-main"
REPO = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else DEFAULT_REPO

with (ROOT / "expected_orientation.json").open(encoding="utf-8") as handle:
    expected = json.load(handle)

if not REPO.is_dir():
    raise SystemExit(
        "Noted repository not found. Clone https://github.com/avidx-app/noted-main.git "
        "and pass its path as the first argument."
    )

for relative in expected["files_inspected"]:
    assert (REPO / relative).is_file(), f"Missing Noted file: {relative}"

storage = (REPO / "convex/storage.ts").read_text(encoding="utf-8")
vision = (REPO / "team-os/product/vision.md").read_text(encoding="utf-8")
paywall = (REPO / "team-os/product/prds/paywall/paywall-subscription-prd.md").read_text(encoding="utf-8")
upload = (REPO / "hooks/use-tracked-upload.tsx").read_text(encoding="utf-8")
edge_route = (REPO / "app/api/edgestore/[...edgestore]/route.ts").read_text(encoding="utf-8")
modal_test = (REPO / "components/modals/cover-image-modal.test.tsx").read_text(encoding="utf-8")

implemented = re.search(r"STORAGE_LIMIT_BYTES\s*=\s*(\d+)\s*\*\s*1024\s*\*\s*1024", storage)
assert implemented and int(implemented.group(1)) == 25
assert "File uploads (25MB hard cap)" in vision
assert "25 MB-per-file upload cap" in paywall
assert "input: { userId: undefined }" in upload
assert "if (!userId)" in edge_route and "Allow unauthenticated uploads" in edge_route
assert "handles file upload securely" in modal_test
assert "quota" not in modal_test.lower()
assert expected["contradiction"] and expected["repo_cannot_answer"] and expected["decision"]

print(
    "Chapter 17 repo-orientation validation passed: Noted describes a 25 MB limit, "
    "models cumulative user storage, and omits user identity from the upload quota gate."
)
