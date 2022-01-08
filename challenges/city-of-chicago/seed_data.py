import csv
import psycopg2
import re
import os


def table_creation_query():  # Creating a table
    return """
    CREATE TABLE salaries (
        id serial PRIMARY KEY, 
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        job_title VARCHAR(255),
        full_or_part_time VARCHAR(255),
        department VARCHAR(255),
        annual_salary DECIMAL
    );"""


def insert_record():
    return """
    INSERT INTO salaries
    (first_name, last_name, job_title, full_or_part_time, department, annual_salary)
    VALUES 
    (%s, %s, %s, %s, %s, %s);"""


def split_name(name):
    split = re.split("\s|(?<!\d)[,.](?!\d)", name)
    if split[1] == '':
        return [split[0], split[3]]
    else:
        return [split[0], split[4]]  # last, first


def clean_data(csv_row):  # Cleaning the CSV file
    cleaned = {}
    cleaned['first_name'] = split_name(csv_row['Name'])[0]
    cleaned['last_name'] = split_name(csv_row['Name'])[1]
    cleaned['job_title'] = csv_row['Job Titles']
    cleaned['full_or_part_time'] = csv_row['Full or Part-Time']
    cleaned['department'] = csv_row['Department']
    if csv_row['Salary or Hourly'] == 'Salary':
        cleaned['annual_salary'] = round(float(csv_row['Annual Salary']), 2)
    else:
        annual_salary = round(float(
            csv_row['Typical Hours']) * float(csv_row['Hourly Rate']), 2)
        cleaned['annual_salary'] = annual_salary
    return cleaned


connection = psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS salaries;')
cursor.execute(table_creation_query())

with open('./salaries.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cleaned_data = clean_data(row)
        cursor.execute(insert_record(),
                       (cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['job_title'], cleaned_data['full_or_part_time'], cleaned_data['department'], cleaned_data['annual_salary']))

connection.commit()
connection.close()
