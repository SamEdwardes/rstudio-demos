library(shiny)
library(DESeq2)

ui <- fluidPage(
  titlePanel("Hello world!"),
  sidebarLayout(
    sidebarPanel(
      actionButton("button_counter", "Button Counter")
    ),
    mainPanel(
      p("Number of button presses:"),
      verbatimTextOutput("num_button_presses")
    )
  )
)


server <- function(input, output, session) {
  
  v <- reactiveValues(
    num_button_presses = 0
  )
  
  observeEvent(input$button_counter, {
    v$num_button_presses <- v$num_button_presses + 1
  })
  
  output$num_button_presses <- renderText(v$num_button_presses)
  
}

shinyApp(ui = ui, server = server)
