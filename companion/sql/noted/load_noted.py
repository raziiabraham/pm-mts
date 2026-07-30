#!/usr/bin/env python3
"""Build the Noted cohort SQLite database from the vendored snapshot.

Chapter 5 investigates a real product's records rather than a DVD-rental sample.
The rows come from Noted (the author's workspace product) via its own seeder,
`scripts/seed-convex.mjs`, which expands a fixture deterministically from
seed 20260518 — so the same rows, and therefore the same printed results, come
back every time. The snapshot in upstream/ is the seeder's output captured at
noted-main commit 985ad95, vendored so this companion needs no Convex deployment
and no network access.

The database carries BOTH halves of the same cohort, because the chapters split
along that seam:

  * Chapter 5 works the stored product records — the Convex tables. What the
    product wrote down.
  * Chapter 6 works the `events` table — the analytics stream Noted sends to
    Amplitude, from `scripts/seed-amplitude.mjs` (seed 20260519). What the
    product observed happening, with a timestamp on every row.

Same fifty users, same thirty-day window, two different kinds of record. A query
against `documents` says a document is published; a query against `events` says
when it was published and what the user did first.

The data is SYNTHETIC and the book says so. It is shaped to resemble a pattern
the author has seen in production, not discovered in the wild.

Two honest notes about the shape, both of which the chapter teaches:

1. Noted's Convex schema has NO users table. Identity lives in the auth provider,
   so `userId` is an opaque string and there is nothing in the product database to
   join to for user attributes. The `users` table built here is a DERIVED analytics
   dimension — exactly the table a real team has to build for itself — and the
   chapter is explicit that it did not come free with the product.

2. `files` attaches to documents by key, and in the live schema a file can carry an
   ARRAY of document ids. The relational export resolves the single-document case
   so the join is inspectable; the array case is the document-model wrinkle the
   chapter discusses rather than hides.

3. The event stream does NOT reconcile exactly with the product tables, on purpose.
   The constructed seed models incomplete client-side delivery from blockers,
   privacy settings, and beacons that do not flush, so the stream delivers about
   79–85% of what the tables recorded. That percentage is a teaching condition, not
   an estimate of real blocker prevalence or warehouse completeness. A seed that
   reconciled perfectly would hide the need to compare a stream with its product
   source. `reconcile_sources()` therefore pins the expected counts rather than
   demanding equality: it fails on drift, and it fails if analytics ever exceeds
   the product tables, which would mean double-counting rather than loss.

    python companion/sql/noted/load_noted.py [--database PATH]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "upstream" / "noted_cohort_rows.json"
EVENT_SNAPSHOT = HERE / "upstream" / "noted_cohort_events.json"
DEFAULT_DB = HERE / "noted.db"

SCHEMA = """
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS documents;
DROP TABLE IF EXISTS files;
DROP TABLE IF EXISTS coworker_messages;
DROP TABLE IF EXISTS squad_agents;
DROP TABLE IF EXISTS ai_settings;
DROP TABLE IF EXISTS user_storage;
DROP TABLE IF EXISTS users;

-- DERIVED. Noted's product database has no users table: identity lives in the
-- auth provider. This dimension is assembled for analysis, and the persona is
-- read out of the seeded userId. Treat it as a team-built table, not a product one.
CREATE TABLE users (
    user_id   TEXT PRIMARY KEY,
    persona   TEXT NOT NULL
);

CREATE TABLE documents (
    document_id  INTEGER PRIMARY KEY,
    user_id      TEXT NOT NULL REFERENCES users(user_id),
    title        TEXT NOT NULL,
    is_published INTEGER NOT NULL,
    is_archived  INTEGER NOT NULL
);

CREATE TABLE files (
    file_id     INTEGER PRIMARY KEY,
    user_id     TEXT NOT NULL REFERENCES users(user_id),
    document_id INTEGER REFERENCES documents(document_id),
    name        TEXT NOT NULL,
    mime_type   TEXT NOT NULL,
    size_bytes  INTEGER NOT NULL
);

-- One row per user: the seeder records a message COUNT per user rather than one
-- row per message. The event stream keeps per-message grain for Chapter 6.
CREATE TABLE coworker_messages (
    user_id       TEXT PRIMARY KEY REFERENCES users(user_id),
    message_count INTEGER NOT NULL
);

CREATE TABLE squad_agents (
    agent_id INTEGER PRIMARY KEY,
    user_id  TEXT NOT NULL REFERENCES users(user_id),
    name     TEXT NOT NULL
);

CREATE TABLE ai_settings (
    user_id         TEXT PRIMARY KEY REFERENCES users(user_id),
    active_provider TEXT,
    active_model    TEXT
);

CREATE TABLE user_storage (
    user_id    TEXT PRIMARY KEY REFERENCES users(user_id),
    bytes_used INTEGER NOT NULL
);

-- The analytics stream. One row per observed action, which is the whole
-- difference from the tables above: a document row says a document is published,
-- an event row says when. `occurred_at` is UTC text so SQLite date functions work,
-- and `occurred_on` is the day key most funnel and retention queries group by.
-- The promoted columns are the properties Chapter 6 uses; `properties` keeps the
-- full payload so nothing is lost, queryable with json_extract().
CREATE TABLE events (
    event_id       INTEGER PRIMARY KEY,
    user_id        TEXT NOT NULL REFERENCES users(user_id),
    event_type     TEXT NOT NULL,
    occurred_at    TEXT NOT NULL,
    occurred_on    TEXT NOT NULL,
    session_id     INTEGER,
    platform       TEXT,
    funnel_stage   TEXT,
    feature_area   TEXT,
    lifecycle_stage TEXT,
    plan_tier      TEXT,
    document_id    INTEGER REFERENCES documents(document_id),
    ai_provider    TEXT,
    page_path      TEXT,
    message_sequence INTEGER,
    properties     TEXT NOT NULL
);

CREATE INDEX events_user_idx ON events(user_id);
CREATE INDEX events_type_idx ON events(event_type);
CREATE INDEX events_day_idx ON events(occurred_on);
"""


def load_events(connection: sqlite3.Connection, document_id_by_key: dict[str, int]) -> None:
    """Load the Amplitude stream, sorted by time so event_id follows the clock."""
    events = json.loads(EVENT_SNAPSHOT.read_text(encoding="utf-8"))
    events.sort(key=lambda e: (e["time"], e["user_id"], e["event_type"]))

    rows = []
    for index, event in enumerate(events, start=1):
        props = event.get("event_properties", {})
        moment = dt.datetime.fromtimestamp(event["time"] / 1000, tz=dt.timezone.utc)
        rows.append(
            (
                index,
                event["user_id"],
                event["event_type"],
                moment.strftime("%Y-%m-%d %H:%M:%S"),
                moment.strftime("%Y-%m-%d"),
                event.get("session_id"),
                event.get("platform"),
                props.get("funnel_stage"),
                props.get("feature_area"),
                props.get("lifecycle_stage"),
                props.get("plan_tier"),
                document_id_by_key.get(props.get("document_seed_key")),
                props.get("ai_provider"),
                props.get("page_path"),
                props.get("message_sequence"),
                json.dumps(props, sort_keys=True),
            )
        )
    connection.executemany(
        "INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows
    )


# What the stream is expected to deliver against each product table. Pinned so a
# regenerated snapshot cannot quietly change a number the book has printed.
EXPECTED_DELIVERY = {
    "documents created": (
        "SELECT COUNT(*) FROM documents",
        "SELECT COUNT(*) FROM events WHERE event_type = 'Document Created'",
        243,
        203,
    ),
    # Net of withdrawals. A document published and later pulled reads as
    # unpublished in the tables while carrying both events in the stream, so
    # comparing raw publish events against the flag would count it twice.
    "documents published (net of withdrawals)": (
        "SELECT COUNT(*) FROM documents WHERE is_published = 1",
        "SELECT (SELECT COUNT(*) FROM events WHERE event_type = 'Document Published') "
        "- (SELECT COUNT(*) FROM events WHERE event_type = 'Document Unpublished')",
        35,
        28,
    ),
    "documents archived": (
        "SELECT COUNT(*) FROM documents WHERE is_archived = 1",
        "SELECT COUNT(*) FROM events WHERE event_type = 'Document Archived'",
        28,
        22,
    ),
    "coworker messages": (
        "SELECT SUM(message_count) FROM coworker_messages",
        "SELECT COUNT(*) FROM events WHERE event_type = 'Coworker Message Sent'",
        2895,
        2444,
    ),
}


def reconcile_sources(connection: sqlite3.Connection) -> None:
    """Check the two halves of the cohort against each other.

    The stream is expected to fall SHORT of the product tables — see note 3 — so
    this pins both sides instead of demanding they match. It fails on drift, and it
    fails if the stream ever exceeds the tables, which would mean double-counted
    events rather than lost ones.
    """
    for label, (product_sql, stream_sql, want_product, want_stream) in EXPECTED_DELIVERY.items():
        product = connection.execute(product_sql).fetchone()[0]
        stream = connection.execute(stream_sql).fetchone()[0]
        if (product, stream) != (want_product, want_stream):
            raise SystemExit(
                f"{label} drifted: product tables {product} (expected {want_product}), "
                f"event stream {stream} (expected {want_stream})"
            )
        if stream > product:
            raise SystemExit(
                f"{label}: the event stream ({stream}) exceeds the product tables "
                f"({product}), which means double-counting, not delivery loss"
            )

    orphans = connection.execute(
        "SELECT COUNT(*) FROM events e LEFT JOIN users u ON u.user_id = e.user_id "
        "WHERE u.user_id IS NULL"
    ).fetchone()[0]
    if orphans:
        raise SystemExit(f"{orphans} events reference a user that is not in the cohort")

    unresolved = connection.execute(
        "SELECT COUNT(*) FROM events "
        "WHERE event_type IN ('Document Created', 'Document Published', 'Document Archived', "
        "'Document Unpublished', 'Public Link Copied') AND document_id IS NULL"
    ).fetchone()[0]
    if unresolved:
        raise SystemExit(f"{unresolved} document events did not resolve to a document row")

    window = connection.execute("SELECT MIN(occurred_on), MAX(occurred_on) FROM events").fetchone()
    if window != ("2026-01-01", "2026-01-30"):
        raise SystemExit(f"event window drifted: {window[0]} .. {window[1]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", default=str(DEFAULT_DB))
    args = parser.parse_args()

    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    target = Path(args.database)
    target.unlink(missing_ok=True)

    connection = sqlite3.connect(target)
    connection.executescript(SCHEMA)

    connection.executemany(
        "INSERT INTO users VALUES (?, ?)",
        [(u["userId"], u["persona"]) for u in snapshot["users"]],
    )
    connection.executemany(
        "INSERT INTO ai_settings VALUES (?, ?, ?)",
        [(u["userId"], u.get("aiProvider"), u.get("aiModel")) for u in snapshot["users"]],
    )
    connection.executemany(
        "INSERT INTO user_storage VALUES (?, ?)",
        [(u["userId"], u.get("bytesUsed", 0)) for u in snapshot["users"]],
    )

    # Documents keep a stable id so files can reference them by their seed key.
    document_id_by_key: dict[str, int] = {}
    document_rows = []
    for index, doc in enumerate(snapshot["documents"], start=1):
        document_id_by_key[doc["seedKey"]] = index
        document_rows.append(
            (index, doc["userId"], doc["title"], int(doc["isPublished"]), int(doc["isArchived"]))
        )
    connection.executemany("INSERT INTO documents VALUES (?, ?, ?, ?, ?)", document_rows)

    connection.executemany(
        "INSERT INTO files VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                index,
                f["userId"],
                document_id_by_key.get(f.get("documentSeedKey")),
                f["name"],
                f["type"],
                f["size"],
            )
            for index, f in enumerate(snapshot["files"], start=1)
        ],
    )
    connection.executemany(
        "INSERT INTO coworker_messages VALUES (?, ?)",
        [(c["userId"], c["count"]) for c in snapshot["coworkerMessages"]],
    )
    connection.executemany(
        "INSERT INTO squad_agents VALUES (?, ?, ?)",
        [
            (index, a["userId"], a["name"])
            for index, a in enumerate(snapshot["squadAgents"], start=1)
        ],
    )
    load_events(connection, document_id_by_key)
    connection.commit()
    reconcile_sources(connection)

    counts = {
        table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in ("users", "documents", "files", "coworker_messages", "squad_agents",
                      "ai_settings", "user_storage", "events")
    }
    connection.close()
    print(f"Built {target}")
    print("  " + "  ".join(f"{k}={v}" for k, v in counts.items()))
    print(f"  provenance: noted-main {snapshot['provenance']['commit'][:7]}, "
          f"seed {snapshot['provenance']['seed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
