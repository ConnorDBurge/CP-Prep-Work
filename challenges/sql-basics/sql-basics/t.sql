-- Finding a student record by name instead of id number
SELECT students.* FROM students
WHERE students.last_name = 'Sipes';

-- Listing all the students enrolled in a particular course
SELECT 
    students.last_name AS last, 
    students.first_name AS first 
FROM students
JOIN enrollments ON enrollments.student_id = students.id
JOIN classes ON enrollments.class_id = classes.id
WHERE classes.name = 'CS 101';

-- Finding the number of students whose birthday is in the next month
SELECT *
FROM students
WHERE birthdate 
    BETWEEN '1987-01-01' AND '1987-01-31';

-- Find > 3 credit classes ordered by their name in descending alpha order
SELECT * FROM classes
WHERE credits > 3
ORDER BY name ASC;

-- Find > 3 credit classes ordered by the number or credits, ascending
SELECT * FROM classes
WHERE credits > 3
ORDER BY credits ASC;

-- Retrieve students and their address in a single query
SELECT 
    students.id, 
    students.first_name, 
    students.last_name, 
    students.birthdate, 
    students.address_id, 
    addresses.line_1, 
    addresses.city, 
    addresses.state, 
    addresses.zipcode
FROM students
INNER JOIN addresses ON addresses.id = students.address_id;

-- Return all the students and any matching addresses
SELECT 
    students.id, 
    students.first_name, 
    students.last_name, 
    students.birthdate, 
    students.address_id, 
    addresses.line_1, 
    addresses.city, 
    addresses.state, 
    addresses.zipcode
FROM students
LEFT JOIN addresses ON addresses.id = students.address_id;

-- Query for students who live in Maryland
SELECT
    students.id,
    students.first_name, 
    students.last_name, 
    addresses.city, 
    addresses.state
FROM students
LEFT JOIN addresses ON addresses.id = students.address_id
WHERE addresses.state = 'Maryland';

-- UPDATE an address
UPDATE addresses 
SET 
    line_1 = '200 Church Street',
    city = 'Barrington',
    state = 'Illinois',
    zipcode = '60010'
WHERE
    id = 2;

-- Everyone gets an A!
UPDATE enrollments SET grade='A';