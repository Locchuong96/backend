**Like and iLike**

- `%` Meaning any value

- select rows where the value of specific column likely a value: `SELECT * FROM person WHERE email LIKE '%.com';` or `SELECT * FROM person WHERE email LIKE '%bloomberg.com';` 

- select follow `%`: `SELECT * FROM person WHERE email LIKE '%google.%';`

- select follow number of charater`_`: `SELECT * FROM person WHERE email LIKE '%_____@%';`