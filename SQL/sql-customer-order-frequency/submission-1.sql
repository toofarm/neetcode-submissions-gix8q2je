-- Write your query below
WITH cte AS (
    SELECT customer_id, product_id, quantity, EXTRACT( MONTH FROM order_date ) AS month_num,
        EXTRACT( YEAR FROM order_date ) AS year_num
    FROM orders
),
cte2 AS (
    SELECT a.customer_id, a.month_num, SUM(a.quantity * b.price) AS total
    FROM cte a
    LEFT JOIN product b USING(product_id)
    WHERE year_num = '2020'
    GROUP BY customer_id, month_num
),
cte3 AS (
    SELECT a.customer_id, b.name
    FROM cte2 a
    LEFT JOIN customers b USING(customer_id)
    WHERE month_num = 6 AND total > 99 OR month_num = 7 AND total > 99
),
cte4 AS (
    SELECT customer_id, name, COUNT(*) AS num
    FROM cte3
    GROUP BY customer_id, name
)
SELECT customer_id, name
FROM cte4
WHERE num > 1;