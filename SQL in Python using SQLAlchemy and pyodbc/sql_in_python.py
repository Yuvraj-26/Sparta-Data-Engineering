import pyodbc
import pandas as pd
import sqlalchemy

# SQLAlchemy is a Python library for working with databases. It provides tools to interact with databases using
# Python code instead of raw SQL. SQLAlchemy offers an Object-Relational Mapping (ORM) system for defining database
# structures with Python classes, and it includes a SQL Expression Language for querying. It's versatile, supporting
# various database systems and simplifying tasks like data retrieval, insertion, and updates.

# An ORM (Object-Relational Mapping) is a programming technique that maps database tables to classes in
# object-oriented programming languages like Python. It allows you to interact with databases using code and objects
# rather than writing raw SQL queries, making database operations more intuitive and abstracting the underlying
# database structure.

# pandas methods require 2 arguments - sql and the connection
# pandas.read_sql(): This method is used to read data from a SQL database and load it into a pandas DataFrame. It
# requires a valid database connection and a SQL query to retrieve data from one or more database tables. The data is
# then returned as a DataFrame, making it easy to work with in Python.

# DataFrame.to_sql(): This method in pandas is used to write the contents of a DataFrame to a SQL database as a new
# table

# pyodbc is a Python module that allows you to connect to and interact with relational databases using the ODBC (Open
# Database Connectivity) standard. ODBC is a standardized API for connecting to various database management systems (
# DBMS) and data sources ODBC driver for the database system act as an interface between the pycharm and the database

# https://insightsoftware.com/blog/what-is-odbc/ SQLAlchemy is the Python Benefits: - ease of conversion as can
# convert data from database into pandas for analysis and convert results back to SQL for storage or further querying
# - use complex SQL queries such as joining and aggregation as the ORM provides a way to interact with databases by
# mapping ables to Python classes
# - cross-platform and work on multiple operating systems
# - pandas and SQAlchemy allow optimised data retrieval
# and db operations such as indexing, caching, and query optimisation
# - sqlalchemy abstracts the differences between various database systems so can write agnostic code
# allowing us to work with different database backends such as MYSQL, SQL Server, PostgresSQL, with minimal changes
# - Dataframes can be exported in CSV, JSON, or loaded into jupyter notebook easily


# print pyodbc version and drivers
print(pyodbc.version)
print(pyodbc.drivers())

#  azure sql edge container running on docker
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'yourStrong(!)Password'
driver = 'ODBC Driver 17 for SQL Server'

# connection strings - to establish connection need the variables above
# connecting through pyodbc uses connect method
pyodbc_conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# connecting through sqlalchemy uses create engine
# sql alchemy is additional to pyodbc
sqlalchemy_conn = sqlalchemy.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
# The cursor object is used to execute SQL queries and fetch results from the database
cursor = pyodbc_conn.cursor()

# for execute commands within the cursor object use fetchone or fetchall or fetchmany
# print the SQL server version information
print(cursor.execute("SELECT @@version;"))
# fetchone() fetches the next row from the results set and returns it as a tuple
row = cursor.fetchone()
print(row)

# fetchall() method retrieves all rows from the results set and returns them as a list of types
cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)

# query selects all rows and columns from the customers table within a cursor object that holds the query result
# then convert cursor object into pandas dataframe corresponding to the data returned by the query
# the output is incorrect and doesn't insert all data into one row
cust_rows_obj = cursor.execute("SELECT * FROM Customers;")
customers_df = pd.DataFrame(cust_rows_obj)
# print(customers_df)

# using pyodbc connection
sql_query = 'SELECT * FROM Customers'
# read.sql accepts query and pyodbc connection
df = pd.read_sql(sql_query, pyodbc_conn)
# outputs warning saying pandas only supports sqlalchemy engine or connection
# print(df)

# when working with pandas, use sqlalchemy connection
sql_query = 'SELECT * FROM Customers'
df = pd.read_sql(sql_query, sqlalchemy_conn)
# executes sql query to retrieve all from customer table in the connected database,
# loads the result into pandas dataframe
# print(df)

# creating the DataFrame
# fetch data from customers table in the connected db and select customers whose city is Paris
# pd.read_sql has two arguments sql query and sqlalchemy connection
# loads the result data in a pandas dataframe
paris_cus_df = pd.read_sql("SELECT * FROM Customers WHERE city = 'Paris'", con=sqlalchemy_conn)
# print(paris_cus_df)

# using to_sql to create a table from the DataFrame
# use the df.to_sql with name of the new table, sqlalchemy connection, and if exists action
# take the data from the paris_cus_df dataframe and write it into the SQL database table called paris_customers
paris_cus_df.to_sql(name="paris_customers", con=sqlalchemy_conn, if_exists="replace")

# checking everything worked by querying the new table
# checks whether paris_customer stable was successfully created and if it contains the expected data
query = pd.read_sql_query("SELECT * FROM paris_customers;", con=sqlalchemy_conn)
# print(query)

# read_sql_query is suitable for executing a single SQL query and storing its result in a DataFrame,
# while read_sql # is more flexible, allowing you to execute multiple queries and returning a list of DataFrames
# as the result.

# Task: try to query a new table, transform the dataframe using pandas methods,
# and load it back in as a new table in sql

