-- Select all rows from the classes table
SELECT * FROM classes;

-- Select the name and credits from the classes table where the number of credits is greater than 3
SELECT name, credits FROM classes
WHERE credits > 3;

-- All rows from the classes table where credits is an even number
SELECT * FROM classes
WHERE credits % 2 = 0;

-- All of Tianna's enrollments that she hasn't yet received a grade for
SELECT * FROM enrollments
JOIN students ON students.id = enrollments.student_id
WHERE students.id = 1 AND enrollments.grade IS NULL;

-- All of Tianna's enrollments that she hasn't yet received a grade for, selected by her first name, not her student.id
SELECT * FROM enrollments
JOIN students ON students.id = enrollments.student_id
WHERE students.first_name = 'Tianna' AND enrollments.grade IS NULL;

-- All of Tianna's enrollments that she hasn't yet received a grade for, selected by her first name, not her student.id, with the class name included in the result set
SELECT classes.name FROM enrollments
JOIN students ON students.id = enrollments.student_id
JOIN classes ON enrollments.class_id = classes.id
WHERE 
    students.first_name = 'Tianna' AND 
    enrollments.grade IS NULL;

-- All students born before 1986 who have a 't' in their first or last name
DROP VIEW IF EXISTS tees;
CREATE VIEW tees AS
    SELECT * FROM students
    WHERE
        students.first_name ILIKE '%t%' OR
        students.last_name ILIKE '%t%';
SELECT * FROM tees
WHERE birthdate < '1985-01-01';

-- The average age of all the students
SELECT 
    AVG((CURRENT_DATE - students.birthdate) / 365) AS avg_age 
FROM students;

-- Addresses that have a space in their city name.
SELECT * FROM addresses 
WHERE addresses.city ILIKE '% %';

-- Students & their addresses that live in a city with more than one word in the city name
SELECT 
    students.last_name, 
    students.first_name,
    addresses.city
FROM students
JOIN addresses ON addresses.id = students.address_id
WHERE addresses.city ILIKE '% %';

-- The average number of credits for classes offered at the school.
SELECT
    AVG(classes.credits) AS avg_credits
FROM classes;

-- The first and last name of all students who have received an 'A'.
SELECT
    students.last_name, 
    students.first_name,
    enrollments.grade
FROM students
JOIN enrollments ON students.id = enrollments.student_id
WHERE enrollments.grade = 'A';

-- Each student's first name and the total credits they've enrolled in
SELECT 
    students.first_name, 
    SUM(classes.credits) AS credits
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN classes ON classes.id = enrollments.class_id
GROUP BY students.first_name;

-- The total number of credits each student has received a grade for.
SELECT 
    first_name,
    credits
FROM (SELECT 
        student_id,
        first_name,
        SUM(credits) AS credits
    FROM (SELECT *
        FROM students
        JOIN enrollments ON students.id = enrollments.student_id
        JOIN classes ON classes.id = enrollments.class_id
        WHERE enrollments.grade IS NOT NULL) AS grades
    GROUP BY student_id, first_name) AS total_credits;

-- All enrollments, including the class name
SELECT classes.name, enrollments.* FROM enrollments
JOIN classes ON classes.id = enrollments.class_id;

-- Students born between 1982-1985 (inclusive)
SELECT * FROM students
WHERE birthdate
    BETWEEN '1982-01-01' AND '1985-12-31';

-- Insert a new enrollment recording that Andre Rohan took PHYS 218 and got an A.
INSERT INTO enrollments (student_id, class_id, grade) VALUES (5, 4, 'A');