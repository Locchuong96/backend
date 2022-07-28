**Group by Having**

- Group by having meaning you can give a condition: `SELECT country_of_birth,COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 2 ORDER BY country_of_birth`

- More [Aggregate-functions](https://www.postgresql.org/docs/11/functions-aggregate.html): `Min`,`Max`,`Sum`,etc.