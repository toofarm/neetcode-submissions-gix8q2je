-- Write your query below
SELECT sale_date, SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END) AS diff
FROM sales
GROUP BY sale_date
ORDER BY sale_date;