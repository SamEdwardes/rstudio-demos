# demo-jupyter-python-penguins

## Set up

```bash
# set up a virtual environment
/opt/python/3.10.4/bin/python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt

# register the venv as kernel
python -m ipykernel install --user --name demo-jupyter-python-penguins-3-10-4
```

## Deploy

### Git-backed deploy

The app is automatically deployed to RStudio connect using git backed deployment. Make any changes to the code, then run the following:

```bash
rsconnect write-manifest notebook \
  --overwrite \
  --python venv/bin/python \
  notebook.ipynb
```

> ⚠️ Remember to update the app/requirements.txt file if you add any new packages.

### Programtic deploy

You can deploy the app using the rsconnect cli:

```bash
rsconnect deploy notebook \
  --python venv/bin/python \
  --new \
  notebook.ipynb
```
