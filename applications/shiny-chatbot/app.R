library(shiny)
library(shinychat)
library(paws.common)

ui <- bslib::page_fillable(
	chat_ui(
		id = "chat",
		messages = "**Hello!** How can I help you today?"
	),
	fillable_mobile = TRUE
)

server <- function(input, output, session) {
	chat <- ellmer::chat_aws_bedrock(
		"Be terse",
		model = "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
	)

	observeEvent(input$chat_user_input, {
		stream <- chat$stream_async(input$chat_user_input)
		chat_append("chat", stream)
	})
}

shinyApp(ui, server)
