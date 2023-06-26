import dash
from dash import html, dcc

from python_dashboard.functions.plots import rating_graph, payment_graph, sales_over_time_graph, sales_graph

dash.register_page(__name__)

layout = html.Div([
    html.Div(className="flex flex-col  space-y-4 md:flex-row  md:space-y-0 md:space-x-4 justify-around align-center",
             children=[
                 html.Div(className="flex flex-col justify-center align-center", children=[
                     html.H1("Summary Page", className="text-4xl text-black font-bold"),
                     html.P(
                         "Big Picture of the Data.",
                         className="text-xl text-slate-900")
                 ]),
             ]),

    html.Div(className="flex flex-col space-y-4  justify-around align-center",
             children=[
                 html.Div(className="", children=[
                     html.Div(children=[
                         dcc.Graph(figure=rating_graph())
                     ])
                 ]),
                 html.Div(className="", children=[
                     html.Div(children=[
                         dcc.Graph(figure=payment_graph())
                     ])
                 ]),
                 html.Div(className="", children=[
                     html.Div(children=[
                         dcc.Graph(figure=sales_over_time_graph())
                     ])
                 ]),
                 html.Div(className="", children=[
                     html.Div(children=[
                         dcc.Graph(figure=sales_graph())
                     ])
                 ])
             ])
])
