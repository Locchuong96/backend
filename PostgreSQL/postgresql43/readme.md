**Unique Constrains**

Unique constrain make sure in the column every row have a unique value.

`SELECT email,COUNT(*) FROM person GROUP BY email;`

`SELECT email,COUNT(*) FROM person GROUP BY email HAVING COUNT(*) > 1;`

- add unique constrain for a column or multi column: `ALTER TABLE [name_of_table] ADD CONSTRAINT [name_of_constrain] UNIQUE ([column1],[column2])` example: `ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE(email);`

- the other way to ad constrain: `ALTER TABLE person UNIQUE(email);`

- delete conflict `DELETE FROM person WHERE email = 'gweaving@wisc.edu';`

- delete the constraint `ALTER TABLE person DROP CONSTRAINT unique_email_address;`