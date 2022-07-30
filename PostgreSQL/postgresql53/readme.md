**Left Joins**

A left join B print out the columns from table A and B and the column from table A

- left join `SELECT * FROM person LEFT JOIN car ON car.id = peron.car_id;`

- find the different part: `SELECT * FROM person LEFT JOIN car ON person.car_id = car.id WHERE car.id = null;`or `WHERE car.* IS NULL;`