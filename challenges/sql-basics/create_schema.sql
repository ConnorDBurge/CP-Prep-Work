-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  birthdate DATE NOT NULL,
  address_id INTEGER
);
DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
  id SERIAL PRIMARY KEY,
  line_1 VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zipcode INTEGER NOT NULL
);
DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  credits VARCHAR(255)
);
DROP TABLE IF EXISTS enrollments;
CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  class_id INTEGER NOT NULL,
  grade VARCHAR(255)
);
