**Where Clause and AND**

- We use where clause to select row follow a conditions 

`SELECT * FROM person WHERE gender = 'Female';`

`SELECT * FROM person WHERR gender = 'Male';`

- We can also add multi condition with `AND` or `OR`

`SELECT * FROM person WHERE gender = 'Male' AND country_of_birth = 'Poland'`

`SELECT * FROM person WHERE country_of_birth = 'China' OR country_of_birth = 'Poland'`

`SELECT * FROM person WHERE gender = 'Male' AND (country_of_birth = 'Poland' OR country_of_birth ='China') AND last_name = 'Pietersma'`
