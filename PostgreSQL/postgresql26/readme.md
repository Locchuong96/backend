**Group by**

Group by meaning you choice a column as a index and re-structure the table follow it.

- count rows follow a column: `SELECT country_of_birth ,COUNT(*) FROM person GROUP BY contry_of_birth;`

- count rows follow a column sort by order: `SELECT country_of_birth ,COUNT(*) FROM person GROUP BY contry_of_birth ORDER BY country_of_birth;`