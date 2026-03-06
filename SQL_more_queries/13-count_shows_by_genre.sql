-- Lists all genres with the number of shows linked
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM g
JOIN tsg ON g.id = tsg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
