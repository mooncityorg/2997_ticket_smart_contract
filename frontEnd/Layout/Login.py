from dash import dcc
from dash import html
from backEnd.Tool import getJSON


style = getJSON(file = '/frontEnd/Resource/Login.json')
loginLayout = html.Div([

    html.H1('h1')

], style = style['divStyle'])
