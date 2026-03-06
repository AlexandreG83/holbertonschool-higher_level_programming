-- Lists all shows with the genre Comedy
SELECT s.title
FROM tv_shows s
JOIN tv_show_genres tsg ON s.id = tsg.tv_show_id
JOIN genres g ON tsg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
