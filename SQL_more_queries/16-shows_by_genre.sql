-- Lists all shows and their genres, NULL if no genre
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres tsg ON s.id = tsg.tv_show_id
LEFT JOIN genres g ON tsg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
