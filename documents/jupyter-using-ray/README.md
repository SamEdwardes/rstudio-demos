# Using Ray to Execute Parellel Code

For more details about Ray refer to <https://docs.ray.io/en/latest/ray-core/walkthrough.html>.

To get started create a new Python virtual environment and install the requirements.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```

Then you can run this notebook. To upload this notebook to Posit Connect run the following commands:

```bash
rsconnect deploy notebook \
  --python .venv/bin/python \
  --new \
  examples.ipynb
```