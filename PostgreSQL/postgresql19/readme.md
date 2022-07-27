**Order by**

- `ASC` meaning increase 1 2 3 4 5 (default)

- `DESC` meaning descrease 5 4 3 2 1

`ASC` and `DESC` both work for date,number,string

- select all order by specific column `SELECT * FROM person ORDER BY [column_name] DESC`
- select some columns order by specific column `SELECT [column1],[column2] FROM person ORDER BY [column3] DESC`
- select some columns order some specific columns `SELECT [column1],[column2] FROM person ORDER BY [column3],[column4] DESC`