from dash import dcc
from dash import Dash
from dash import html

from backEnd.Tools import Tools

application = Dash(suppress_callback_exceptions = True)
server = application.server


application.layout = html.Div([

    html.Div(children = [

        html.H1('ok')

    ])

], style = {'background-image' : 'url(https://www.umkc.edu/global-assets/images/Womens-Soccer-at-the-Liberty-Memorial.jpg)'})


if (__name__ == '__main__'):

    x2 = Tools()

    p = x2.getPath()
    print(p)

    application.run_server(debug = True)
