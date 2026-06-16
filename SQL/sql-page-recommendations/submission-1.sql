-- Write your query below
WITH cte AS (
    SELECT user2_id AS user_id
    FROM friendship
    WHERE user1_id = 1
    UNION
    SELECT user1_id AS user_id
    FROM friendship
    WHERE user2_id = 1
),
cte2 AS (
    SELECT DISTINCT b.page_id AS page
    FROM cte a
    INNER JOIN likes b USING(user_id)
)
SELECT page AS recommended_page
FROM cte2
WHERE page NOT IN (
    SELECT page_id
    FROM likes
    WHERE user_id = 1
)
ORDER BY recommended_page ASC;