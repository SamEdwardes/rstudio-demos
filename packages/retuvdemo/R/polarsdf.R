pl <- NULL

.onLoad <- function(...) {
  reticulate::py_require("polars")
  pl <<- reticulate::import("polars", delay_load = TRUE)
}

#' Polars DataFrame
#'
#' @param df A data frame or similar object.
#'
#' @returns A Polars DataFrame.
#' @export
#'
#' @examples
#' polarsdf(iris)
polarsdf <- function(df) {
  pl$DataFrame(df)
}
