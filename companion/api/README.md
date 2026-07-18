# Chapter 2: Read an API as a Product Contract

You do not need Python to begin this exercise. Start with the contract a product manager would discuss with engineering and design.

## Contract at a glance

| Field | Value |
| --- | --- |
| Host | `https://api.briefly.example` |
| Method | `POST` |
| Path | `/v1/context-drafts` |
| Content type | `application/json` |
| Product job | Turn a public website into an editable context draft |

`api.briefly.example` is an explicit fictional, non-live host. The exercise teaches the request, response, state, and ownership contract without pretending to contact a production service. The same contract is available in machine-readable form as [`openapi.yaml`](openapi.yaml).

## Request

```http
POST /v1/context-drafts HTTP/1.1
Host: api.briefly.example
Content-Type: application/json
```

```json
{
  "request_id": "req_briefly_001",
  "website_url": "https://example.invalid",
  "requested_fields": [
    "flagship_offering",
    "offering_description",
    "customer_segments"
  ],
  "user_can_edit": true
}
```

[Open the request as JSON](request.json)

Before reading the responses, predict:

- What should the interface show while the request is running?
- Which fields must remain editable?
- What should happen when the URL is invalid?
- What should happen when the URL is valid but the source cannot be retrieved?

## Response 1: draft ready for human review

**HTTP status:** `200 OK` · **Product state:** `ready_for_review`

```json
{
  "request_id": "req_briefly_001",
  "status": "ready_for_review",
  "context": {
    "flagship_offering": "Briefly Research Workspace",
    "offering_description": "A fictional workspace for organizing public market evidence.",
    "customer_segments": ["product teams", "market researchers"]
  },
  "sources": [
    {
      "url": "https://example.invalid",
      "retrieved_at": "2026-07-01T00:00:00Z"
    }
  ],
  "user_can_edit": true
}
```

The interface can show the draft and its source, but should not present generated context as verified truth. The user remains able to edit it.

[Open the success response as JSON](success.json)

## Response 2: the request is invalid

**HTTP status:** `400 Bad Request` · **Product state:** `invalid_request`

```json
{
  "request_id": "req_briefly_001",
  "status": "invalid_request",
  "error": {
    "code": "invalid_website_url",
    "field": "website_url",
    "message": "Enter a public http or https website URL."
  },
  "retryable": false
}
```

The interface should return focus to `website_url` and explain what the user must correct. Retrying the same invalid payload would not help.

[Open the validation response as JSON](validation_error.json)

## Response 3: the source provider is unavailable

**HTTP status:** `503 Service Unavailable` · **Product state:** `source_unavailable`

```json
{
  "request_id": "req_briefly_001",
  "status": "source_unavailable",
  "error": {
    "code": "website_could_not_be_retrieved",
    "message": "We could not retrieve public website content. You can retry or enter the context yourself."
  },
  "retryable": true,
  "manual_entry_available": true
}
```

This failure is not the user’s fault. The interface can offer retry and manual entry without inventing a context payload.

[Open the provider-failure response as JSON](provider_error.json)

## Turn the contract into product decisions

For each response, record:

1. what the user sees;
2. which action is available next;
3. whether retry is safe;
4. what support or operations can inspect using `request_id`;
5. which analytics event would distinguish the state; and
6. what must remain under user or specialist control.

Use the [API State Worksheet](../templates/api_state_worksheet.md) to adapt this method to one bounded product behavior.

## Optional verification

After you understand the contract, the supplied Python check can confirm that the four JSON fixtures preserve the expected request ID, allowed states, validation details, retry rules, and failure boundaries:

```sh
python3 companion/api/validate_contract.py
```

Expected output:

```text
Chapter 2 API contract validation passed.
```

That pass proves the supplied teaching files are internally consistent. It does not call the fictional host or prove that a production API behaves correctly.
