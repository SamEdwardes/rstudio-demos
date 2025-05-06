library(dplyr)

con <- connections::connection_open(
  RSQLite::SQLite(),
  "sample.db"
)

employees <- tbl(con, "employees")
departments <- tbl(con, "departments")


function() "SELECT {} FROM {}"

departments |>
  select(name) |>
  mutate(upper_name = toupper(name)) |>
  collect()
