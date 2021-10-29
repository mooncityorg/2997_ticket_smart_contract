from dash import dcc
from dash import Dash
from dash import html

from Back End.Tools import

application = Dash(suppress_callback_exceptions = True)
server = application.server


application.layout = html.Div([

    html.Div(children = [

        html.H1(children = 'ok'),
        html.H1(children = 'me')

    ])

], style = {'background-image' : 'url(https://www.umkc.edu/global-assets/images/Womens-Soccer-at-the-Liberty-Memorial.jpg)'})


if (__name__ == '__main__'):

    application.run_server(debug = True)
