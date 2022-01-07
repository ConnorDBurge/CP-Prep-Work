DROP TABLE IF EXISTS addresses CASCADE;
DROP TABLE IF EXISTS guardians CASCADE;
DROP TABLE IF EXISTS students CASCADE;

CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    line_1 VARCHAR(255) NOT NULL,
    line_2 VARCHAR(255) DEFAULT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zipcode VARCHAR(5) NOT NULL
); -- very important

CREATE TABLE guardians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    address INTEGER REFERENCES addresses(id)
); -- very important

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    grade VARCHAR(2) NOT NULL,
    dob DATE NOT NULL,
    guardian_id INTEGER REFERENCES guardians(id)
); -- very important