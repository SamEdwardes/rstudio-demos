import os

import streamlit as st
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config
from loguru import logger
from posit import connect

DATABRICKS_CLUSTER_ID = "0606-201802-s75pygqn"

# -----------------------------------------------------------------------------
# Set-up Databricks connection
# -----------------------------------------------------------------------------

# If running on Connect. See
# https://docs.posit.co/connect/cookbook/content/integrations/databricks/viewer/python/
# for examples using different frameworks.

if os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    logger.info("Running in Posit Connect")
    client = connect.Client()
    user_session_token = st.context.headers.get("Posit-Connect-User-Session-Token")
    access_token = client.oauth.get_credentials(user_session_token).get("access_token")
    config = Config(
        token=access_token,
        host="https://adb-3256282566390055.15.azuredatabricks.net",
        cluster_id=DATABRICKS_CLUSTER_ID,
    )

# If running outside of Connect. This example assumes you are runninging in
# Posit Workbench with Databricks managed credentials configured.

else:
    logger.info("NOT running in Posit Connect")
    config = Config(
        profile="workbench",
        cluster_id=DATABRICKS_CLUSTER_ID,
    )

# Create your spark connection object.
spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

# -----------------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------------

st.write("Databricks on Connect with pyspark example")

df = spark.read.table("sol_eng_demo_nickp.default.lending_club")
st.dataframe(df.limit(5).toPandas())
