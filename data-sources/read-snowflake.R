library(dplyr)

# Create the connection object.
con <- DBI::dbConnect(
    odbc::snowflake(),
    connection_name = "workbench",
    database = "LENDING_CLUB",
    schema = "PUBLIC"
)

# List all of the tables in the database.
DBI::dbGetQuery(con, "SHOW TABLES;") |>
    as_tibble()

# Execute a query.
tbl(con, "LOAN_DATA") |>
    select(ID, LOAN_AMNT, TERM, INT_RATE, GRADE) |>
    filter(!is.na(LOAN_AMNT)) |>
    arrange(desc(LOAN_AMNT)) |>
    head(10) |>
    collect()
