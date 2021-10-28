from dash import dcc
from dash import Dash
from dash import html


application = Dash(suppress_callback_exceptions = True)
server = application.server


application.layout = html.Div([

    html.H1('3ASJW6')

])


if (__name__ == '__main__'):

    application.run_server(debug = True)
