**Coalesce**

is a result's option, return a greater value:

- `SELECT COALESCE(1);`

- `SELECT COALESCE(1) AS number;`

- `SELECT COALESCE(1,null) AS number;` -> 1

- `SELECT COALESCE(1,2) AS number;` -> 2

- `SELECT COALESCE(null,1,null) AS number;` -> 2

you can use `COALESCE` to give a default value: `SELECT COALESCE(email,'NO EMAIL') FROM car;`