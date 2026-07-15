.headers off
.mode list
.separator |

CREATE TABLE film (
    film_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    rating TEXT NOT NULL,
    rental_rate NUMERIC NOT NULL,
    length INTEGER NOT NULL
);
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    store_id INTEGER NOT NULL
);
CREATE TABLE country (
    country_id INTEGER PRIMARY KEY,
    country TEXT NOT NULL
);
CREATE TABLE city (
    city_id INTEGER PRIMARY KEY,
    country_id INTEGER NOT NULL
);
CREATE TABLE address (
    address_id INTEGER PRIMARY KEY,
    city_id INTEGER NOT NULL
);
CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    address_id INTEGER NOT NULL
);
CREATE TABLE rental (
    rental_id INTEGER PRIMARY KEY,
    rental_date TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    inventory_id INTEGER NOT NULL
);
CREATE TABLE payment (
    payment_id INTEGER PRIMARY KEY,
    rental_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    amount NUMERIC NOT NULL
);

INSERT INTO film VALUES
    (1, 'River', 'PG', 2.99, 50),
    (2, 'Mountain', 'PG', 3.99, 90),
    (3, 'City', 'R', 4.99, 130);
INSERT INTO inventory VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 1);
INSERT INTO country VALUES (1, 'Australia'), (2, 'Indonesia');
INSERT INTO city VALUES (1, 1), (2, 2);
INSERT INTO address VALUES (1, 1), (2, 2);
INSERT INTO customer VALUES
    (1, 'a@example.test', 'Ari', 'One', 1),
    (2, 'b@example.test', 'Bela', 'Two', 2);
INSERT INTO rental VALUES
    (1, '2005-05-01 09:00:00', 1, 1),
    (2, '2005-05-02 10:00:00', 1, 2),
    (3, '2005-05-02 11:00:00', 2, 3),
    (4, '2005-06-01 08:00:00', 2, 1);
INSERT INTO payment VALUES
    (1, 1, 1, 5.00),
    (2, 2, 1, 7.00),
    (3, 3, 2, 3.00),
    (4, 4, 2, 11.00);

SELECT 'rating_counts';
SELECT rating, COUNT(*) AS number_of_films
FROM film
GROUP BY rating
ORDER BY rating;

SELECT 'daily_rental_revenue';
SELECT
    DATE(rental.rental_date) AS rental_day,
    inventory.store_id AS store_id,
    SUM(payment.amount) AS daily_rental_revenue
FROM rental
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
WHERE rental.rental_date >= '2005-05-01'
  AND rental.rental_date < '2005-06-01'
GROUP BY 1, 2
ORDER BY 1, 2;

SELECT 'daily_active_users';
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
GROUP BY 1, 2
ORDER BY 1, 2;

SELECT 'customers_above_average_total';
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
)
ORDER BY c.customer_id;
