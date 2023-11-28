library(shiny)

ui <- fluidPage(
  titlePanel("Working with file in Shiny for R"),
  mainPanel(
    tags$b("Current working directory:"),
    verbatimTextOutput("current_working_directory"),
    textInput(
      "directory_to_print",
      label = "Directory to print:",
      value = "."
    ),
    p("Files in directory:"),
    verbatimTextOutput("directory_contents")
  )
)


server <- function(input, output, session) {
  
  output$current_working_directory <- renderPrint({
    getwd()
  })
  
  output$directory_contents <- renderPrint({
    dir(input$directory_to_print)
  })
  
}

shinyApp(ui = ui, server = server)
