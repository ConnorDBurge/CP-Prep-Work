-- Schema
DROP TABLE IF EXISTS students;
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
  st VARCHAR(255) NOT NULL,
  zipcode INTEGER NOT NULL
);
CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  class_name VARCHAR(255) NOT NULL,
  cedits VARCHAR(255)
);
CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  class_id INTEGER NOT NULL,
  grade INTEGER NOT NULL
);
