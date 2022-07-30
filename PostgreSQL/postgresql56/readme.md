**Serial & Sequences**

- if you call this function the value will auto increase `SELECT * FROM nextval('person_id_seq'::regclass)`

- restart the value count of sequences table: `ALTER SEQUENCE person_id_seq RESTART WITH 10;`