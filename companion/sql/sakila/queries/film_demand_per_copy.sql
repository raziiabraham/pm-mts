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
