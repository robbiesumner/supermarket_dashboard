import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, Input, Output, State, dcc

df = pd.read_csv('./data/supermarket_sales.csv')

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP],
           external_scripts=external_script, use_pages=True
           )

sidebar = html.Div([
    dcc.Link([
        html.P("Home")],
        href="/", className=""),
    dcc.Link([
        html.P("Summary")],
        href="summary-page", className=""),
    dcc.Link([
        html.P("Location")],
        href="location-page", className=""),
], className="pr-48 flex flex-col w-full h-full text-black text-left text-xl space-y-2",
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div("Supermarket Dashboard",
                     className="justify-self-start	 text-left pl-5 text-black text-4xl py-3 w-full"),
        ),
        dbc.Col([
            html.Button([html.I(className="bi bi-list")], id="open-offcanvas", n_clicks=0,
                        className="self-end text-right text-3xl w-full text-black rounded-xl align-middle h-full"),
        ],
        ),

    ], className="flex flex-row bg-slate-300 w-screen"),

    dbc.Row([
        dbc.Offcanvas(
            dbc.Col([html.Div([sidebar, html.Button([html.I(className="bi bi-x-lg")], id="close-offcanvas", n_clicks=0,
                                                    className="text-right sm:hidden text-3xl w-min text-black rounded-xl align-top h-full"),
                               ], className="flex flex-row")], width=8), id="offcanvas", title="Supermarket Dashboard",
            is_open=False,
            style={'horizontal-width': 10},

        ),
    ]),

    dbc.Col([dash.page_container], className=" py-3 grow w-full"),

    dbc.Row([
        html.P("Designed by Killian Lorenz, Robbie Summner, Frieder Löwe und Tjark Gerken",
               className="text-center py-1 bg-slate-300 text-slate-600 text-sm")
        ,
    ]),
], fluid=True,
    className="bg-white flex flex-col h-screen", )


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    Input("close-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run(debug=True)