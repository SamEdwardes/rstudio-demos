import polars as pl
import snowflake.connector

# Create the connection object.
con = snowflake.connector.connect(
    connection_name="workbench",
    database="LENDING_CLUB",
    schema="PUBLIC",
)

# List all of the tables in the database.
list_tables_query = """
SELECT *
FROM "LENDING_CLUB"."INFORMATION_SCHEMA"."TABLES";
"""

pl.read_database(list_tables_query, connection=con)

# Execute a query.
query = """
SELECT "ID", "LOAN_AMNT", "TERM", "INT_RATE", "GRADE"
FROM LOAN_DATA
WHERE "LOAN_AMNT" IS NOT NULL
ORDER BY "LOAN_AMNT" DESC
LIMIT 10;
"""

pl.read_database(query, connection=con)
