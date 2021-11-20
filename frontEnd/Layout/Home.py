# Import <
from dash import html, dcc
from backEnd.API.Utility import getJSON

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
                          html.Div(id = 'divHeaderId',
                                   children = [

                                       # Logo <
                                       html.Div(id = 'divLogoId',
                                                children = [

                                                    html.H1(children = 'Connect++',
                                                            style = style['h1Style'])

                                                ], style = style['divLogoStyle']),

                                       # >

                                       # Search <
                                       html.Div(id = 'divSearchId',
                                                children = [

                                                    dcc.Dropdown(id = 'dropdownId',
                                                                 options = [



                                                                 ])

                                                ], style = style['divSearchStyle'])

                                       # >

                                   ], style = style['divHeaderStyle'])

                          # >

                          # Navigation Bar <


                          # >

                      ], style = style['homeLayoutStyle'])
