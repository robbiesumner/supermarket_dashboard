import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div([
    html.Div(className='flex flex-col  space-y-4 md:flex-row  md:space-y-0 md:space-x-4 justify-around align-center',
             children=[
                 html.Div(className='flex flex-col justify-center align-center', children=[
                     html.H1("Location Page", className="text-4xl text-black font-bold"),
                     html.P(
                         "On this Page you can find the different plots showing the situation and performance of the Stores.",
                         className="text-xl text-slate-900")
                 ]),
                 html.Div(className='py-2 md:py-4 px-2 bg-slate-400  w-full md:w-max rounded-xl', children=[
                     html.H2("Choose your Store", className="text-xl text-white font-bold "),
                     dcc.RadioItems(options=['A', 'B', 'C'],
                                    value='A',
                                    inline=True,
                                    id='store-selection',
                                    className="space-x-4 py-2 text-white text-left md:text-center")
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


