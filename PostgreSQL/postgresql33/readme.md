**Alias**

- if you create a new column and don't give it a name, `postgres` will auto give it a name as the name of function `ROUND` or `?column?`

- you can you `alias` keyword to give the new column a new, or rename a column: `SELECT id,make,price AS original_price,ROUND(price - price*0.1) AS discount_price FROM car;`