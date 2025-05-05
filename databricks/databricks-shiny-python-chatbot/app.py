from loguru import logger
from shiny import App, ui

logger.info("Starting app")

app_ui = ui.page_fixed(ui.chat_ui(id="my_chat"))


def server(input):
    # # -----------------------------------------------------------------------------
    # # Set-up Databricks connection
    # # -----------------------------------------------------------------------------
    # if os.environ.get("WORKBENCH_WEB_BASE_URL"):
    #     logger.info("Running in Posit Workbench")
    #     cfg = Config(profile="workbench")

    # elif os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    #     logger.info("Running in Posit Connect")
    #     # Get OAuth token using posit-sdk
    #     client = posit.connect.Client()
    #     user_session_token = st.context.headers.get("Posit-Connect-User-Session-Token")
    #     access_token = client.oauth.get_credentials(user_session_token).get("access_token")
    #     # Create the Databricks config object
    #     cfg = Config(
    #         token=access_token,
    #         host=os.environ.get(
    #             "DATABRICKS_HOST", "https://adb-3256282566390055.15.azuredatabricks.net"
    #         ),
    #     )

    # else:
    #     raise ValueError("Not running on Posit Connect or Posit Workbench")

    # -----------------------------------------------------------------------------
    # Shiny app
    # -----------------------------------------------------------------------------
    chat = ui.Chat(id="my_chat")
    # chat_client = ChatDatabricks(
    #     model="databricks-claude-3-7-sonnet"
    # )

    # Define a callback to run when the user submits a message
    @chat.on_user_submit
    async def handle_user_input(user_input: str):
        # Simply echo the user's input back to them
        await chat.append_message(f"You said: {user_input}")

    # @chat.on_user_submit
    # async def handle_user_input(user_input: str):
    #     response = await chat_client.stream_async(user_input)
    #     await chat.append_message_stream(response)


app = App(app_ui, server)
