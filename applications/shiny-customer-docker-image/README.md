# shiny-custom-docker

A Shiny app using a custom docker image.

## Docker

Build and push the docker image to a remote repository:

```bash
docker build --tag samedwardes/posit-connect-runtime:r4.1.3-pdftools --platform 'linux/amd64' .
docker push samedwardes/posit-connect-runtime:r4.1.3-pdftools
```

## Configure Connect

Connect must be configured to use image `samedwardes/posit-connect-runtime:r4.1.3-pdftools`. For example, if you are Helm to manage your Connect kubernetes deployment:

```yaml
# values.yaml
launcher:
  enabled: true
  defaultInitContainer:
    tagPrefix: jammy-
  customRuntimeYaml: base
  additionalRuntimeImages:
    - name: samedwardes/posit-connect-runtime:r4.1.3-pdftools
      r:
        installations:
          - path: /opt/R/4.1.3/bin/R
            version: 4.1.3
```

## Deploy to Connect

### Programtic Deployment

```r
rsconnect::deployApp(
  appDir = "app",
  image = "samedwardes/posit-connect-runtime:r4.1.3-pdftools"
)
```

### Git Backed Deployment

```r
rsconnect::writeManifest(
  appDir = "app",
  image = "samedwardes/posit-connect-runtime:r4.1.3-pdftools",
)
```