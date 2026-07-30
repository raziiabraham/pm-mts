-- Chapter 5 worked examples, in chapter order.
-- GENERATED from drafts/chapter_05_sql_product_reality.md by
-- scripts/sync_chapter_5_examples.py -- do not hand-edit; the book's printed
-- results are verified against the rows these queries return.

.headers on
.mode column

.print ''
.print 'Example 1: SELECT title, is_published FROM documents WHERE is_published = 1'
SELECT title, is_published
FROM documents
WHERE is_published = 1
ORDER BY title
LIMIT 5;

.print ''
.print 'Example 2: SELECT (SELECT COUNT(*) FROM users) AS users, (SELECT SUM(messag'
SELECT
    (SELECT COUNT(*) FROM users) AS users,
    (SELECT SUM(message_count) FROM coworker_messages)
        AS coworker_messages,
    (SELECT COUNT(*) FROM documents) AS documents,
    (SELECT COUNT(*) FROM documents WHERE is_published = 1)
        AS published;

.print ''
.print 'Example 3: SELECT is_published, COUNT(*) AS documents FROM documents GROUP '
SELECT is_published, COUNT(*) AS documents
FROM documents
GROUP BY is_published
ORDER BY is_published;

.print ''
.print 'Example 4: SELECT COUNT(*) AS rows_returned, COUNT(DISTINCT u.user_id) AS u'
SELECT
    COUNT(*) AS rows_returned,
    COUNT(DISTINCT u.user_id) AS users,
    SUM(m.message_count) AS summed_messages
FROM users AS u
JOIN documents AS d
    ON d.user_id = u.user_id
JOIN coworker_messages AS m
    ON m.user_id = u.user_id
WHERE u.user_id = 'cohort_power_01';

.print ''
.print 'Example 5: SELECT d.title, f.name, f.mime_type FROM documents AS d JOIN fil'
SELECT d.title, f.name, f.mime_type
FROM documents AS d
JOIN files AS f
    ON f.document_id = d.document_id
WHERE d.user_id = 'cohort_power_01'
ORDER BY d.document_id
LIMIT 5;

.print ''
.print 'Example 6: SELECT u.persona, COUNT(DISTINCT u.user_id) AS users, SUM(m.mess'
SELECT
    u.persona,
    COUNT(DISTINCT u.user_id) AS users,
    SUM(m.message_count) AS messages
FROM users AS u
JOIN coworker_messages AS m
    ON m.user_id = u.user_id
JOIN documents AS d
    ON d.user_id = u.user_id
GROUP BY u.persona
ORDER BY users DESC, u.persona;

.print ''
.print 'Example 7: WITH per_user AS ( SELECT u.user_id, u.persona, m.message_count,'
WITH per_user AS (
    SELECT
        u.user_id,
        u.persona,
        m.message_count,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id) AS documents,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id
            AND d.is_published = 1) AS published
    FROM users AS u
    JOIN coworker_messages AS m
        ON m.user_id = u.user_id
)
SELECT
    persona,
    COUNT(*) AS users,
    SUM(message_count) AS messages,
    SUM(documents) AS documents,
    SUM(published) AS published
FROM per_user
GROUP BY persona
ORDER BY messages DESC;

.print ''
.print 'Example 8: SELECT COUNT(*) AS engaged_users_never_published FROM coworker_m'
SELECT COUNT(*) AS engaged_users_never_published
FROM coworker_messages AS m
WHERE m.message_count >= 20
  AND NOT EXISTS (
      SELECT 1
      FROM documents AS d
      WHERE d.user_id = m.user_id
        AND d.is_published = 1
  );

.print ''
.print 'Example 9: SELECT CASE WHEN published > 0 THEN ''published at least once'' WH'
SELECT
    CASE
        WHEN published > 0 THEN 'published at least once'
        WHEN messages >= 20 THEN 'chatting, never published'
        WHEN documents > 0 THEN 'drafting, barely chatting'
        ELSE 'signed up only'
    END AS activation_state,
    COUNT(*) AS users
FROM (
    SELECT
        u.user_id,
        m.message_count AS messages,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id) AS documents,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id
            AND d.is_published = 1) AS published
    FROM users AS u
    JOIN coworker_messages AS m
        ON m.user_id = u.user_id
)
GROUP BY activation_state
ORDER BY users DESC;

.print ''
.print 'Example 10: WITH per_user AS ( SELECT user_id, message_count FROM coworker_m'
WITH per_user AS (
    SELECT user_id, message_count
    FROM coworker_messages
)
SELECT
    COUNT(*) AS users_above_average,
    (SELECT ROUND(AVG(message_count), 1) FROM per_user)
        AS average_messages
FROM per_user
WHERE message_count > (
    SELECT AVG(message_count) FROM per_user
);

.print ''
.print 'Example 11: WITH per_user AS ( SELECT u.user_id, u.persona, (SELECT COUNT(*)'
WITH per_user AS (
    SELECT
        u.user_id,
        u.persona,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id) AS documents,
        (SELECT COUNT(*) FROM documents AS d
          WHERE d.user_id = u.user_id
            AND d.is_published = 1) AS published
    FROM users AS u
)
SELECT
    persona,
    COUNT(*) AS users,
    SUM(published) AS published,
    ROUND(1.0 * SUM(published) / COUNT(*), 2)
        AS published_per_user,
    ROUND(100.0 * SUM(published) / SUM(documents), 1)
        AS pct_of_drafts_published
FROM per_user
GROUP BY persona
ORDER BY published_per_user DESC;

.print ''
.print 'Example 12: WITH per_persona AS ( SELECT u.persona, (SELECT SUM(m.message_co'
WITH per_persona AS (
    SELECT
        u.persona,
        (SELECT SUM(m.message_count)
           FROM coworker_messages AS m
           JOIN users AS x ON x.user_id = m.user_id
          WHERE x.persona = u.persona) AS messages,
        (SELECT COUNT(*)
           FROM documents AS d
           JOIN users AS x ON x.user_id = d.user_id
          WHERE x.persona = u.persona
            AND d.is_published = 1) AS published
    FROM users AS u
    GROUP BY u.persona
)
SELECT
    persona,
    messages,
    published,
    CASE
        WHEN published = 0 THEN NULL
        ELSE ROUND(1.0 * messages / published, 0)
    END AS messages_per_published
FROM per_persona
ORDER BY messages_per_published;

.print ''
.print 'Example 13: SELECT COUNT(*) AS private_drafts, COUNT(DISTINCT user_id) AS us'
SELECT
    COUNT(*) AS private_drafts,
    COUNT(DISTINCT user_id) AS users
FROM documents AS d
WHERE d.is_published = 0
  AND d.is_archived = 0
  AND NOT EXISTS (
      SELECT 1
      FROM documents AS p
      WHERE p.user_id = d.user_id
        AND p.is_published = 1
  );

.print ''
.print 'Example 14: SELECT u.persona, COUNT(*) AS private_drafts, COUNT(DISTINCT d.u'
SELECT
    u.persona,
    COUNT(*) AS private_drafts,
    COUNT(DISTINCT d.user_id) AS users
FROM documents AS d
JOIN users AS u
    ON u.user_id = d.user_id
WHERE d.is_published = 0
  AND d.is_archived = 0
  AND NOT EXISTS (
      SELECT 1
      FROM documents AS p
      WHERE p.user_id = d.user_id
        AND p.is_published = 1
  )
GROUP BY u.persona
ORDER BY private_drafts DESC;

.print ''
.print 'Example 15: SELECT (SELECT COUNT(*) FROM coworker_messages WHERE message_cou'
SELECT
    (SELECT COUNT(*) FROM coworker_messages
      WHERE message_count > 0) AS users_in_chat,
    (SELECT COUNT(DISTINCT user_id) FROM squad_agents)
        AS users_with_agent;
