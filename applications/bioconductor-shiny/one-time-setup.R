# Install renv
install.packages("renv")

# Check your settings before enabling renv
getOption("repos")

# Setup and configure renv for the project
renv::init(
  # Renv will automatically detect the correct bioconductor version to use
  # based on your R version. You can also check for yourself here:
  # https://p3m.dev/client/#/repos/bioconductor/setup.
  # Setting bioconductor true will also set the correct repos (e.g. BioCsoft, 
  # BioCann, etc.)
  bioconductor = TRUE,
  repos = c(
    CRAN = "https://p3m.dev/cran/latest"
  ),
  settings = list(
    # Use binary linux packages when available
    ppm.enabled = TRUE
  )
)

# Check the results
BiocManager::repositories()
getOption("repos")
