from dotenv import load_dotenv

load_dotenv()

import json
import os

import flask
import polars as pl
import snowflake.connector
from dash import Dash, Input, Output, callback, dash_table, dcc, html
from loguru import logger
from posit.connect.external.snowflake import PositAuthenticator
from werkzeug.exceptions import BadRequest

# Define variables that will be needed for accessing snowflake
# from Workbench or Connect.
DATABASE = "LENDING_CLUB"
SCHEMA = "PUBLIC"


def get_session_token(req: flask.Request) -> str:
    """
    Returns a dict containing "user" and "groups" information populated by
    the incoming request header "RStudio-Connect-Credentials".
    """
    credential_header = req.headers.get("RStudio-Connect-Credentials")
    session_header = req.headers.get("Posit-Connect-User-Session-Token")
    if not credential_header:
        raise BadRequest("Missing required header: Posit-Connect-User-Session-Token")
    logger.info(f"{session_header=}")
    return session_header


def make_connection_to_snowflake():
    """
    When running in Posit Connect, use the OAuth Viewer integration. Otherwise
    assume running in Workbench and use Workbench Managed Credentials
    """
    if os.getenv("POSIT_PRODUCT") == "CONNECT":
        logger.info("Running in Posit Connect")

        session_token = get_session_token(flask.request)

        auth = PositAuthenticator(
            local_authenticator="EXTERNALBROWSER",
            user_session_token=session_token
        )

        con = snowflake.connector.connect(
            account="duloftf-posit-software-pbc-dev",
            warehouse="DEFAULT_WH",
            database=DATABASE,
            schema=SCHEMA,
            authenticator=auth.authenticator,
            token=auth.token,
        )

    else:
        logger.info("Assumed to be running in Posit Workbench.")

        con = snowflake.connector.connect(
            connection_name="workbench",
            database=DATABASE,
            schema=SCHEMA,
        )

    return con


def query_data(grade_filter=None) -> pl.DataFrame:
    base_query = """
    SELECT "ID", "LOAN_AMNT", "TERM", "INT_RATE", "GRADE"
    FROM LOAN_DATA
    WHERE "LOAN_AMNT" IS NOT NULL
    """

    if grade_filter and grade_filter != "All":
        base_query += f" AND \"GRADE\" = '{grade_filter}'"

    query = (
        base_query
        + """
    ORDER BY "LOAN_AMNT" DESC
    LIMIT 20;
    """
    )
    con = make_connection_to_snowflake()
    df = pl.read_database(query, con)
    return df


app = Dash()


app.layout = [
    html.H1("Loan Data"),
    html.Div(
        [
            html.Label("Filter by Grade:"),
            dcc.Dropdown(
                id="grade-filter",
                value="All",
                style={"width": "200px", "margin-bottom": "20px"},
            ),
        ]
    ),
    html.Div(
        id="data-table-container",
        children=[dash_table.DataTable(id="data-table", page_size=10)],
    ),
    # Dummy input to trigger the grades dropdown update on app load
    html.Div(id="dummy-input", style={"display": "none"}),
]


@callback(Output("grade-filter", "options"), Input("dummy-input", "children"))
def update_grades_dropdown(_) -> list[dict[str, str]]:
    query = """
    SELECT DISTINCT "GRADE"
    FROM LOAN_DATA
    WHERE "GRADE" IS NOT NULL
    ORDER BY "GRADE";
    """
    con = make_connection_to_snowflake()
    df = pl.read_database(query, con)
    unique_grades = ["All"] + df["GRADE"].to_list()
    logger.info(f"{unique_grades=}")
    return unique_grades


@callback(Output("data-table", "data"), Input("grade-filter", "value"))
def update_table(selected_grade):
    filtered_df = query_data(selected_grade)
    return filtered_df.to_dicts()


if __name__ == "__main__":
    if os.getenv("DASH_DEBUG"):
        logger.info("Running in dash debug mode.")
        port = os.environ["PORT"]
        logger.info(f"{port=}")
        logger.info(f"{os.getenv('DASH_REQUESTS_PATHNAME_PREFIX')=}")
        app.run(debug=True, port=port)
    else:
        app.run(debug=False)
