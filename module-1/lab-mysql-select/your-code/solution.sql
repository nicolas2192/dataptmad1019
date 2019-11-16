/*Challenge 1*/
SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title, publishers.pub_name
FROM authors
LEFT JOIN titleauthor ON authors.au_id=titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id=titles.title_id
INNER JOIN publishers ON titles.pub_id=publishers.pub_id
ORDER BY authors.au_id DESC;

/*Challenge 2*/
CREATE TABLE tt as
SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title_id, titles.title, publishers.pub_name, publishers.pub_id
FROM authors
LEFT JOIN titleauthor ON authors.au_id=titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id=titles.title_id
INNER JOIN publishers ON titles.pub_id=publishers.pub_id
ORDER BY authors.au_id DESC;

SELECT *, count(title_id)
FROM tt
GROUP BY au_id
ORDER BY au_id DESC;





