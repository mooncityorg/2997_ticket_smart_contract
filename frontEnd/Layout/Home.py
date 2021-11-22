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

                                  html.Div(id = 'divHeaderId',
                                           children = [

                                               html.Img(src = style['logoSrc'],
                                                        style = style['logoStyle'])

                                           ], style = style['divHeaderStyle']),

                              width = True)

                          ]),

                          # >

                          # Body <
                          dbc.Row([

                              # Navigation Bar <
                              dbc.Col(

                                  html.Div(id = 'divMenuId',
                                           children = [

                                               html.H1('ok')

                                           ], style = style['divMenuStyle']),

                              width = 2),

                              # >

                              # Dashboard <
                              dbc.Col(

                                  html.Div(id = 'divDashboardId',
                                           children = [

                                               html.H1('ok')

                                           ], style = style['divDashboardStyle']),

                              width = True)

                              # >

                          ], className = 'g-0')

                          # >

                      ], style = style['homeLayoutStyle'])
