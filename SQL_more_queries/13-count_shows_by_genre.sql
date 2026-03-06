-- Lists all genres with the number of shows linked
SELECT tv_genre.name AS genre, COUNT(tv_show_genre.show_id) AS number_of_shows
FROM tv_genre
JOIN tv_show_genre ON tv_genre.id = tv_show_genre.genre_id
GROUP BY tv_genre.name
ORDER BY number_of_shows DESC;
