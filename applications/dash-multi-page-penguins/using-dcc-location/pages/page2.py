# pages/page2.py

from dash import Input, Output, callback, dcc, html

layout = html.Div(
    [
        html.H3("Page 2"),
        dcc.Dropdown(
            {f"Page 2 - {i}": f"{i}" for i in ["London", "Berlin", "Paris"]},
            id="page-2-dropdown",
        ),
        html.Div(id="page-2-display-value"),
    ]
)


@callback(Output("page-2-display-value", "children"), Input("page-2-dropdown", "value"))
def display_value(value):
    return f"You have selected {value}"
