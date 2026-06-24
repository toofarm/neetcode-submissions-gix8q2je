-- Write your query below
WITH cte AS (
    SELECT wimbledon FROM championships
    UNION ALL
    SELECT fr_open FROM championships
    UNION ALL
    SELECT us_open FROM championships
    UNION ALL 
    SELECT au_open FROM championships
)
SELECT a.player_id, a.player_name, 
    COUNT(b.wimbledon) AS grand_slams_count
FROM players a
LEFT JOIN cte b ON a.player_id = b.wimbledon
GROUP BY player_id
HAVING COUNT(b.wimbledon) > 0;