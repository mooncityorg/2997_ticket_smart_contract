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

                                    # Input <
                                    html.Div(id = 'divInputId',
                                             children = [

                                                 # Code <
                                                 html.Div(id = 'divCodeId',
                                                          children = [

                                                              dcc.Input(value = '',
                                                                        n_submit = 0,
                                                                        id = 'inputId',
                                                                        debounce = True,
                                                                        style = style['inputStyle'],
                                                                        placeholder = '6-Digit Code')

                                                          ]),

                                                 # >

                                                 # Verify <
                                                 html.Div(id = 'divVerifyId',
                                                          children = [

                                                              html.Button(n_clicks = 0,
                                                                          id = 'verifyId',
                                                                          children = 'Verify',
                                                                          style = style['verifyStyle'])

                                                          ])

                                                 # >

                                             ], style = style['divInputStyle'])

                                    # >

                                ])
