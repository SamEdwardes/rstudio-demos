# demo-streamlit-penguins

- Code: <https://github.com/SamEdwardes/demo-streamlit-penguins>
- Deployment: <https://colorado.rstudio.com/rsc/demo-streamlit-penguins/>

![screenshot](imgs/app-screenshot.png)

## Usaage

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r app/requirements.txt
```

Then run the app.

```bash
streamlit run app/app.py
```

## Deployment

### Git-backed deploy

The app is automatically deployed to RStudio connect using git backed deployment. Make any changes to the code, then run the following:

```bash
rsconnect write-manifest streamlit \
  --overwrite \
  --python .venv/bin/python \
  --entrypoint app \
  app
```

> ⚠️ Remember to update the `app/requirements.txt` file if you add any new packages. 

### Programatic deploy

You can deploy the app using the rsconnect cli:

```bash
rsconnect deploy streamlit \
  --python .venv/bin/python \
  --entrypoint app \
  --new \
  app
```

