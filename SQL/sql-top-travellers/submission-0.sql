-- Write your query below
SELECT a.name, COALESCE(SUM(b.distance), 0) AS travelled_distance
FROM users a
LEFT JOIN rides b ON a.id = b.user_id
GROUP BY name
ORDER BY travelled_distance DESC, name ASC;