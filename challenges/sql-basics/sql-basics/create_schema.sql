-- Schema
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS addresses CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS enrollments CASCADE;

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  birthdate DATE NOT NULL,
  address_id INTEGER
);

CREATE TABLE addresses (
  id SERIAL PRIMARY KEY,
  line_1 VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zipcode VARCHAR(255) NOT NULL
);

CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  credits INTEGER
);

CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES students(id),
  class_id INTEGER REFERENCES classes(id),
  grade VARCHAR(12)
);

-- seeds databse using seed_data.sql file
\i seed_data.sql