# Shiny for R with Reticulate

Any example of how to publish a Shiny for R application that uses reticulate to Connect.

## Developing on Workbench

### Usage

- Create a new virtual environment

```bash
python -m venv .venv
source .venv/bin/activate 
python -m pip install --upgrade pip wheel setuptools
```

- Create a requirements.txt file that defines your dependencies. You should pin the versions. For example:

```test
numpy==1.26.0
```

- Install the requirements into your virtual environment.

```bash
python -m pip install -r requirements.txt
```

**Important**

- Set the `RETICULATE_PYTHON` environment variable to instruct reticulate which python interpeter to use. Set the value in the `.Renviron` file.

```bash
# .Renviron
# Tell reticulate to use your virtual environment in your development environment
# (e.g. Workbench). When you deploy to Connect, this value will be ignored. Connect
# will automatically create a virtual environment using the requirements.txt file
# and use that environment.
RETICULATE_PYTHON="./.venv/bin/python3"
```

You will now be able to use Python in your R code!

```R
library(reticulate)

np <- import("numpy")
np$array(c(1, 2, 3))
```

### Troubleshooting Reticulate on Workbench

- Run these commands:

```R
> Sys.getenv("RETICULATE_PYTHON")
> Sys.getenv("RETICULATE_PYTHON_FALLBACK")
> reticulate::py_config()
```

- If you reticulate cannot find numpy. E.g.:

```R
> reticulate::py_config()
Error in normalizePath(conda, winslash = "/", mustWork = TRUE) : 
  path[1]="/opt/python/3.9.6/bin/conda": No such file or directory
python:         /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv/bin/python3
libpython:      /opt/python/3.10.11/lib/libpython3.10.so
pythonhome:     /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv:/usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv
version:        3.10.11 (main, Jun  4 2023, 22:34:21) [GCC 11.3.0]
numpy:           [NOT FOUND]
```

- Try installing numpy from source:

```bash
python -m pip install --force-reinstall --no-binary numpy numpy
```

## Deployment

### Git-backed

Update the code, and then run:

```r
rsconnect::writeManifest(
  appFiles = c("app.R", "requirements.txt"),
)
```

The app will be automatically redeployed by RStudio Connect.

### Programatic

You can also deploy the app using the `rsconnect` api:

```r
rsconnect::deployApp(
  appFiles = c("app.R", "requirements.txt"),
  appTitle = "Shiny for R with Reticulate"
)
```

