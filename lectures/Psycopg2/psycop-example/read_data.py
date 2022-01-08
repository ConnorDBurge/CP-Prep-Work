import psycopg2
import pandas as pd


def execute_query(connection, query, columns):
    cursor = connection.cursor()
    results = None
    cursor.execute(query)
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=columns)


connection = psycopg2.connect(
    f"dbname=sacramento_real_estate")

print('\nAre single family homes or condos more expensive on average?')
q1 = """
SELECT AVG(sale_price) FROM properties
WHERE property_type = 'Residential'"""
c1 = ['avg']
family_home_df = execute_query(connection, q1, c1)
family_home_avg = float(family_home_df['avg'])
print(f'Family Home Avg: \t${family_home_avg:,.2f}')

q2 = """
SELECT AVG(sale_price) FROM properties
WHERE property_type = 'Condo'"""
c2 = ['avg']
condo_df = execute_query(connection, q2, c2)
condo_avg = float(condo_df['avg'])
print(f'Condo Avg: \t\t${condo_avg:,.2f}')


print("\nWhat's the most expensive house and condo sold? What's the cost per square foot?")
q3 = """
SELECT  
    properties.sale_price AS sale_price,
    properties.sale_price / properties.square_feet AS per_sqft
FROM properties
WHERE property_type = 'Residential'
ORDER BY properties.sale_price DESC
LIMIT 1;"""
c3 = ['sale_price', 'per_sqft']
res_df = execute_query(connection, q3, c3)
print(
    f'Residential:\t${int(res_df["sale_price"]):,}\t${int(res_df["per_sqft"]):,}')

q4 = """
SELECT  
    properties.sale_price AS sale_price,
    properties.sale_price / properties.square_feet AS per_sqft
FROM properties
WHERE property_type = 'Condo'
ORDER BY properties.sale_price DESC
LIMIT 1;"""
c4 = ['sale_price', 'per_sqft']
con_df = execute_query(connection, q4, c4)
print(
    f'Condo:\t\t${int(con_df["sale_price"]):,}\t${int(con_df["per_sqft"]):,}')
