--Функция поиска по шаблону
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts
    WHERE name ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;



--Функция с pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, offs INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts
    ORDER BY id
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;