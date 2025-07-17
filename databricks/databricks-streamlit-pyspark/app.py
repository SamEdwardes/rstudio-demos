import os

import streamlit as st
from loguru import logger
from posit import connect

from databricks.connect import DatabricksSession
from databricks.sdk.core import Config

# -----------------------------------------------------------------------------
# Set-up Databricks connection
# -----------------------------------------------------------------------------
DATABRICKS_CLUSTER_ID = os.environ.get("DATABRICKS_CLUSTER_ID", "0606-201802-s75pygqn")

if os.environ.get("WORKBENCH_WEB_BASE_URL"):
    logger.info("Running in Posit Workbench")
    cfg = Config(profile="workbench", cluster_id=DATABRICKS_CLUSTER_ID)

elif os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    logger.info("Running in Posit Connect")
    # Get OAuth token using posit-sdk
    client = connect.Client()
    user_session_token = st.context.headers.get("Posit-Connect-User-Session-Token")
    access_token = client.oauth.get_credentials(user_session_token).get("access_token")
    # Create the Databricks config object
    cfg = Config(
        token=access_token,
        host=os.environ.get(
            "DATABRICKS_HOST", "https://adb-3256282566390055.15.azuredatabricks.net"
        ),
        cluster_id=DATABRICKS_CLUSTER_ID,
    )

else:
    raise ValueError("Not running on Posit Connect or Posit Workbench")

# Create your spark connection object.
spark = DatabricksSession.builder.sdkConfig(cfg).getOrCreate()

# -----------------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------------

st.write("Databricks on Connect with pyspark example")

df = spark.read.table("sol_eng_demo_nickp.default.lending_club")
st.dataframe(df.limit(5).toPandas())
