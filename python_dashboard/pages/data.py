import dash
from dash import html, dcc, callback, Output, Input, dash_table

from python_dashboard.functions.getData import get_data

dash.register_page(__name__)

data = get_data()

layout = html.Div(children=[
    html.Div(className="space-y-2", children=[
        html.Div(children=[
            dcc.Dropdown(options=["A", "B", "C"],
                         value=[],
                         multi=True,
                         id="store-selection", className="space-x-2 w-1/2")
        ], className=""),
        html.Div(className="", children=[
            dash_table.DataTable(data=data.to_dict("records"), page_size=15, id="data_table",
                                 style_table={"overflowX": "auto"})
        ]),
    ])
])


@callback(
    Output(component_id="data_table", component_property="data"),
    Input(component_id="store-selection", component_property="value")
)
def update_table(store_chosen):
    sliced_data = get_data(store_chosen)
    return sliced_data.to_dict("records")
