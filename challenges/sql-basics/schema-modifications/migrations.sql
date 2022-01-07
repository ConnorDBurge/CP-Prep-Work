DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id serial PRIMARY KEY,
    first text,
    last text,
    social varchar(255),
    account_number varchar(255),
    line_1 varchar(255),
    city varchar(255),
    state varchar(255),
    zip integer,
    current_balance_cents integer
);

DROP TABLE IF EXISTS statements;
CREATE TABLE statements (
    id serial PRIMARY KEY,
    customer_id integer,
    gallons_used integer,
    cents_per_gallon integer,
    start_date date,
    end_date date,
    status varchar(255),
    payment_date date,
    due_date date,
    amount_due_cents integer,
    min_amount_due_cents integer
);

-- Changing column names
ALTER TABLE customers 
    RENAME COLUMN first TO first_name;
ALTER TABLE customers 
    RENAME COLUMN last TO last_name;
    
-- Changing column types
ALTER TABLE customers 
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN social TYPE VARCHAR(9),
    ALTER COLUMN account_number TYPE VARCHAR(14),
    ALTER COLUMN zip TYPE VARCHAR(5);

-- Adding a new column
ALTER TABLE customers
    ADD line_2 VARCHAR(255);

-- Deleting a column
ALTER TABLE customers   
    DROP COLUMN current_balance_cents;

-- Changing column type
ALTER TABLE statements 
    ALTER COLUMN customer_id SET NOT NULL,
    ALTER COLUMN gallons_used TYPE DECIMAL,
    ALTER COLUMN status SET DEFAULT 'payment_due';
