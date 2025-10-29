library(shiny)
library(ggplot2)

# Load the penguin data (assuming it's already in your environment as 'penguins')
# If not, uncomment the next line:
# penguins <- read.csv("data.csv")

# Define UI
ui <- fluidPage(
  titlePanel("Penguin Flipper Length Explorer"),
  
  sidebarLayout(
    sidebarPanel(
      h4("Explore the Data"),
      
      # Species filter
      checkboxGroupInput("species_filter", 
                        "Select Species:",
                        choices = c("Adelie", "Chinstrap", "Gentoo"),
                        selected = c("Adelie", "Chinstrap", "Gentoo")),
      
      # Plot type selection
      radioButtons("plot_type", 
                  "Plot Type:",
                  choices = list(
                    "Scatter Plot" = "scatter",
                    "Box Plot" = "boxplot",
                    "Violin Plot" = "violin",
                    "Histogram" = "histogram"
                  ),
                  selected = "scatter"),
      
      # Show statistics
      checkboxInput("show_stats", "Show Summary Statistics", value = TRUE),
      
      hr(),
      
      # Additional options for scatter plot
      conditionalPanel(
        condition = "input.plot_type == 'scatter'",
        selectInput("color_by", 
                   "Color points by:",
                   choices = list(
                     "Species" = "species",
                     "Island" = "island",
                     "Sex" = "sex"
                   ),
                   selected = "species"),
        
        checkboxInput("add_smooth", "Add trend line", value = FALSE)
      )
    ),
    
    mainPanel(
      # Plot output
      plotOutput("main_plot", height = "500px"),
      
      # Statistics output
      conditionalPanel(
        condition = "input.show_stats",
        h4("Summary Statistics"),
        verbatimTextOutput("stats_output")
      ),
      
      # Data table
      h4("Filtered Data"),
      DT::dataTableOutput("data_table")
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  
  # Reactive data filtering
  filtered_data <- reactive({
    data <- penguins[!is.na(penguins$flipper_length_mm), ]
    data <- data[data$species %in% input$species_filter, ]
    return(data)
  })
  
  # Main plot
  output$main_plot <- renderPlot({
    data <- filtered_data()
    
    if(nrow(data) == 0) {
      plot(1, type="n", xlab="", ylab="", xlim=c(0, 10), ylim=c(0, 10))
      text(5, 5, "No data available for selected filters", cex=1.5)
      return()
    }
    
    if(input$plot_type == "scatter") {
      p <- ggplot(data, aes(x = species, y = flipper_length_mm)) +
        geom_jitter(aes_string(color = input$color_by), 
                   width = 0.2, alpha = 0.7, size = 2) +
        labs(title = "Flipper Length by Species",
             x = "Species",
             y = "Flipper Length (mm)") +
        theme_minimal() +
        theme(axis.text.x = element_text(angle = 45, hjust = 1))
      
      if(input$add_smooth) {
        p <- p + geom_smooth(method = "lm", se = TRUE, color = "red")
      }
      
    } else if(input$plot_type == "boxplot") {
      p <- ggplot(data, aes(x = species, y = flipper_length_mm, fill = species)) +
        geom_boxplot(alpha = 0.7) +
        labs(title = "Flipper Length Distribution by Species",
             x = "Species",
             y = "Flipper Length (mm)") +
        theme_minimal() +
        theme(axis.text.x = element_text(angle = 45, hjust = 1))
      
    } else if(input$plot_type == "violin") {
      p <- ggplot(data, aes(x = species, y = flipper_length_mm, fill = species)) +
        geom_violin(alpha = 0.7) +
        geom_boxplot(width = 0.1, alpha = 0.5) +
        labs(title = "Flipper Length Distribution by Species",
             x = "Species", 
             y = "Flipper Length (mm)") +
        theme_minimal() +
        theme(axis.text.x = element_text(angle = 45, hjust = 1))
      
    } else if(input$plot_type == "histogram") {
      p <- ggplot(data, aes(x = flipper_length_mm, fill = species)) +
        geom_histogram(alpha = 0.7, position = "identity", bins = 20) +
        facet_wrap(~species, ncol = 1) +
        labs(title = "Flipper Length Distribution by Species",
             x = "Flipper Length (mm)",
             y = "Count") +
        theme_minimal()
    }
    
    print(p)
  })
  
  # Summary statistics
  output$stats_output <- renderText({
    data <- filtered_data()
    
    if(nrow(data) == 0) {
      return("No data available for selected filters")
    }
    
    stats_by_species <- aggregate(flipper_length_mm ~ species, data = data, 
                                 function(x) c(
                                   Count = length(x),
                                   Mean = round(mean(x, na.rm = TRUE), 1),
                                   Median = round(median(x, na.rm = TRUE), 1),
                                   SD = round(sd(x, na.rm = TRUE), 1),
                                   Min = min(x, na.rm = TRUE),
                                   Max = max(x, na.rm = TRUE)
                                 ))
    
    # Format the output
    result <- ""
    for(i in 1:nrow(stats_by_species)) {
      species_name <- stats_by_species$species[i]
      stats <- stats_by_species$flipper_length_mm[i, ]
      
      result <- paste0(result, 
                      sprintf("%s (n=%d):\n", species_name, stats["Count"]),
                      sprintf("  Mean: %s mm, Median: %s mm\n", stats["Mean"], stats["Median"]),
                      sprintf("  SD: %s mm, Range: %s-%s mm\n\n", 
                             stats["SD"], stats["Min"], stats["Max"]))
    }
    
    return(result)
  })
  
  # Data table
  output$data_table <- DT::renderDataTable({
    data <- filtered_data()
    # Select relevant columns
    display_data <- data[, c("species", "island", "flipper_length_mm", "body_mass_g", "sex")]
    DT::datatable(display_data, 
                  options = list(pageLength = 10, scrollX = TRUE),
                  rownames = FALSE)
  })
}

# Run the application
shinyApp(ui = ui, server = server)