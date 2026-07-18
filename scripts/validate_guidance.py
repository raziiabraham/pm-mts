#!/usr/bin/env python3
"""Validate the reader- and agent-facing navigation for the public companion."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDES = [
    ROOT / "README.md",
    ROOT / "GETTING_STARTED.md",
    ROOT / "COMPANION_MAP.md",
    ROOT / "AI_GUIDE.md",
    ROOT / "AGENTS.md",
    ROOT / "companion" / "README.md",
    ROOT / "companion" / "api" / "README.md",
    ROOT / "companion" / "sql" / "sakila" / "README.md",
    ROOT / "companion" / "analytics" / "README.md",
    ROOT / "companion" / "ai_evaluation" / "README.md",
    ROOT / "companion" / "calibration" / "README.md",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_local_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for raw_target in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", text):
        target = raw_target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        require(resolved.exists(), f"Broken local link in {path.relative_to(ROOT)}: {raw_target}")


for guide in GUIDES:
    require(guide.exists(), f"Missing guide: {guide.relative_to(ROOT)}")
    validate_local_links(guide)

root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
require("Start with a product question—not Python" in root_readme, "Root README lost artifact-first positioning")
require("Chapters 1, 8, 13, 16, and 20" in root_readme, "Root README quick path is stale")
require("Chapter 18" in root_readme and "Chapters 19–20" in root_readme, "Root README capstone path is stale")

agent_guide = (ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
for expected in ("Chapter 2 API contract", "Chapter 5 SQL", "Chapter 13 AI evaluation", "adapt a worksheet"):
    require(expected in agent_guide, f"AI guide is missing route: {expected}")

agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
require("First-response contract" in agents, "AGENTS.md lost its first-response teaching contract")
require("Never lead with Python" in agents, "AGENTS.md no longer enforces artifact-first guidance")

chapter_map = (ROOT / "COMPANION_MAP.md").read_text(encoding="utf-8")
for chapter in range(1, 21):
    require(re.search(rf"^\| {chapter} \|", chapter_map, flags=re.MULTILINE) is not None, f"Chapter {chapter} is missing from COMPANION_MAP.md")

api_dir = ROOT / "companion" / "api"
api_readme = (api_dir / "README.md").read_text(encoding="utf-8")
for expected in (
    "https://api.briefly.example",
    "`POST`",
    "`/v1/context-drafts`",
    "200 OK",
    "400 Bad Request",
    "503 Service Unavailable",
):
    require(expected in api_readme, f"API guide is missing: {expected}")

request = json.loads((api_dir / "request.json").read_text(encoding="utf-8"))
success = json.loads((api_dir / "success.json").read_text(encoding="utf-8"))
validation = json.loads((api_dir / "validation_error.json").read_text(encoding="utf-8"))
provider = json.loads((api_dir / "provider_error.json").read_text(encoding="utf-8"))
request_id = request["request_id"]
require(all(item["request_id"] == request_id for item in (success, validation, provider)), "API examples no longer share one request_id")
require(success["status"] == "ready_for_review", "API success state drifted")
require(validation["status"] == "invalid_request", "API validation state drifted")
require(provider["status"] == "source_unavailable", "API provider state drifted")

openapi = (api_dir / "openapi.yaml").read_text(encoding="utf-8")
for expected in ("openapi: 3.1.0", "https://api.briefly.example", "/v1/context-drafts:", '"200":', '"400":', '"503":'):
    require(expected in openapi, f"OpenAPI contract is missing: {expected}")

sql_dir = ROOT / "companion" / "sql" / "sakila"
query = (sql_dir / "queries" / "film_demand_per_copy.sql").read_text(encoding="utf-8").strip()
sql_readme = (sql_dir / "README.md").read_text(encoding="utf-8")
require(query in sql_readme, "SQL guide no longer embeds the exact runnable query")
require("LOVE SUICIDES" in sql_readme and "rentals per copy" in sql_readme, "SQL guide is missing its visible result")
require("does **not** prove unmet demand" in sql_readme, "SQL guide lost its interpretation boundary")

print("Reader and AI-agent guidance validation passed.")
