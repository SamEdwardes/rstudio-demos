# demo-plumber-penguins

A demo of how to use [Plumber](https://www.rplumber.io/index.html) to create APIs on RStudio Connect.

- Code: <https://github.com/SamEdwardes/demo-plumber-penguins>

![screenshot](imgs/screenshot.png)

## Usage

```bash
curl -X GET "https://pub.current.posit.team/content/8491faf4-d37d-44ce-9499-12dc67c15ddf/penguins?sample_size=2" -H "Content-Type: application/json" -H "Authorization: Key ${CONNECT_API_KEY}"
```

## Deployment

### Git-backed

After making any code changes run the following:

```r
rsconnect::writeManifest("app")
```

RStudio Connect will then automatically redeploy the app.

### Programatic

You can also deploy the app using the `rsconnect` api:

```r
rsconnect::deployAPI(
  api = "app",
  appFiles = c("plumber.R"),
  appTitle = "Shiny Penguins Plumber"
)
```
