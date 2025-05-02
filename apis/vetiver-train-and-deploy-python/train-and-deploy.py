import os

import rsconnect
import vetiver
from sklearn.tree import DecisionTreeRegressor
from vetiver.data import mtcars

import pins

# Fit a a model.

car_mod = DecisionTreeRegressor().fit(mtcars.drop(columns="mpg"), mtcars["mpg"])

v = vetiver.VetiverModel(
    car_mod,
    model_name="sam.edwardes/cars_mpg",
    prototype_data=mtcars.drop(columns="mpg"),
)

# Save the model as a pin to Connect.

board = pins.board_rsconnect(
    server_url=os.getenv("CONNECT_SERVER"),
    api_key=os.getenv("CONNECT_API_KEY"),
    allow_pickle_read=True,
)

vetiver.vetiver_pin_write(board, v, versioned=True)

# Deploy the model to Connect as a REST API using FastAPI.

connect_server = rsconnect.api.RSConnectServer(
    url=os.getenv("CONNECT_SERVER"), api_key=os.getenv("CONNECT_API_KEY")
)

vetiver.deploy_rsconnect(
    connect_server=connect_server,
    board=board,
    pin_name="sam.edwardes/cars_mpg",
    title="Tree model for mtcars",
)
