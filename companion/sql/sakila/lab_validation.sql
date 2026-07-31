.bail on

SELECT title, rental_rate
FROM film
WHERE rating = 'PG'
LIMIT 5;

SELECT rating, COUNT(*) AS number_of_films
FROM film
GROUP BY rating;

SELECT
    DATE(rental.rental_date) AS rental_day,
    inventory.store_id AS store_id,
    SUM(payment.amount) AS daily_rental_revenue
FROM rental
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
WHERE rental.rental_date >= '2005-05-01'
  AND rental.rental_date < '2005-06-01'
GROUP BY 1, 2;

SELECT
    DATE(rental_date) AS rental_day,
    country.country,
    COUNT(DISTINCT rental.customer_id) AS active_users
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE rental_date >= '2005-05-01'
  AND rental_date < '2005-06-01'
GROUP BY 1, 2;

WITH customer_spend AS (
    SELECT
        customer_id,
        SUM(amount) AS total_spend
    FROM payment
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.email,
    cs.total_spend
FROM customer AS c
JOIN customer_spend AS cs
    ON c.customer_id = cs.customer_id
WHERE cs.total_spend > (
    SELECT AVG(total_spend)
    FROM customer_spend
);
