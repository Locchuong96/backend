**Limit, Offset & Fetch**

- select every first 10 rows on the table `SELECT * FROM person LIMIT 10;`	

- select first 10 rows but offset 5 row first `SELECT * FROM person OFFSET 5 LIMIT 10;`

- select all but start from row 5th `SELECT * FROM person OFFSET 5;`

- select from row 5th take 10 rows `SELECT * FROM person OFFSET 5 FETCH 10 ROW ONLY;`

- select the first row `SELECT * FROM person OFFSET 5 FETCH FIRST 1 ROW ONLY;`

- select the first row `SELECT * FROM person OFFSET 5 FETCH FIRST ROW ONLY;`