import datetime

import dash
import pandas as pd
from dash import html, dcc

from python_dashboard.functions.getData import get_data
from python_dashboard.functions.getGrowth import calculate_growth
from python_dashboard.functions.getSalesTimeFrame import get_sales_sum_timeframe

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[html.H1('Go to the Summary Page', className="text-4xl"),
                           html.P(
                               'On the summary page you can find a overview about the state of our Supermarket Enterprise',
                               className="text-black my-3"),
                           dcc.Link([
                               html.Button(["Summary Page"], id='summary-page', n_clicks=0,
                                           className='bg-cyan-500 w-56 hover:bg-slate-700 text-white font-bold py-2 px-4 rounded-xl')],
                               href="summary-page", className="self-center")
                           ],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-full py-10 rounded-2xl"),

        html.Div(children=[html.H1('Go to the Location Page', className="text-4xl"),
                           html.P('The Location Page display the Data for each Location individually.',
                                  className="text-black my-3"),
                           dcc.Link([
                               html.Button(["Location Page"], id='summary-page', n_clicks=0,
                                           className='bg-cyan-500 w-56 hover:bg-slate-700 text-white font-bold py-2 px-4 rounded-xl')],
                               href="location-page", className="self-center ")
                           ],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-100 py-10 rounded-2xl"),
        html.Div(children=[html.H1('Checkout the data', className="text-4xl"),
                           html.P(
                               'Find out where the analysis is coming from and how the data is structured.',
                               className="text-black my-3"),
                           dcc.Link([
                               html.Button(["Data "], id='summary-page', n_clicks=0,
                                           className='bg-cyan-500 w-56 hover:bg-slate-700 text-white font-bold py-2 px-4 rounded-xl')],
                               href="data", className="self-center md:self-left")
                           ],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-full py-10 rounded-2xl"),
    ], className="flex flex-col lg:flex-row space-y-5 lg:space-x-5 lg:space-y-0 items-stretch"),

    html.H1('Our KPIs', className="text-4xl"),
    html.Div(children=[
        html.Div(children=[html.H1('All time Sales', className="text-4xl"),
                           html.Div(children=[html.P(round(get_data()["Bruttoeinkommen"].sum(), 2),
                                                     className="text-cyan-700 text-6xl font-extrabold"),
                                              html.P(" €", className="text-cyan-700 text-6xl align-text-bottom")],
                                    className="flex flex-row h-full")],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),
        html.Div(children=[html.H1('Sales in the last Month Data was collected', className="text-4xl"),
                           html.Div(children=[html.P(get_sales_sum_timeframe(
                               start_date=pd.to_datetime(get_data()["Datum"].max()) - datetime.timedelta(days=30)),
                               className="text-cyan-700 text-6xl font-extrabold"),
                               html.P(" €", className="text-cyan-700 text-6xl align-text-bottom")],
                               className="flex flex-row h-full")],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),
        html.Div(children=[html.H1('Growth compared to the previous month', className="text-4xl"),
                           html.Div(children=[html.P(calculate_growth(),
                                                     className="text-cyan-700 text-6xl font-extrabold"),
                                              html.P(" %", className="text-cyan-700 text-6xl align-text-bottom")],
                                    className="flex flex-row h-full")],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),
        html.Div(children=[html.H1('All Time Rating Average', className="text-4xl"),
                           html.Div(children=[
                               html.P(str(round(get_data()["Bewertung"].mean(), 2)) + " / 10",
                                      className="text-cyan-700 text-6xl font-extrabold"),
                               html.I(
                                   className="bi bi-star-fill text-yellow-400 text-5xl align-text-center self-middle")],
                               className="flex flex-row h-full items-center space-x-2")
                           ],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),

    ], className="grid grid-cols-1 md:grid-cols-2 gap-4"),

], className="flex flex-col h-full w-full justify-items-center space-y-5")
