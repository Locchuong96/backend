**Arithmetic Operators - Round**

- query all rows: `SELECT id,make,model,price FROM car;`

- query and create new column `price*.10`: `SELECT id,make,model,price,price*0.10 FROM car;`

- round the query: `SELECT id,make,model,price,ROUND(price*0.10) FROM car;`

- round the query with 2 decimal: `SELECT id,make,model,price,ROUND(price*0.10,2) FROM car;`

- discount `10%`: `SELECT id,make,model,price,ROUND(price - price*0.1,2) FROM car;`