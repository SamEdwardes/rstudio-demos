import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
import dash

dash.register_page(
    __name__, 
    order=1, 
    name="Distribution of Flipper Length"
)

url = "https://github.com/allisonhorst/palmerpenguins/raw/master/inst/extdata/penguins.csv"
data = pd.read_csv(url)

def plot_histogram():
    fig = go.Figure()
    for i in data["species"].unique():
        fig.add_trace(
            go.Histogram(
                x=data.loc[data["species"] == i, "flipper_length_mm"],
                name=i
            )
        )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title="Distribution of Flipper Length",
        barmode='overlay',
        showlegend=False
    )
    return fig


layout = html.Div(
    dcc.Graph(figure=plot_histogram())
)