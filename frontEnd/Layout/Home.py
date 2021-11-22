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

                              dbc.Col(

                                  # Background <
                                  html.Div(id = 'divLogoId',
                                           children = [

                                               dbc.Row([

                                                   dbc.Col(

                                                       html.Img(src = style['logoSrc'],
                                                                style = style['logoStyle']),

                                                   width = 'auto'),

                                                   dbc.Col(

                                                       dbc.FormFloating([

                                                           dbc.Input(type = 'email', placeholder = '#'),
                                                           dbc.Label('email address')

                                                       ]),

                                                   width = 'auto')

                                               ], justify = 'between')

                                           ], style = style['divLogoStyle']),

                                  # >

                              width = True)

                          ]),

                          # >

                          # Body <
                          dbc.Row([

                              # Navigation Bar <
                              dbc.Col(

                                  html.Div(id = 'divMenuId',
                                           children = [

                                               #

                                           ], style = style['divMenuStyle']),

                              width = 1),

                              # >

                              # Dashboard <
                              dbc.Col(

                                  html.Div(id = 'divDashboardId',
                                           children = [

                                               #

                                           ], style = style['divDashboardStyle']),

                              width = True)

                              # >

                          ], className = 'g-0')

                          # >

                      ], style = style['homeLayoutStyle'])
