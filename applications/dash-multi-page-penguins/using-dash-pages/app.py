# Load environment variables before importing dash
from dotenv import load_dotenv
load_dotenv()

import dash # noqa: E402
import dash_bootstrap_components as dbc  # noqa: E402
import pandas as pd # noqa: E402
from dash import Dash, dcc, html # noqa: E402

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
data = pd.read_csv(url)

app.layout = dbc.Container(
    [
        html.H1("Meet the penguins!", style={"margin-top": "10pt"}),
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
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
