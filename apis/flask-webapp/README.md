# Flask Webapp

This repo is an example of how to deploy a Flask "Webapp" to Posit Connect. A webapp is very similar to a normal Flask API. The main difference is that it returns HTML instead of JSON.

## Usage

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
```

Then run the app.

```bash
flask --debug --app "app/app.py" run
```

## Deployment

### Git-backed

The app is automatically deployed to Posit connect using git backed deployment. Make any changes to the code, then run the following:

```bash
rsconnect write-manifest api \
    --overwrite \
    --python .venv/bin/python \
    --entrypoint app.app:app \
    .
```

> ⚠️ Remember to update the app/requirements.txt file if you add any new packages.

### Programmatic

You can deploy the app using the rsconnect cli:

```bash
rsconnect deploy api \
    --title "Flask Webapp Example" \
    --entrypoint "app.app:app" \
    --python ".venv/bin/python" \
    .
```