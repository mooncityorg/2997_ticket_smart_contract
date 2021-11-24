# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application

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
                                  html.Div(id = 'divHeaderBackgroundId',
                                           children = [

                                               # Content <
                                               dbc.Row([

                                                   # <
                                                   dbc.Col(

                                                       dbc.InputGroup([

                                                           #

                                                       ]),

                                                   align = 'center', width = 'auto'),

                                                   # >

                                                   # Search <
                                                   dbc.Col(

                                                       dbc.InputGroup([

                                                           # by Name <
                                                           dcc.Dropdown(id = 'byNameId',
                                                                        placeholder = 'by Name',
                                                                        style = style['byNameStyle']),
                                                                        # requirement:
                                                                        # options = method that returns:
                                                                            # label : name, value : userId

                                                           # >

                                                           # filter Role <
                                                           dcc.Dropdown(multi = True,
                                                                        id = 'filterRole',
                                                                        value = 'student',
                                                                        placeholder = 'filter Role',
                                                                        style = style['filterRoleStyle'],
                                                                        options = [

                                                                            {'label' : l, 'value' : v}

                                                                        for l, v in style['filterRoleOptions'].items()])

                                                           # >

                                                       ]),

                                                   align = 'center', width = 'auto')

                                                   # >

                                               ], justify = 'between')

                                               # >

                                           ], style = style['divHeaderBackgroundStyle']),

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

                              width = 'auto'),

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


@application.callback(Output('inputGroupTextId', 'children'),
                      Input('dropdownMenuSearchId', 'label'))
def dropdownFunction(value: str) -> list:
    '''  '''

    print(value)
