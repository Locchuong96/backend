**NULLIF**

When you do the math `SELECT 10/0` -> division by zero error

But when you division with `null`, it will return `null`

- Return the first element if the 2 element is not equal `SELECT NULLIF(100,10);` -> 100

- Return null if they are equal `SELECT NULLIF(100,100);` -> null

- `SELECT 10 / NULLIF(0,0);` -> null 

- `SELECT COALESCE(10 / NULLIF(0,0),0);` -> 0 

