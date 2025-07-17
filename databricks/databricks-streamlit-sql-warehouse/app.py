import os

import polars as pl
import posit
import streamlit as st
from loguru import logger

from databricks import sql
from databricks.sdk.core import Config

# -----------------------------------------------------------------------------
# Set-up Databricks connection
# -----------------------------------------------------------------------------
if os.environ.get("WORKBENCH_WEB_BASE_URL"):
    logger.info("Running in Posit Workbench")
    cfg = Config(profile="workbench")

elif os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    logger.info("Running in Posit Connect")
    # Get OAuth token using posit-sdk
    client = posit.connect.Client()
    user_session_token = st.context.headers.get("Posit-Connect-User-Session-Token")
    access_token = client.oauth.get_credentials(user_session_token).get("access_token")
    # Create the Databricks config object
    cfg = Config(
        token=access_token,
        host=os.environ.get(
            "DATABRICKS_HOST", "https://adb-3256282566390055.15.azuredatabricks.net"
        ),
    )

else:
    raise ValueError("Not running on Posit Connect or Posit Workbench")

# Create your SQL connection object.
con = sql.connect(
    server_hostname=cfg.host,
    http_path=os.environ.get("SQL_HTTP_PATH", "/sql/1.0/warehouses/e985c33f1db7502f"),
    access_token=cfg.token,
)

# -----------------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------------
st.write("Databricks on Connect with SQL Warehouse")

sql_query = """
SELECT *
FROM `sol_eng_demo_nickp`.`default`.`lending_club`
LIMIT 100;
"""

df = pl.read_database(sql_query, con).with_columns(
    pl.col("loan_amnt", "funded_amnt", "funded_amnt_inv", "revol_bal").cast(pl.Int64),
    pl.col(
        "installment", "annual_inc", "out_prncp", "out_prncp_inv", "total_pymnt"
    ).cast(pl.Float64),
    pl.col("int_rate", "revol_util").str.replace("%", "").cast(pl.Float64) / 100,
)

st.dataframe(df)
