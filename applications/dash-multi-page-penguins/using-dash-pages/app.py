import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
url = "https://github.com/allisonhorst/palmerpenguins/raw/master/inst/extdata/penguins.csv"
data = pd.read_csv(url)

app.layout = dbc.Container([
    html.H1('Meet the penguins!', style={'margin-top': '10pt'}),
    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),
	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
