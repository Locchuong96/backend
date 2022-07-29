**On conflict do nothing**

When contraints
- when conflict do nothing: `ON CONFLICT ([column]) DO NOTHING;`

- full command: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.com') ON CONFLICT (id) DO NOTHING;`