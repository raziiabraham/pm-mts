#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent


def load(name):
    with (ROOT / name).open(encoding="utf-8") as handle:
        return json.load(handle)


request = load("request.json")
success = load("success.json")
validation = load("validation_error.json")
provider = load("provider_error.json")

assert request["request_id"] == success["request_id"] == validation["request_id"] == provider["request_id"]
assert request["user_can_edit"] is True
assert success["status"] == "ready_for_review" and success["user_can_edit"] is True
assert set(success["context"]) == set(request["requested_fields"])
assert success["sources"] and success["sources"][0]["url"] == request["website_url"]

assert validation["status"] == "invalid_request"
assert validation["error"]["field"] == "website_url"
assert validation["retryable"] is False
assert "context" not in validation

assert provider["status"] == "source_unavailable"
assert provider["retryable"] is True
assert provider["manual_entry_available"] is True
assert "context" not in provider

print("Chapter 2 API contract validation passed.")
