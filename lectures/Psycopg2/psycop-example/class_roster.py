import psycopg2
import os

# Connect to the database
connection = psycopg2.connect(f'dbname=class_roster')

# Once a connection has been opened, we are going to open a cursor to run our SQL queries
cursor = connection.cursor()

# Let's create a query to create a students table and execute it
cursor.execute('DROP TABLE IF EXISTS students')
student_table_creation_query = """
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        favorite_food VARCHAR(255)
    );"""
cursor.execute(student_table_creation_query)
cursor.execute(
    f"INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Jon', "Sushi"))
cursor.execute(
    "INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Tom', "Mostaccioli"))
cursor.execute(
    "INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Mike', "Thai Curry"))
# Commit these changes to the database
connection.commit()
# Close communication with the database
cursor.close()
connection.close()
