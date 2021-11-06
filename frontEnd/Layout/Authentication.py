# Import <
from dash import dcc, html
from backEnd.Tool import getJSON, application

# >


style = getJSON(file = '/frontEnd/Resource/Authentication.json')
authenticationLayout = html.Div(id = 'authenticationLayoutId',
                                children = [

                                    # Warning <
                                    dcc.ConfirmDialog(id = 'warningId',
                                                      message = 'The authentication you entered was incorrect.'),

                                    # >

                                    # <

                                ])
