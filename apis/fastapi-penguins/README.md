# demo-fastapi-penguins

- Code: <https://github.com/SamEdwardes/demo-fastapi-penguins>
- Deployment: <https://colorado.rstudio.com/rsc/demo-fastapi-penguins/docs>

![screenshot](imgs/screenshot.png)

## Usage

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```

Then run the app.

```bash
uvicorn app:app --reload
```

You could also call the API using `curl`:

```bash
curl -X 'GET' \
  'https://colorado.rstudio.com/rsc/demo-fastapi-penguins/penguins?sample_size=1' \
  -H 'accept: application/json'
```

If the API is private you will need to authenticate using your API key.

```bash
curl -X 'GET' \
  'https://colorado.rstudio.com/rsc/demo-fastapi-penguins/penguins?sample_size=1' \
  -H 'accept: application/json' \
  -H "Authorization: Key ${CONNECT_API_KEY}"
```

## Deployment

### Git-backed

The app is automatically deployed to RStudio connect using git backed deployment. Make any changes to the code, then run the following:

```bash
rsconnect write-manifest fastapi \
  --overwrite \
  --python .venv/bin/python \
  --entrypoint app:app \
  .
```

> ⚠️ Remember to update the app/requirements.txt file if you add any new packages.

### Programmatic

You can deploy the app using the rsconnect cli:

```bash
rsconnect deploy fastapi \
  --python .venv/bin/python \
  --entrypoint app:app \
  --new \
  .
```