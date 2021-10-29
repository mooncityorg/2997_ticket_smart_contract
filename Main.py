from dash import Dash
from frontEnd.Layout.Login import loginLayout


application = Dash(suppress_callback_exceptions = True)
server, application.layout = application.server, loginLayout


if (__name__ == '__main__'):

    application.run_server(debug = True)


