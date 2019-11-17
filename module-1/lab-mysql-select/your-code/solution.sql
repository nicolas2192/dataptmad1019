/*Challenge 1*/
SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title, publishers.pub_name
FROM authors
LEFT JOIN titleauthor ON authors.au_id=titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id=titles.title_id
INNER JOIN publishers ON titles.pub_id=publishers.pub_id
ORDER BY authors.au_id DESC;

/*Challenge 2*/
SELECT joint.au_id, joint.au_lname, joint.au_fname, joint.pub_name, count(joint.title_id)
FROM
(
SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title_id, titles.title, publishers.pub_name, publishers.pub_id
FROM authors
LEFT JOIN titleauthor ON authors.au_id=titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id=titles.title_id
INNER JOIN publishers ON titles.pub_id=publishers.pub_id
) as joint
GROUP BY joint.au_id, joint.pub_id
ORDER BY joint.au_id DESC;

/*Challenge 3*/
WITH titau AS
	(
	SELECT titleauthor.au_id, titles.title_id, sum(sales.qty) AS total
	FROM titles
	INNER JOIN titleauthor ON titles.title_id=titleauthor.title_id
	INNER JOIN sales ON titles.title_id=sales.title_id
	GROUP BY titleauthor.au_id, titleauthor.title_id
	) 
SELECT titau.au_id, authors.au_lname, authors.au_fname, sum(titau.total) AS tot
FROM titau
LEFT JOIN authors ON titau.au_id=authors.au_id
GROUP BY titau.au_id
ORDER BY tot DESC
LIMIT 3;

/*Challenge 4*/
WITH titau AS
	(
	SELECT titleauthor.au_id, titles.title_id, sum(sales.qty) AS total
	FROM titles
	LEFT JOIN titleauthor ON titles.title_id=titleauthor.title_id
	LEFT JOIN sales ON titles.title_id=sales.title_id
	GROUP BY titleauthor.au_id, titleauthor.title_id
	) 
SELECT titau.au_id, authors.au_lname, authors.au_fname, sum(titau.total) AS tot
FROM titau
LEFT JOIN authors ON titau.au_id=authors.au_id
GROUP BY titau.au_id
ORDER BY tot DESC;




