library(dplyr)
library(connectapi)

client <- connect(server = "https://colorado.rstudio.com/rsc")
sam_edawrdes_guid <- "d03a6b7a-c818-4e40-8ef9-84ca567f9671"

all_content <- get_content(client, owner_guid = sam_edawrdes_guid)

white_list <- c(
  "Using VS Code in Workbench",
  "bike_predict_model_r: a pinned list"
)

content_to_delete <-
  all_content |> 
  filter(
    !stringr::str_ends(title, " - Palmer Penguins"),
    !stringr::str_starts(title, "Bike Predict - "),
    !stringr::str_starts(title, "bike-predict-model-metrics:"),
    !title %in% white_list
  ) |> 
  select(
    guid,
    name,
    title,
    created_time,
    last_deployed_time
  )

content_to_delete |> 
  select(guid, title) |> 
  print(n=100)

print(content_to_delete, n = 100)

for (i in c(1:nrow(content_to_delete))) {
  glimpse(content_to_delete[i,])
  content <- as.list(content_to_delete[i,])
  item <- content_item(client, content$guid)
  content_delete(item)
}
  
