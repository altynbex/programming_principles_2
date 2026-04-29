-- ADD PHONE
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE name = p_name;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;

-- MOVE TO GROUP
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE gid INT;
DECLARE cid INT;
BEGIN
    SELECT id INTO gid FROM groups WHERE name = p_group;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group) RETURNING id INTO gid;
    END IF;

    SELECT id INTO cid FROM contacts WHERE name = p_name;

    UPDATE contacts SET group_id = gid WHERE id = cid;
END;
$$;

-- SEARCH (ALL FIELDS)
CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(id INT, name VARCHAR, email VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p || '%' OR c.email ILIKE '%' || p || '%' OR p.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

