import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

from python_dashboard.functions.getData import get_data

dash.register_page(__name__)

layout = html.Div([
    html.Div(className='flex flex-col  space-y-4 md:flex-row  md:space-y-0 md:space-x-4 justify-around align-center',
             children=[
                 html.Div(className='flex flex-col justify-center align-center', children=[
                     html.H1("Summary Page", className="text-4xl text-black font-bold"),
                     html.P(
                         "Big Picture of the Data.",
                         className="text-xl text-slate-900")
                 ]),
             ]),

    html.Div(className='flex flex-col space-y-4  justify-around align-center',
             children=[
                 html.Div(className='', children=[
                     html.Div(children=[
                         dcc.Graph(figure={}, id='sales-chart')
                     ])
                 ]),
                 html.Div(className='', children=[
                     html.Div(children=[
                         dcc.Graph(figure={}, id='sale-chart')
                     ])
                 ]),
                 html.Div(className='', children=[
                     html.Div(children=[
                         dcc.Graph(figure={}, id='rating-chart')
                     ])
                 ])
             ])
])


@callback(
    Output(component_id='sales-chart', component_property='figure'),
    Input(component_id='store-selection', component_property='value')
)
def update_graph(store_chosen):
    sliced_data = get_data(store_chosen)
    if sliced_data.empty:
        return {}
    else:
        fig = px.box(sliced_data, x='Produktlinie', y='Bruttoeinkommen', color='Produktlinie', points="all", )
    return fig


@callback(
    Output(component_id='rating-chart', component_property='figure'),
    Input(component_id='store-selection', component_property='value')
)
def update_graph(store_chosen):
    sliced_data = get_data(store_chosen)
    if sliced_data.empty:
        return {}
    else:
        fig = px.box(sliced_data, x='Produktlinie', y='Bewertung', color='Produktlinie', points="all", )
    return fig


@callback(
    Output(component_id='sale-chart', component_property='figure'),
    Input(component_id='store-selection', component_property='value')
)
def update_graph(store_chosen):
    sliced_data = get_data(store_chosen)
    if sliced_data.empty:
        return {}
    sliced_data = sliced_data.groupby(['Datum']).sum().reset_index()
    print(sliced_data)
    fig = px.line(sliced_data, x='Datum', y='Bruttoeinkommen')
    return fig

# Histogram zeitverteilung als Graph
