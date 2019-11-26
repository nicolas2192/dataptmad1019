/* Challenge 1 */
WITH step1 as
(
	SELECT titleauthor.title_id, titleauthor.au_id, 
	(titles.advance * titleauthor.royaltyper / 100) as advance,
	(titles.price * sales.qty * titles.royalty / 100) as sales_royalty
	FROM titles 
	INNER JOIN titleauthor ON titles.title_id=titleauthor.title_id
	INNER JOIN sales ON titles.title_id=sales.title_id
),
step2 as
(
	SELECT step1.title_id, step1.au_id, sum(step1.advance) as total_adv, round(sum(step1.sales_royalty),2) as tot_ryt
	FROM step1
	GROUP BY step1.au_id, step1.title_id
	ORDER BY step1.au_id
)
SELECT step2.title_id, step2.au_id, step2.total_adv, step2.tot_ryt,
(step2.total_adv + step2.tot_ryt) as profit
FROM step2
ORDER BY profit DESC
LIMIT 3;



/* Challenge 2 */
CREATE TEMPORARY TABLE IF NOT EXISTS step1 AS
SELECT titleauthor.title_id, titleauthor.au_id, 
(titles.advance * titleauthor.royaltyper / 100) as advance,
(titles.price * sales.qty * titles.royalty / 100) as sales_royalty
FROM titles 
INNER JOIN titleauthor ON titles.title_id=titleauthor.title_id
INNER JOIN sales ON titles.title_id=sales.title_id


CREATE TEMPORARY TABLE IF NOT EXISTS step2 AS
SELECT step1.title_id, step1.au_id, sum(step1.advance) as total_adv, round(sum(step1.sales_royalty),2) as tot_ryt
FROM step1
GROUP BY step1.au_id, step1.title_id
ORDER BY step1.au_id

SELECT step2.title_id, step2.au_id, step2.total_adv, step2.tot_ryt,
(step2.total_adv + step2.tot_ryt) as profit
FROM step2
ORDER BY profit DESC
LIMIT 3;


/* Challenge 3 */
CREATE TABLE IF NOT EXISTS most_profiting_authors AS
SELECT step2.au_id, (step2.total_adv + step2.tot_ryt) as profit
FROM step2
ORDER BY profit DESC
LIMIT 3;




