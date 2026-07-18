.headers on
.mode column

.print '1. First five PG-rated films alphabetically'
SELECT title, rental_rate
FROM film
WHERE rating = 'PG'
ORDER BY title
LIMIT 5;

.print ''
.print '2. Film count by rating'
SELECT rating, COUNT(*) AS number_of_films
FROM film
GROUP BY rating
ORDER BY rating;

.print ''
.print '3. First five customer-to-title rows after the join'
SELECT c.first_name, c.last_name, f.title
FROM customer AS c
JOIN rental AS r ON c.customer_id = r.customer_id
JOIN inventory AS i ON r.inventory_id = i.inventory_id
JOIN film AS f ON i.film_id = f.film_id
ORDER BY c.customer_id, r.rental_date
LIMIT 5;

.print ''
.print '4. Frequently rented films relative to inventory copies'
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
.print '5. Recorded May 2005 rental revenue by store'
SELECT
    i.store_id,
    ROUND(SUM(p.amount), 2) AS recorded_rental_revenue
FROM rental AS r
JOIN payment AS p ON r.rental_id = p.rental_id
JOIN inventory AS i ON r.inventory_id = i.inventory_id
WHERE r.rental_date >= '2005-05-01'
  AND r.rental_date < '2005-06-01'
GROUP BY i.store_id
ORDER BY i.store_id;

.print ''
.print '6. Copies on open rental at the start of 1 June 2005'
SELECT
    i.store_id,
    COUNT(DISTINCT r.inventory_id) AS copies_on_open_rental
FROM rental AS r
JOIN inventory AS i ON r.inventory_id = i.inventory_id
WHERE r.rental_date < '2005-06-01'
  AND (
      r.return_date IS NULL
      OR r.return_date >= '2005-06-01'
  )
GROUP BY i.store_id
ORDER BY i.store_id;

.print ''
.print '7. Top five above-average customers by recorded spend'
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
.print '8. Film count by length category'
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
