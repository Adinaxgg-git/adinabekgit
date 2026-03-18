DROP TABLE IF EXISTS phonebook CASCADE;

CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

INSERT INTO phonebook(name, phone) VALUES
('Adina', '87001234567'),
('Ali', '87771234567'),
('Dana', '87005554433');

CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
    invalid TEXT := '';
BEGIN
    FOR i IN 1..array_length(names,1) LOOP
        
        IF phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO phonebook(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            invalid := invalid || names[i] || ' ';
        END IF;

    END LOOP;

    RAISE NOTICE 'Invalid users: %', invalid;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_phonebook_paginated(lim INT, off INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    ORDER BY id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$ LANGUAGE plpgsql;

-- TESTS

SELECT * FROM search_phonebook('Adi');

CALL upsert_user('Adina', '11111111111');

CALL insert_many_users(
    ARRAY['Test1','Test2'],
    ARRAY['87001234567','abc']
);

SELECT * FROM get_phonebook_paginated(2,0);

CALL delete_user('Test1');