**Export csv with postgres**

- export to csv: `\copy (Query) TO Path DELIMITER ',' CSV HEADER;`

-example: `\copy (SELECT * FROM person LEFT JOIN car ON car.id = person.car_id) TO '/Users/PC/Desktop/postgresql/postgresql55/person.csv' DELIMITER ',' CSV HEADER;`