-- Chapter 5 worked examples, in chapter order.
-- GENERATED from drafts/chapter_05_sql_product_reality.md by
-- scripts/sync_chapter_5_examples.py -- do not hand-edit; the book's printed
-- results are verified against the rows these queries return.

.headers on
.mode column

.print ''
.print 'Example 1: SELECT title, rental_rate FROM film WHERE rating = ''PG'' ORDER BY'
SELECT title, rental_rate
FROM film
WHERE rating = 'PG'
ORDER BY title
LIMIT 5;

.print ''
.print 'Example 2: SELECT (SELECT COUNT(*) FROM film) AS titles, (SELECT COUNT(*) F'
SELECT
    (SELECT COUNT(*) FROM film) AS titles,
    (SELECT COUNT(*) FROM category) AS categories,
    (SELECT COUNT(DISTINCT rating) FROM film) AS ratings;

.print ''
.print 'Example 3: SELECT rating, COUNT(*) AS number_of_films FROM film GROUP BY ra'
SELECT rating, COUNT(*) AS number_of_films
FROM film
GROUP BY rating
ORDER BY rating;

.print ''
.print 'Example 4: SELECT c.first_name, c.last_name, f.title FROM customer AS c JOI'
SELECT
    c.first_name,
    c.last_name,
    f.title
FROM customer AS c
JOIN rental AS r
    ON c.customer_id = r.customer_id
JOIN inventory AS i
    ON r.inventory_id = i.inventory_id
JOIN film AS f
    ON i.film_id = f.film_id
ORDER BY c.customer_id, r.rental_date
LIMIT 5;

.print ''
.print 'Example 5: SELECT f.title, COUNT(r.rental_id) AS rentals FROM film AS f JOI'
SELECT f.title, COUNT(r.rental_id) AS rentals
FROM film AS f
JOIN inventory AS i ON i.film_id = f.film_id
JOIN rental AS r ON r.inventory_id = i.inventory_id
GROUP BY f.film_id, f.title
ORDER BY rentals DESC, f.title
LIMIT 5;

.print ''
.print 'Example 6: SELECT COUNT(*) AS titles_with_no_copy FROM film AS f WHERE NOT '
SELECT COUNT(*) AS titles_with_no_copy
FROM film AS f
WHERE NOT EXISTS (
    SELECT 1
    FROM inventory AS i
    WHERE i.film_id = f.film_id
);

.print ''
.print 'Example 7: SELECT f.title, c.name AS category FROM film AS f JOIN film_cate'
SELECT f.title, c.name AS category
FROM film AS f
JOIN film_category AS fc ON fc.film_id = f.film_id
JOIN category AS c ON c.category_id = fc.category_id
WHERE NOT EXISTS (
    SELECT 1 FROM inventory AS i WHERE i.film_id = f.film_id
)
ORDER BY f.title
LIMIT 5;

.print ''
.print 'Example 8: SELECT i.store_id, ROUND(SUM(p.amount), 2) AS recorded_rental_re'
SELECT
    i.store_id,
    ROUND(SUM(p.amount), 2) AS recorded_rental_revenue
FROM rental AS r
JOIN payment AS p
    ON r.rental_id = p.rental_id
JOIN inventory AS i
    ON r.inventory_id = i.inventory_id
WHERE r.rental_date >= '2005-05-01'
  AND r.rental_date < '2005-06-01'
GROUP BY i.store_id
ORDER BY i.store_id;

.print ''
.print 'Example 9: SELECT i.store_id, COUNT(DISTINCT r.inventory_id) AS copies_on_o'
SELECT
    i.store_id,
    COUNT(DISTINCT r.inventory_id) AS copies_on_open_rental
FROM rental AS r
JOIN inventory AS i
    ON r.inventory_id = i.inventory_id
WHERE r.rental_date < '2005-06-01'
  AND (
      r.return_date IS NULL
      OR r.return_date >= '2005-06-01'
  )
GROUP BY i.store_id
ORDER BY i.store_id;

.print ''
.print 'Example 10: WITH customer_spend AS ( SELECT customer_id, SUM(amount) AS tota'
WITH customer_spend AS (
    SELECT
        customer_id,
        SUM(amount) AS total_spend
    FROM payment
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer,
    ROUND(cs.total_spend, 2) AS total_spend
FROM customer AS c
JOIN customer_spend AS cs
    ON c.customer_id = cs.customer_id
WHERE cs.total_spend > (
    SELECT AVG(total_spend)
    FROM customer_spend
)
ORDER BY cs.total_spend DESC, c.customer_id
LIMIT 5;

.print ''
.print 'Example 11: WITH shelving AS ( SELECT f.film_id, MAX(CASE WHEN i.store_id = '
WITH shelving AS (
    SELECT
        f.film_id,
        MAX(CASE WHEN i.store_id = 1 THEN 1 ELSE 0 END) AS at_store_1,
        MAX(CASE WHEN i.store_id = 2 THEN 1 ELSE 0 END) AS at_store_2
    FROM film AS f
    LEFT JOIN inventory AS i
        ON i.film_id = f.film_id
    GROUP BY f.film_id
)
SELECT
    CASE
        WHEN at_store_1 = 1 AND at_store_2 = 1 THEN 'both stores'
        WHEN at_store_1 = 1 THEN 'store 1 only'
        WHEN at_store_2 = 1 THEN 'store 2 only'
        ELSE 'neither store'
    END AS availability,
    COUNT(*) AS titles
FROM shelving
GROUP BY availability
ORDER BY titles DESC;

.print ''
.print 'Example 12: SELECT CASE WHEN length < 60 THEN ''Short'' WHEN length BETWEEN 60'
SELECT
    CASE
        WHEN length < 60 THEN 'Short'
        WHEN length BETWEEN 60 AND 120 THEN 'Medium'
        ELSE 'Long'
    END AS film_length_category,
    COUNT(*) AS number_of_films
FROM film
GROUP BY film_length_category
ORDER BY MIN(length);

.print ''
.print 'Example 13: WITH shelving AS ( SELECT f.film_id, MAX(CASE WHEN i.store_id = '
WITH shelving AS (
    SELECT
        f.film_id,
        MAX(CASE WHEN i.store_id = 1 THEN 1 ELSE 0 END) AS at_store_1,
        MAX(CASE WHEN i.store_id = 2 THEN 1 ELSE 0 END) AS at_store_2,
        COUNT(DISTINCT i.inventory_id) AS copies
    FROM film AS f
    JOIN inventory AS i
        ON i.film_id = f.film_id
    GROUP BY f.film_id
),
demand AS (
    SELECT i.film_id, COUNT(r.rental_id) AS rentals
    FROM inventory AS i
    LEFT JOIN rental AS r
        ON r.inventory_id = i.inventory_id
    GROUP BY i.film_id
)
SELECT
    CASE
        WHEN at_store_1 = 1 AND at_store_2 = 1 THEN 'both stores'
        ELSE 'one store only'
    END AS shelving_group,
    COUNT(*) AS titles,
    SUM(d.rentals) AS rentals,
    ROUND(AVG(CAST(d.rentals AS REAL) / s.copies), 2) AS avg_rentals_per_copy
FROM shelving AS s
JOIN demand AS d
    ON d.film_id = s.film_id
GROUP BY shelving_group
ORDER BY titles DESC;

.print ''
.print 'Example 14: WITH film_performance AS ( SELECT f.film_id, f.title, COUNT(DIST'
WITH film_performance AS (
    SELECT
        f.film_id,
        f.title,
        COUNT(DISTINCT i.inventory_id) AS inventory_copies,
        COUNT(r.rental_id) AS recorded_rentals
    FROM film AS f
    JOIN inventory AS i
        ON i.film_id = f.film_id
    LEFT JOIN rental AS r
        ON r.inventory_id = i.inventory_id
    GROUP BY f.film_id, f.title
)
SELECT
    title,
    inventory_copies,
    recorded_rentals,
    ROUND(1.0 * recorded_rentals / inventory_copies, 2)
        AS rentals_per_copy
FROM film_performance
WHERE inventory_copies >= 4
ORDER BY rentals_per_copy DESC, recorded_rentals DESC, title
LIMIT 5;

.print ''
.print 'Example 15: WITH shelving AS ( SELECT f.film_id, f.title, MAX(CASE WHEN i.st'
WITH shelving AS (
    SELECT
        f.film_id,
        f.title,
        MAX(CASE WHEN i.store_id = 1 THEN 1 ELSE 0 END) AS at_store_1,
        MAX(CASE WHEN i.store_id = 2 THEN 1 ELSE 0 END) AS at_store_2,
        COUNT(DISTINCT i.inventory_id) AS copies
    FROM film AS f
    JOIN inventory AS i
        ON i.film_id = f.film_id
    GROUP BY f.film_id, f.title
),
demand AS (
    SELECT i.film_id, COUNT(r.rental_id) AS rentals
    FROM inventory AS i
    LEFT JOIN rental AS r
        ON r.inventory_id = i.inventory_id
    GROUP BY i.film_id
)
SELECT
    s.title,
    CASE WHEN s.at_store_1 = 1 THEN 'store 1' ELSE 'store 2' END AS stocked_at,
    s.copies,
    d.rentals,
    ROUND(1.0 * d.rentals / s.copies, 2) AS rentals_per_copy
FROM shelving AS s
JOIN demand AS d
    ON d.film_id = s.film_id
WHERE s.at_store_1 + s.at_store_2 = 1
  AND s.copies >= 4
ORDER BY rentals_per_copy DESC, s.title
LIMIT 5;
