import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
import dash

dash.register_page(
    __name__, 
    order=2, 
    name="Bill Length vs. Flipper Length"
)

url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
data = pd.read_csv(url)


def plot_scatter():
    fig = go.Figure()
    for i in data["species"].unique():
        fig.add_trace(
            go.Scatter(
                x=data.loc[data["species"] == i, "flipper_length_mm"],
                y=data.loc[data["species"] == i, "bill_length_mm"],
                name=i,
                mode="markers"
            )
        )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title="Bill Length vs. Flipper Length",
    )
    return fig


layout = html.Div(
    dcc.Graph(figure=plot_scatter())
)
