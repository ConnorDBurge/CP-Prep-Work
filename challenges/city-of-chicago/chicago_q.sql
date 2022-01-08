-- Find the employee being paid the most
-- SELECT last_name, first_name, annual_salary FROM salaries
-- ORDER BY annual_salary DESC
-- LIMIT 1;

-- Find the department with the highest average salary
-- SELECT department, AVG(annual_salary) AS avg_salary FROM salaries
-- GROUP BY department
-- ORDER BY avg_salary DESC
-- LIMIT 1;

-- Find the average salary difference between full time and part time workers
-- SELECT AVG(annual_salary) AS avg_salary FROM salaries
-- WHERE full_or_part_time = 'F';
-- SELECT AVG(annual_salary) AS avg_salary FROM salaries
-- WHERE full_or_part_time = 'P';