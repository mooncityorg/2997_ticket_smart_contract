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

                                                   # Logo <
                                                   dbc.Col(

                                                       html.Img(src = style['logoSrc'],
                                                                style = style['logoStyle']),

                                                   width = 'auto'),

                                                   # >

                                                   # Search <
                                                   dbc.Col(

                                                       dbc.InputGroup([

                                                           dbc.Input(id = 'inputSearchId',
                                                                     placeholder = 'Search'),
                                                           dbc.InputGroupText(id = 'inputGroupTextId'),
                                                           dbc.DropdownMenu(label = 'Role',
                                                                            id = 'dropdownMenuSearchId',
                                                                            color = style['dropdownMenuSearchColor'],
                                                                            children = [

                                                                                dbc.DropdownMenuItem(i)

                                                                            for i in style['dropdownMenuSearchChildren']])

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
