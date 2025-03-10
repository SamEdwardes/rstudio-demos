from databricks.connect import DatabricksSession
from databricks.sdk.core import Config
from loguru import logger

DATABRICKS_CLUSTER_ID = "0606-201802-s75pygqn"

logger.info("building config")

config = Config(
    profile="workbench",
    cluster_id=DATABRICKS_CLUSTER_ID,
)

spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

df = spark.read.table("sol_eng_demo_nickp.default.lending_club")
logger.info(df.limit(10).toPandas())
