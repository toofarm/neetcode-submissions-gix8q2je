-- Write your query below
SELECT a.first_name, a.last_name, COALESCE(b.city, NULL) AS city, COALESCE(b.state, NULL) AS state
FROM person a
LEFT JOIN address b USING(person_id);