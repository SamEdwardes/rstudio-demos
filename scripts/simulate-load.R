# Set the number of rows in data set.
n_rows <- 1000000

# Set the number of columns in data set.
n_cols <- 10

# Set the number of times to fit a model.
n_iterations <- 100

# Get start time.
start_time <- Sys.time()

# Create a data set with random values.For example:
df <- data.frame(matrix(
  rnorm(n_rows * n_cols),
  nrow = n_rows,
  ncol = n_cols
))


# Fit a linear model to the data for n_iterations times.
for (i in 1:n_iterations) {
  print(paste("Fitting model - iteration #", i))
  fit <- lm(X1 ~ ., data = df)
}

# Get end time.
end_time <- Sys.time()

# Get the total run time.
total_time <- difftime(
  start_time,
  end_time,
)

print(total_time)
