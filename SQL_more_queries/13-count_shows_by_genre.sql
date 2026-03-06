-- Lists all genres with the number of shows linked
SELECT g.name AS genre, COUNT(tsg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
