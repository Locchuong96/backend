**Inner Joins**

inner joins for combine 2 table together. print out the column table A and table B

C = A AND B

- join by forgein key: `SELECT * FROM person JOIN car ON person.car_id = car.id;`

- expand view `\x`

- select specific column form the table `SELECT person.first_name,person.last_name,person.gender, car.make,car.model FROM person JOIN car ON person.card_id = car.id;`