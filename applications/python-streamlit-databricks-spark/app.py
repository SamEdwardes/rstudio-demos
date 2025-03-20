import os

import streamlit as st
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config
from loguru import logger
from posit import connect

# -----------------------------------------------------------------------------
# Global variables
# -----------------------------------------------------------------------------

DATABRICKS_CLUSTER_ID = "0606-201802-s75pygqn"

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------


def get_viewer_token() -> str:
    client = connect.Client()
    user_session_token = st.context.headers.get("Posit-Connect-User-Session-Token")
    access_token = client.oauth.get_credentials(user_session_token).get("access_token")
    return access_token


def get_service_account_token() -> str:
    client = connect.Client()
    access_token = client.oauth.get_content_credentials().get("access_token")
    return access_token


class TokenNotFoundError(Exception):
    """Exception raised when a required token is not found."""

    pass


def get_viewer_or_service_account_token() -> str:
    exceptions = []

    # First attempt to get the Viewer token
    try:
        logger.info("Attempting to obtain Viewer OAuth access_token.")
        access_token = get_viewer_token()
        logger.info("Viewer OAuth access_token successfully obtained.")
        return access_token
    except Exception as e:
        exceptions.append(e)
        logger.warning(f"Could not get Viewer integration access_token: {e}")

    # If you could not get the Viewer token, then try the Service Account token
    try:
        logger.info("Attempting to object Service Account OAuth access_token.")
        access_token = get_service_account_token()
        return access_token
    except Exception as e:
        exceptions.append(e)
        logger.warning(f"Could not get Service Account integration access_token: {e}")

    # In the event you cannot obtain the Viewer or Service Account token, raise an error.
    raise TokenNotFoundError(
        f"Could not obtain OAuth token for Viewer or Service Account: {exceptions}"
    )


# -----------------------------------------------------------------------------
# Set-up Databricks connection
# -----------------------------------------------------------------------------

# If running on Connect. See
# https://docs.posit.co/connect/cookbook/content/integrations/databricks/viewer/python/
# for examples using different frameworks.
if os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    logger.info("Running in Posit Connect")
    access_token = get_viewer_or_service_account_token()
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
logger.info(f"{spark=}")

# -----------------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------------

st.write("Databricks on Connect with pyspark example")

logger.info("Querying Databricks lending_club table start")
df = spark.read.table("sol_eng_demo_nickp.default.lending_club")
st.dataframe(df.limit(5).toPandas())
logger.info("Querying Databricks lending_club table complete")
