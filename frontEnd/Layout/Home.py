# Import <
from dash import html, dcc
from backEnd.API.Utility import getJSON
import dash_bootstrap_components as dbc

# >


# Declaration <
# note: we get a user's data in here
# and not in Login.py. in Login.py we
# set the data for a user.
style = getJSON(file = '/frontEnd/Resource/Home.json')

# >


homeLayout = html.Div(id = 'homeLayoutId',
                      children = [

                          # Header <
                          dbc.Row([

                              dbc.Col(html.Div("One of three columns"), width = 4),
                              dbc.Col(html.Div("One of three columns"), width = 4),
                              dbc.Col(html.Div("One of three columns"), width = 4),

                          ], justify = 'center')

                          # >

                          # Navigation Bar <


                          # >

                      ], style = style['homeLayoutStyle'])
