CREATE TABLE table1 (
        message text
);
CREATE TABLE table2 (
        message text
);

--enable plpgsql
CREATE PROCEDURAL LANGUAGE plpgsql;

--define trigger function
CREATE FUNCTION notify_trigger() RETURNS trigger AS $$

DECLARE

BEGIN
 -- TG_TABLE_NAME is the name of the table who's trigger called this function
 -- TG_OP is the operation that triggered this function: INSERT, UPDATE or DELETE.
 execute 'NOTIFY ' || TG_TABLE_NAME || '_' || TG_OP;
 return new;
END;

$$ LANGUAGE plpgsql;

--Create Triggers
CREATE TRIGGER table1_trigger BEFORE insert or update or delete on table1 execute procedure notify_trigger();
CREATE TRIGGER table2_trigger BEFORE insert or update or delete on table2 execute procedure notify_trigger();
