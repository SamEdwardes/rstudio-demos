library(ellmer)

chat <- chat_databricks(
  model = "databricks-claude-3-7-sonnet",
  system_prompt = "You are a friendly but terse assistant.",
)

live_console(chat)
