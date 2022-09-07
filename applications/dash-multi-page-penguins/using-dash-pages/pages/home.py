from textwrap import dedent

import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(
    __name__,
    path="/",
    order=0
)

layout = dbc.Row(children=[
    dbc.Col(
        style={"display": "flex"},
        children=[
            html.Div(
                style={'margin': 'auto'}, 
                children=dedent(
                    """
                    The data was collected and made available by Dr. Kristen Gorman and the Palmer 
                    Station, Antarctica LTER, a member of the Long Term Ecological Research Network.
                    """
                ).strip()
            )
        ]
    ),
    dbc.Col([
        html.Img(
            src="https://allisonhorst.github.io/palmerpenguins/reference/figures/lter_penguins.png",
            width=200
        )
    ], style={'text-align': 'center'}),
])
