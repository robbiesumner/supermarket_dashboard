import dash
from dash import html, dcc

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
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),

        html.Div(children=[html.H1('Go to the Location Page', className="text-4xl"),
                           html.P('The Location Page display the Data for each Location individually.',
                                  className="text-black my-3"),
                           dcc.Link([
                               html.Button(["Location Page"], id='summary-page', n_clicks=0,
                                           className='bg-cyan-500 w-56 hover:bg-slate-700 text-white font-bold py-2 px-4 rounded-xl')],
                               href="location-page", className="self-center ")
                           ],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),

    ], className="flex flex-col md:flex-row space-y-5 md:space-x-5 md:space-y-0"),
    html.H1('Our KPIs', className="text-4xl"),
    html.Div(children=[
        html.Div(children=[html.H1('Sales last Month', className="text-4xl"),
                           html.Div(children=[html.P("42000", className="text-cyan-700 text-6xl font-extrabold"),
                                              html.P(" €", className="text-cyan-700 text-6xl align-text-bottom")],
                                    className="flex flex-row h-full")],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),
        html.Div(children=[html.H1('Sales last Month', className="text-4xl"),
                           html.Div(children=[html.P("42000", className="text-cyan-700 text-6xl font-extrabold"),
                                              html.P(" €", className="text-cyan-700 text-6xl align-text-bottom")],
                                    className="flex flex-row h-full")],
                 className="flex flex-col px-6 justify-center w-full bg-slate-100 h-max py-10 rounded-2xl"),

    ], className="flex flex-col md:flex-row space-y-5 md:space-x-5 md:space-y-0"),

], className="flex flex-col h-full w-full justify-items-center space-y-5")
