# shiny-custom-docker

A Shiny app using a custom docker image.

## Docker

Build and push the docker image to a remote repository:

```bash
docker build --tag samedwardes/posit-connect-runtime:r4.1.3-pdftools --platform 'linux/amd64' .
docker push samedwardes/posit-connect-runtime:r4.1.3-pdftools
```

## Deploy to Connect

### Programtic Deployment

```r
rsconnect::deployApp(
  appDir = "app",
  image = "samedwardes/posit-connect-runtime:r4.1.3-pdftools",
  server = "colorado"
)
```

### Git Backed Deployment

```r
rsconnect::writeManifest(
  appDir = "app",
  image = "samedwardes/posit-connect-runtime:r4.1.3-pdftools",
)
```