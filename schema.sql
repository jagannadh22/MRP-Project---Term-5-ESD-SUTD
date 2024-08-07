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

