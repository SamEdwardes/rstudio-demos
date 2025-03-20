"""
Train and deploy a linear model.

- The model is trained using sklearn.
- The fitted model from sklearn is passed into vetiver to create a vetiver model
  ojbect.
- Vetiver is used to pin the model weights to Connect.
- Vetiver is used to deploy the model as a FastAPI API to Connect.
"""

import os
import sys

import vetiver
from rsconnect.api import RSConnectServer
from sklearn.linear_model import LinearRegression
from vetiver.data import mtcars

import pins

# Fit a model ------------------------------------------------------------------

lm = LinearRegression().fit(mtcars, mtcars["mpg"])
username = os.getenv("USER")
model_name = f"{username}/mtcars-linear-model"

v = vetiver.VetiverModel(lm, model_name=model_name, save_ptype=True, ptype_data=mtcars)

# Pin model --------------------------------------------------------------------

board = pins.board_rsconnect(
    server_url=os.getenv("CONNECT_SERVER"),
    api_key=os.getenv("CONNECT_API_KEY"),
    allow_pickle_read=True,
)

vetiver.vetiver_pin_write(board, v)

# Deploy model -----------------------------------------------------------------

connect_server = RSConnectServer(
    url=os.getenv("CONNECT_SERVER"), api_key=os.getenv("CONNECT_API_KEY")
)

vetiver.deploy_rsconnect(
    connect_server=connect_server,
    board=board,
    pin_name=model_name,
    python=sys.executable,
)
