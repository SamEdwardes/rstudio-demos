# Check reticulate env vars
Sys.getenv("RETICULATE_PYTHON")
Sys.getenv("RETICULATE_PYTHON_FALLBACK")

library(reticulate)

# Check config
reticulate::py_config()

# Check standard lib
os <- import("os")
os$listdir(".")

# Check numpy
np <- import("numpy")
np$array(c(1, 2, 3))

# Check pandas
pd <- import("pandas")


library(reticulate)

np <- import("numpy")
np$array(c(1, 2, 3))
