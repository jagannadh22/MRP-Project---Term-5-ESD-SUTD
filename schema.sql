CREATE TABLE part_records (
    part_id SERIAL PRIMARY KEY,
    part_name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE bills_of_materials (
    bom_id SERIAL PRIMARY KEY,
    parent_part_id INT REFERENCES part_records(part_id),
    child_part_id INT REFERENCES part_records(part_id),
    quantity INT NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    part_id INT REFERENCES part_records(part_id),
    quantity INT NOT NULL,
    order_date DATE NOT NULL
);

CREATE TABLE inventory (
    part_id INT REFERENCES part_records(part_id),
    quantity INT NOT NULL,
    PRIMARY KEY (part_id)
);

CREATE TABLE routing (
    routing_id SERIAL PRIMARY KEY,
    part_id INT REFERENCES part_records(part_id),
    workcenter_id INT REFERENCES workcenters(workcenter_id),
    sequence INT NOT NULL
);

CREATE TABLE workcenters (
    workcenter_id SERIAL PRIMARY KEY,
    location VARCHAR(100) NOT NULL
);

BEGIN;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM bills_of_materials WHERE child_part_id = :part_id) THEN
        RAISE EXCEPTION 'Cannot delete part as it is being used in a BOM.';
    ELSE
        DELETE FROM part_records WHERE part_id = :part_id;
    END IF;
END $$;

COMMIT;
