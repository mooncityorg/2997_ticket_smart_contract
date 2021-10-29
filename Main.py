from dash import dcc
from dash import Dash
from dash import html

from backEnd.Tool import Tool


application = Dash(suppress_callback_exceptions = True)
server = application.server


application.layout = html.Div([



])


if (__name__ == '__main__'):

    application.run_server(debug = True)
