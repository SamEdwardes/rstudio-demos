library(shiny)
library(dplyr)
library(safejoin)


ui <- fluidPage(
  
  titlePanel("Cross platform OS Test"),
  p("Total Number of Packages:"),
  verbatimTextOutput("numPackages"),
  tableOutput("availablePackages")

)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$numPackages <- renderPrint({
    installed.packages() |> 
      as_tibble() |> 
      nrow()
  })
  
  output$availablePackages <- renderTable({
    installed.packages() |> 
      as_tibble() |>
      select(
        Package,
        LibPath,
        Version,
        OS_type,
        NeedsCompilation,
        Built
      )
  })
    
}

# Run the application 
shinyApp(ui = ui, server = server)
