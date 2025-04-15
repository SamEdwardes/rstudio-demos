# Train and Deploy a Model with Python and Vetiver

## Set up

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```

## Train and deploy the model

The script `train-and-deploy.py` will train and deploy the model as REST API to Connect. Run the script using the following:

```bash
python train-and-deploy.py
```

Note the `Direct content URL` printed in the output. Export it as an environment variable `MODEL_URL`.

```bash
export MODEL_URL="https://colorado.posit.co/rsc/content/c2f189da-7626-48e7-9882-78ee6c49c1b9"
```

## Making predictions

### From Python

The notebook [make-predictions.ipynb](make-predictions.ipynb) includes examples of how to call the model API endpoint using Python.

### From the Shell

From the shell with no API key:

```bash
curl -X POST "${MODEL_URL}/predict" \
 -H "Accept: application/json" \
 -H "Content-Type: application/json" \
 -d '{"cyl":0,"disp":0,"hp":0,"drat":0,"wt":0,"qsec":0,"vs":0,"am":0,"gear":0,"carb":0}'

```

From the shell using an API key:

```bash
curl -X POST "${MODEL_URL}/predict" \
 -H "Accept: application/json" \
 -H "Content-Type: application/json" \
 -H "Authorization: Key ${CONNECT_API_KEY}" \
 -d '{"cyl":0,"disp":0,"hp":0,"drat":0,"wt":0,"qsec":0,"vs":0,"am":0,"gear":0,"carb":0}'
```
