library(shiny)
library(reticulate)

ui <- fluidPage(
  titlePanel("Using Reticluate in Shiny"),
  mainPanel(
    p("Which Python am I using?"),
    verbatimTextOutput("python_info"),
    p("Below is an array from numpy"),
    verbatimTextOutput("data")
  )
)


server <- function(input, output, session) {
  # Check which python I am using.
  output$python_info <- renderPrint({
    reticulate::py_config()
  })

  # Create a numpy array
  np <- import("numpy")
  output$data <- renderPrint({
    np$array(c(1, 2, 3))
  })
}

shinyApp(ui = ui, server = server)
