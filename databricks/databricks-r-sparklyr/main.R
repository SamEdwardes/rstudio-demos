library(dplyr)
library(sparklyr)
library(dbplyr)

Sys.setenv(DATABRICKS_PATH = "/sql/protocolv1/o/4425955464597947/1126-223213-xusw1elx")

sc <- spark_connect(
  cluster_id = "1126-223213-xusw1elx",
  version = "17.3",
  method = "databricks_connect"
)

summary <- tbl(sc, in_catalog("sol_eng_demo_nickp", "default", "lending_club")) |>
  filter(!is.na(addr_state)) |>
  mutate(
    region = case_when(
      stringr::str_sub(zip_code, 1, 1) %in% c("8", "9") ~ "West",
      stringr::str_sub(zip_code, 1, 1) %in% c("6", "5", "4") ~ "Midwest",
      stringr::str_sub(zip_code, 1, 1) %in% c("7", "3", "2") ~ "South",
      stringr::str_sub(zip_code, 1, 1) %in% c("1", "0") ~ "East",
      TRUE ~ "NA"
    )
  ) |>
  select(
    member_id,
    region,
    grade,
    sub_grade,
    loan_amnt,
    funded_amnt,
    term,
    int_rate,
    emp_title,
    emp_length,
    annual_inc,
    loan_status,
    purpose,
    title,
    zip_code,
    addr_state,
    dti,
    out_prncp
  ) |>
  mutate(office_no = stringr::str_sub(zip_code, 1, 3)) |> 
  group_by(region, grade) |>
  summarise(out_prncp = sum(as.numeric(out_prncp), na.rm = TRUE)) |>
  collect()

summary

