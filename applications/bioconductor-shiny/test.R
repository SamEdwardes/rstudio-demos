renv::init(
  bioconductor = TRUE,
  # Optionally add the repos argument to a "time stamped" repo.
  # This is not strictly required, as renv will make note of the package
  # version initially installed, but it will prevent people from upgrading to
  # newer versions in the future that may not work with the version of 
  # bioconductor you are using. You can get the right date to use
  # from the Pacakge Manager UI: 
  # https://packagemanager.posit.co/client/#/repos/bioconductor/setup?bioconductor_version=3.18&snapshot=latest&distribution=ubuntu-22.04
  repos = c(
    CRAN = "https://pkg.current.posit.team/cran/__linux__/jammy/2024-05-01"
  )
)
