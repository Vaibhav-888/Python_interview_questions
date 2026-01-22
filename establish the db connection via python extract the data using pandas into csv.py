# Establish the db connection via python.
# Step1: install required libraries
"""
p install sqlalchemy pandas pymysql  # for MySQL
# OR
pip install psycopg2                  # for PostgreSQL
# OR
pip install pyodbc                    # for SQL Server
"""

# step2: for mysql connection for example in this case
import pandas as pd
from sqlalchemy import create_engine

# --- Database connection details ---
username = "root"
password = "your_password"
host = "localhost"
port = "3306"
database = "your_database"

# --- Create SQLAlchemy engine ---
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# --- SQL Query ---
query = "SELECT * FROM your_table_name;"

# --- Read data into pandas DataFrame ---
df = pd.read_sql(query, engine)

# --- Export to CSV ---
output_path = "output_data.csv"
df.to_csv(output_path, index=False)

print(f"Data exported successfully to {output_path}")

# other db strings: sqlserver, postgresql, SQLite
# postgresql: 
engine = create_engine("postgresql://username:password@localhost:5432/dbname")
# sql server

engine = create_engine(
    "mssql+pyodbc://username:password@SERVERNAME/DBNAME?driver=ODBC+Driver+17+for+SQL+Server"
)
# SQLite
engine = create_engine("sqlite:///mydb.sqlite")
