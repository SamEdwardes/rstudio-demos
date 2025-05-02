# The Colorado Report

## Git backed publishing

```r
rsconnect::writeManifest(
  appDir = ".",
  appPrimaryDoc = "colorado-report.qmd",
  quarto = quarto::quarto_path()
)
```

## Screenshot of email output

![Screenshot of email output](./imgs/colorado-report-email-screenshot.png)

## Screenshot of Posit Connect output

![Screenshot of Posit Connect output](./imgs/colorado-report-connect-screenshot.png)
