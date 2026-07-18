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
    ROOT / ".agents" / "skills" / "pm-mts-guide" / "SKILL.md",
    ROOT / ".claude" / "skills" / "pm-mts" / "SKILL.md",
]
CHAPTER_GUIDES = [ROOT / "companion" / "chapters" / f"{chapter:02d}.md" for chapter in range(1, 21)]
GUIDES.extend([ROOT / "companion" / "chapters" / "README.md", *CHAPTER_GUIDES])
CHAPTER_TITLES = (
    "Why PMs Need a Technical Floor",
    "APIs Are Where Product Ideas Become System Behavior",
    "Delivery Is a Product Skill",
    "Image Assets Are a Product Architecture Problem",
    "SQL, NoSQL, and Product Reality",
    "Product Analytics Is a Model of User Behavior",
    "Experiments Turn Product Opinions into Evidence",
    "Flows Make Ambiguity Visible",
    "Design Systems Turn Taste into Shared Infrastructure",
    "Product Psychology Explains Why Users Move or Stop",
    "The Moment Traditional PM Stops Being Enough",
    "Do Not Start with AI; Start with Solution Fit",
    "AI Features Need Evaluation Systems",
    "AI Products Improve Through Calibration Loops",
    "When a Feature Becomes an Agent",
    "AI Agents Are Teammates, Not Magic Assistants",
    "The Repo Is a Product Surface",
    "Discovery Becomes Evidence Operations",
    "AI Makes Prototyping Cheap, Not Thinking Cheap",
    "Delivery Still Matters Most",
)


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
require("You have done the reading. Now let the repository respond." in root_readme, "Root README lost AI-first positioning")
require("$pm-mts-guide Chapter 2" in root_readme, "Root README is missing the Codex skill invocation")
require("/pm-mts 2" in root_readme, "Root README is missing the Claude command invocation")
require("Chapters 1, 8, 13, 16, and 20" in root_readme, "Root README quick path is stale")
require("Chapter 18" in root_readme and "Chapters 19–20" in root_readme, "Root README capstone path is stale")

agent_guide = (ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
for expected in ("Chapter 2: API contract", "Chapter 5: SQL", "Chapter 13: AI evaluation", "Any workbook chapter"):
    require(expected in agent_guide, f"AI guide is missing route: {expected}")
for expected in ("Progressive disclosure", "Prediction before reveal", "Counterexample coaching", "Teach-back", "Evidence ledger"):
    require(expected in agent_guide, f"AI guide is missing AI-first technique: {expected}")

agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
require("First-response contract" in agents, "AGENTS.md lost its first-response teaching contract")
for expected in ("The conversation is the interface", "Render, do, discuss", "Safe command policy", "Progressive workbook interview", "Session completion contract"):
    require(expected in agents, f"AGENTS.md is missing AI-first contract: {expected}")

skill = (ROOT / ".agents" / "skills" / "pm-mts-guide" / "SKILL.md").read_text(encoding="utf-8")
require(skill.startswith("---\nname: pm-mts-guide\n"), "PM MTS skill has invalid or missing frontmatter")
for expected in ("demonstrate", "apply", "experiment", "Keep the conversation as the interface"):
    require(expected in skill, f"PM MTS skill is missing behavior: {expected}")
skill_ui_path = ROOT / ".agents" / "skills" / "pm-mts-guide" / "agents" / "openai.yaml"
require(skill_ui_path.exists(), "PM MTS skill is missing Codex UI metadata")
skill_ui = skill_ui_path.read_text(encoding="utf-8")
require("$pm-mts-guide" in skill_ui, "PM MTS skill UI metadata has a stale default invocation")

claude_skill = (ROOT / ".claude" / "skills" / "pm-mts" / "SKILL.md").read_text(encoding="utf-8")
require(claude_skill.startswith("---\nname: pm-mts\n"), "Claude PM MTS skill has invalid or missing frontmatter")
require("/pm-mts $ARGUMENTS" in claude_skill, "Claude skill no longer accepts compact arguments")
require("Run safe, local, no-key repository checks yourself" in claude_skill, "Claude skill lost automatic execution behavior")

chapter_map = (ROOT / "COMPANION_MAP.md").read_text(encoding="utf-8")
for chapter in range(1, 21):
    require(re.search(rf"^\| {chapter} \|", chapter_map, flags=re.MULTILINE) is not None, f"Chapter {chapter} is missing from COMPANION_MAP.md")
    require(f"companion/chapters/{chapter:02d}.md" in chapter_map, f"Chapter {chapter} map does not route through its reader guide")

required_guide_sections = (
    "## Product question",
    "## What the agent brings into chat",
    "## Five-minute walkthrough",
    "## Take it to your product",
    "## Ask an AI coding agent",
    "## Evidence boundary",
)
for chapter, guide_path in enumerate(CHAPTER_GUIDES, start=1):
    guide = guide_path.read_text(encoding="utf-8")
    require(guide.startswith(f"# Chapter {chapter}: {CHAPTER_TITLES[chapter - 1]}"), f"Chapter {chapter} guide has the wrong title")
    for section in required_guide_sections:
        require(section in guide, f"Chapter {chapter} guide is missing: {section}")
    require("../figures/png/" in guide, f"Chapter {chapter} guide does not expose its book figure")
    require(f"figure_{chapter}_1.png" in guide, f"Chapter {chapter} guide does not link its chapter figure")
    require("../templates/" in guide, f"Chapter {chapter} guide does not link its workbook record")
    require(len(guide.split()) >= 180, f"Chapter {chapter} guide is too thin to guide a reader")

chapter_index = (ROOT / "companion" / "chapters" / "README.md").read_text(encoding="utf-8")
for chapter in range(1, 21):
    require(f"({chapter:02d}.md)" in chapter_index, f"Chapter index is missing Chapter {chapter}")

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

chapter_5 = CHAPTER_GUIDES[4].read_text(encoding="utf-8")
for expected in ("eight executable examples", "run_chapter_examples.sh", "Broader SQL progression"):
    require(expected in chapter_5, f"Chapter 5 guide lost restored SQL coverage: {expected}")

chapter_8 = CHAPTER_GUIDES[7].read_text(encoding="utf-8")
for expected in ("reflective listening", "seven steps for flowcharting", "verb + object"):
    require(expected in chapter_8, f"Chapter 8 guide lost restored flow guidance: {expected}")

flow_record = (ROOT / "companion" / "templates" / "flow_to_acceptance.md").read_text(encoding="utf-8")
require("## Reflective Listening Record" in flow_record, "Flow-to-Acceptance Record lost reflective listening")
require("Counterexample used to challenge" in flow_record, "Flow-to-Acceptance Record lost challenge step")

print("Reader and AI-agent guidance validation passed.")
