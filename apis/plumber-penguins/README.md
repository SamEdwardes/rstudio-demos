# demo-plumber-penguins

A demo of how to use [Plumber](https://www.rplumber.io/index.html) to create APIs on RStudio Connect.

- Code: <https://github.com/SamEdwardes/demo-plumber-penguins>

![screenshot](imgs/screenshot.png)

## Usage

Using curl:

```bash
curl -L -X GET "https://pub.current.posit.team/public/plumber-penguins-2025-07-17/penguins?sample_size=2" -H "Content-Type: application/json" -H "Authorization: Key ${CONNECT_API_KEY}"
```

Using httpie:

```bash
uvx --from httpie https pub.current.posit.team/public/plumber-penguins-2025-07-17/penguins \
  "Authorization:Key ${CONNECT_API_KEY}" \
  sample_size==2
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
