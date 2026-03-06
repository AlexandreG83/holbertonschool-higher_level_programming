-- Lists all genres of the show Dexter
SELECT g.name
FROM tv_shows s
JOIN tv_show_genres tsg ON s.id = tsg.tv_show_id
JOIN genres g ON tsg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
