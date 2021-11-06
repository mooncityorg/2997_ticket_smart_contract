# Import <
from dash import dcc, html
from backEnd.Tool import getJSON, application
from dash.dependencies import Input, Output, State

# >


style = getJSON(file = '/frontEnd/Resource/Verify.json')
authenticationLayout = html.Div(id = 'verifyLayoutId',
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
                                                                        debounce = True,
                                                                        id = 'inputCodeId',
                                                                        style = style['inputStyle'],
                                                                        placeholder = '6-Digit Code')

                                                          ], style = style['divCodeStyle']),

                                                 # >

                                                 # Verify <
                                                 html.Div(id = 'divVerifyId',
                                                          children = [

                                                              html.Button(n_clicks = 0,
                                                                          children = 'Verify',
                                                                          id = 'buttonVerifyId',
                                                                          style = style['verifyStyle'])

                                                          ], style = style['divVerifyStyle'])

                                                 # >

                                             ], style = style['divInputStyle'])

                                    # >

                                ])


#@application.callback(Output('verifyLayoutId', 'children'),
#                      Input())
