import psycopg2
import pandas as pd
import os


def execute_query(connection, query, columns):
    cursor = connection.cursor()
    results = None
    cursor.execute(query)
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=columns)


psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")
