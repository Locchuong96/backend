**Adding and subtracting with dates**

- substract 1 year: `SELECT NOW() - INTERVAL '1 YEAR';`

- add 10 month: `SELECT NOW() + INERVAL '10 MONTH';`

- subtract 100 day: `SELECT NOW() - INTERVAL '100 DAYS';`

- add 100 days: `SELECT (NOW() + INTERVAL '100' DAYS)::DATE;`