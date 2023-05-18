library(shiny)
library(pdftools)

ui <- fluidPage(
  titlePanel("PDF to Text"),
  sidebarLayout(
    sidebarPanel(
      textInput("pdf_url", label = "URL to PDF", value = "http://arxiv.org/pdf/1403.2805.pdf"),
      actionButton("convert_to_text", label = "Convert PDF to Text")
    ),
    mainPanel(
      p("Don't have a PDF to convert? Try these examples:"),
      tags$ul(
        tags$li("http://arxiv.org/pdf/1403.2805.pdf"),
        tags$li("https://github.com/SamEdwardes/spacypdfreader/raw/main/tests/data/test_pdf_01.pdf")
      ),
      verbatimTextOutput("txt")
    )
  )
)


server <- function(input, output, session) {
  
  v <- reactiveValues(
    txt = "Press the 'Convert PDF to Text' button to genreate the PDF text." 
  )
  
  observeEvent(input$convert_to_text, {
    tryCatch(
      {
        tmp <- tempfile()
        download.file(input$pdf_url, tmp, mode = "wb")
        v$txt <- pdf_text(tmp)
      },
      error = function(cond) {
        v$txt <- "There was an error with the PDF provided. Please try a different PDF."
      }
    )
    
  })
  
  # Render outputs
  output$txt <- renderText(v$txt)
  
}

shinyApp(ui = ui, server = server)
