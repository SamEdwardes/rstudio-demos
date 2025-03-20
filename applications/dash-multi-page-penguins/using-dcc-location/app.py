# app.py

from dash import Dash, Input, Output, callback, dcc, html
from pages import index, page1, page2

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
        html.Div(
            [
                dcc.Link("Go to Home", href=app.get_relative_path("/")),
                html.Br(),
                dcc.Link("Go to Page 1", href=app.get_relative_path("/page1")),
                html.Br(),
                dcc.Link("Go to Page 2", href=app.get_relative_path("/page2")),
            ]
        ),
    ]
)


@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    pathname = app.strip_relative_path(pathname)
    if pathname == "":
        return index.layout
    elif pathname == "page1":
        return page1.layout
    elif pathname == "page2":
        return page2.layout
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
