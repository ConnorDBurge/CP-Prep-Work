import csv
import psycopg2
import os

import ipdb
from decimal import Decimal
from datetime import datetime


def table_creation_query():  # Creating a table
    return """
    CREATE TABLE properties (
        id serial PRIMARY KEY, 
        street_address varchar, 
        city varchar, 
        zip_code varchar, 
        state varchar, 
        number_of_beds integer, 
        number_of_baths integer, 
        square_feet integer, 
        property_type varchar, 
        sale_date timestamp, 
        sale_price integer, 
        latitude decimal, 
        longitude decimal
    );"""


connection = psycopg2.connect(
    f"dbname=sacramento_real_estate")
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS properties')
cursor.execute(table_creation_query())


def clean_data(csv_row):  # Cleaning the CSV file
    cleaned = {}
    cleaned['street_address'] = csv_row['street']
    cleaned['city'] = csv_row['city']
    cleaned['zip_code'] = csv_row['zip']
    cleaned['state'] = csv_row['state']
    cleaned['number_of_beds'] = int(csv_row['beds'])
    cleaned['number_of_baths'] = int(csv_row['baths'])
    cleaned['square_feet'] = int(csv_row['sq__ft'])
    cleaned['property_type'] = csv_row['type']
    cleaned['sale_date'] = datetime.strptime(csv_row['sale_date'], '%m/%d/%y')
    cleaned['sale_price'] = csv_row['price']
    cleaned['latitude'] = Decimal(csv_row['latitude'])
    cleaned['longitude'] = Decimal(csv_row['longitude'])
    return cleaned


with open('./transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cleaned_data = clean_data(row)
        cursor.execute("INSERT INTO properties (street_address, city, zip_code, state, number_of_beds, number_of_baths, square_feet, property_type, sale_date, sale_price, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cleaned_data['street_address'], cleaned_data[
            'city'], cleaned_data['zip_code'], cleaned_data['state'], cleaned_data['number_of_beds'], cleaned_data['number_of_baths'], cleaned_data['square_feet'], cleaned_data['property_type'], cleaned_data['sale_date'], cleaned_data['sale_price'], cleaned_data['latitude'], cleaned_data['longitude']))

connection.commit()
connection.close()
