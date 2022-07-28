**In**

- instead using this query `SELECT * FROM person WHERE country_of_birth = 'China' OR contry_of_birth = 'France' contry_of_birth = 'Brazil';`

- you can use `IN` as a list values: `SELECT * FROM person WHERE country_of_birth IN ('China','France','Brazil')`