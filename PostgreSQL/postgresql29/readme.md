**Calculating Min,Max,Average**

- get all: `SELECT * FROM car;`
- get max value: `SELECT MAX(price) FROM car;`
- get min value: `SELECT MIN(price) FROM car;`
- get average value: `SELECT AVG(price) FROM car;`
- get average value: `SELECT ROUND(AVG(price)) FROM car;`
- get min or max value from a group by table: `SELECT make,model,MIN(price) FROM car GROUP BY make,model;` or `SELECT make,MAX(price) FROM car GROUP BY make;`