# Import <
from dash import dcc, html
from backEnd.Tool import getJSON, application
from dash.dependencies import Input, Output, State

# >


style = getJSON(file = '/frontEnd/Resource/Authentication.json')
authenticationLayout = html.Div(id = 'authenticationLayoutId',
                                children = [

                                    # Warning <
                                    dcc.ConfirmDialog(id = 'warningId',
                                                      message = 'The authentication you entered was incorrect.'),

                                    # >

                                    # <
                                    html.Div(id = 'divInputId',
                                             children = [

                                                 html.H1('ok')

                                             ])

                                    # >

                                ])
