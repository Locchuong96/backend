**Upsert**

When your client do a request add new row into table, after that they want to edit and send a request again that is meaning we got 2 command insert table like that:

`INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.com') ON CONFLICT (id) DO NOTHING;`

and then you want change the email 'mytim@email.com' -> 'mytim@email.gov'

`INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.gov') ON CONFLICT (id) DO NOTHING;`

- you can use `DO UPDATE` if there is and conflict of id, like this: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.gov') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;`

- multi excluded: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.gov') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, first_name = EXCLUDED.first_name,last_name = EXCLUDED.last_name;`