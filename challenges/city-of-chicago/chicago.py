import psycopg2
import pandas as pd
import os


def execute_query(connection, query, columns):
    cursor = connection.cursor()
    results = None
    cursor.execute(query)
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=columns)


connection = psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")

print('\nFind the employee being paid the most')
print(execute_query(connection, """
SELECT last_name, first_name, annual_salary FROM salaries
ORDER BY annual_salary DESC
LIMIT 1;""", ['last_name', 'first_name', 'annual_salary']))

print('\nFind the employee being paid the least')
print(execute_query(connection, """
SELECT last_name, first_name, annual_salary FROM salaries
ORDER BY annual_salary ASC
LIMIT 1;""", ['last_name', 'first_name', 'annual_salary']))

print('\nFind the department with the highest average salary')
print(execute_query(connection, """
SELECT department, AVG(annual_salary) AS avg_salary FROM salaries
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;""", ['department', 'avg_salary']))

print('\nFind the department with the lowest average salary')
print(execute_query(connection, """
SELECT department, AVG(annual_salary) AS avg_salary FROM salaries
GROUP BY department
ORDER BY avg_salary ASC
LIMIT 1;""", ['department', 'avg_salary']))

print('\nFind the average salary difference between full time and part time workers')
f_avg = round(execute_query(connection, """
SELECT AVG(annual_salary) AS avg_salary FROM salaries
WHERE full_or_part_time = 'F';""", ['avg_salary']), 2)
p_avg = round(execute_query(connection, """
SELECT AVG(annual_salary) AS avg_salary FROM salaries
WHERE full_or_part_time = 'P';""", ['avg_salary']), 2)
difference = float((f_avg - p_avg)['avg_salary'])
print(f'Difference: ${difference:,.2f}')

print('\nFind the most common first name')
print(execute_query(connection, """
SELECT first_name, COUNT(first_name) AS cnt
FROM salaries
GROUP BY first_name
ORDER BY cnt DESC
LIMIT 1;""", ['first_name', 'cnt']))

print('\nFind the most common first name')
print(execute_query(connection, """
SELECT last_name, COUNT(first_name) AS cnt
FROM salaries
GROUP BY last_name
ORDER BY cnt DESC
LIMIT 1;""", ['last_name', 'cnt']))

connection.commit()
connection.close()
