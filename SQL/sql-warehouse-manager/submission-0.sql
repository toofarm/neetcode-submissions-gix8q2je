-- Write your query below
WITH cte AS (
    SELECT product_id, (width * height * length) AS volume
    FROM products
)
SELECT a.name AS warehouse_name, SUM(b.volume * a.units) AS volume
FROM warehouse a
LEFT JOIN cte b on a.product_id = b.product_id
GROUP BY a.name;