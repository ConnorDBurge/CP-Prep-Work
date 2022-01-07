INSERT INTO addresses (line_1, city, state, zipcode) VALUES ('931 Dogwood Lane South', 'Oceanside', 'CA', '92058');
INSERT INTO addresses (line_1, city, state, zipcode) VALUES ('917 Huntington Place', 'Peachtree City', 'GA', '30269');
INSERT INTO addresses (line_1, city, state, zipcode) VALUES ('555 South Fake Street', 'Chicago', 'IL', '60198');

INSERT INTO guardians (id, name, phone, email, address) VALUES (1, 'Sara Connor', '678-727-8332', 'sara@email.com', 1);
INSERT INTO guardians (id, name, phone, email, address) VALUES (2, 'Connor Burge', '678-789-3898', 'connor@email.com', 3);
INSERT INTO guardians (id, name, phone, email, address) VALUES (3, 'Elrod Kyndall', '345-231-8798', 'kyndall@email.com', 2);

INSERT INTO students (name, grade, dob, guardian_id) VALUES ('John Smith', '7', '2005-01-28', 3);
INSERT INTO students (name, grade, dob, guardian_id) VALUES ('Joan Bill', '5', '20010-03-04', 3);

-- SELECT * FROM guardians
-- JOIN addresses ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- SELECT * FROM addresses
-- JOIN guardians ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- SELECT addresses FROM addresses
-- JOIN guardians ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- SELECT 
--     guardians.name, 
--     addresses.line_1,
--     addresses.line_2,
--     addresses.city,
--     addresses.state,
--     addresses.zipcode
-- FROM guardians
-- JOIN addresses ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- SELECT 
--     guardians.name, 
--     addresses.*
-- FROM guardians
-- JOIN addresses ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- SELECT addresses.* FROM addresses
-- JOIN guardians ON addresses.id = guardians.address
-- WHERE  guardians.name = 'Connor Burge';

-- UPDATE students
-- SET name = 'John Smitherin'
-- WHERE id = 1;

-- SELECT students.name
-- FROM students
-- JOIN guardians ON guardians.id = students.guardian_id
-- WHERE guardian_id = 3;

SELECT students.name, addresses.* FROM addresses
JOIN guardians ON addresses.id = guardians.address
JOIN students ON guardians.id = students.guardian_id
WHERE students.name = 'John Smitherin';
