**Check Constraints**

- check constraints make sure there nothing else but given value in a row: `ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender ILIKE 'female' OR gender ILIKE 'male');`