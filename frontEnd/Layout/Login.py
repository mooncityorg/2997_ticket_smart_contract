# Import <
from dash import dcc, html
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application, Submit, Verify

# >


# Declaration <
backupLayout = None
style = getJSON(file = '/frontEnd/Resource/Login.json')

# >


loginLayout = html.Div(id = 'divLoginLayoutId',
                       children = [

                           # Submit Modal <
                           dbc.Modal(centered = True,
                                     id = 'submitModalId',
                                     children = [

                                         dbc.ModalBody([

                                             html.H4(style = style['submitH4Style'],
                                                     children = 'There was an error.'),

                                             dbc.FormText(style = style['submitFormTextStyle'],
                                                          children = 'The information you input was invalid.')

                                         ], style = style['modalStyle'])

                                     ]),

                           # >

                           # Verify Modal <
                           dbc.Modal(centered = True,
                                     id = 'verifyModalId',
                                     children = [

                                         dbc.ModalBody([

                                             html.H4(style = style['verifyH4Style'],
                                                     children = 'There was an error.'),

                                             dbc.FormText(style = style['verifyFormTextStyle'],
                                                          children = 'The information you input was invalid.')

                                         ], style = style['modalStyle'])

                                     ]),

                           # >

                           # Authenticate Modal <
                           dbc.Modal(centered = True,
                                     id = 'authenticateModalId',
                                     children = [

                                         dbc.ModalBody([

                                             # Header <
                                             dbc.Row(children = [

                                                 # Text <
                                                 dbc.Col(children = [

                                                     # Header <
                                                     html.H3(style = style['headerH3Style'],
                                                             children = 'Welcome to Connect++'),

                                                     html.H6(style = style['headerH6Style'],
                                                             children = 'You just received a code.'),

                                                     # >

                                                     # Body <
                                                     html.Hr(style = style['textHrStyle']),

                                                     html.H6(style = style['bodyH6Style'],
                                                             children = 'We use the code you give us to log into '
                                                                        'your UMKC Pathway account so we can get '
                                                                        'your name and current class schedule.'),

                                                     html.H6(style = style['bodyH6Style'],
                                                             children = 'This can take up to twenty seconds.'),

                                                     html.Hr(style = style['textHrStyle']),

                                                     # >

                                                 ])

                                                 # >

                                             ]),

                                             # >

                                             # Footer <
                                             dbc.Row(justify = 'between',
                                                     children = [

                                                         # Input <
                                                         dbc.Col(width = 'auto',
                                                                 children = [

                                                                     dbc.Input(n_submit = 0,
                                                                               debounce = True,
                                                                               type = 'password',
                                                                               placeholder = 'Code',
                                                                               id = 'authenticationInputId',
                                                                               style = style['authenticationInputStyle'])

                                                                 ]),

                                                         # >

                                                         # Button <
                                                         dbc.Col(width = 'auto',
                                                                 children = [

                                                                     dbc.Button(n_clicks = 0,
                                                                                children = 'Authenticate',
                                                                                id = 'authenticateButtonId',
                                                                                style = style['authenticationButtonStyle'])

                                                                 ])

                                                         # >

                                                     ])

                                             # >

                                         ], style = style['modalStyle'])

                                     ]),

                           # >

                           html.Div(id = 'divDivLoginLayoutId',
                                    children = [

                                        # Logo <
                                        dbc.Row(justify = 'center',
                                                children = [

                                                    dbc.Col(width = 4,
                                                            children = [

                                                                html.Div(id = 'logoDivStyle',
                                                                         children = [

                                                                             html.Img(src = style['logoImgSrc'],
                                                                                      style = style['logoImgStyle'])

                                                                         ], style = style['logoDivStyle'])

                                                            ])

                                                ]),

                                        # >

                                        # Input <
                                        dbc.Row(justify = 'center',
                                                children = [

                                                    dbc.Col(width = 10,
                                                            children = [

                                                                html.Div(id = 'inputDivId',
                                                                         children = [

                                                                             # Logo <
                                                                             html.H1(children = 'Connect++',
                                                                                     className = 'display-3',
                                                                                     style = style['logoH1Style']),

                                                                             html.P(className = 'lead',
                                                                                    children = 'by 3ASJW6',
                                                                                    style = style['logoPStyle']),

                                                                             # >

                                                                             # Username <
                                                                             dbc.Row(justify = 'center',
                                                                                     children = [

                                                                                         dbc.Col(width = 3,
                                                                                                 children = [

                                                                                                     dbc.FormFloating(children = [

                                                                                                         dbc.Input(id = 'usernameInputId',
                                                                                                                   placeholder = 'Username',
                                                                                                                   style = style['usernameInputStyle']),
                                                                                                         dbc.Label('Username')

                                                                                                     ])

                                                                                                 ])

                                                                                     ]),

                                                                             # >

                                                                             # Password <
                                                                             dbc.Row(justify = 'center',
                                                                                     children = [

                                                                                         dbc.Col(width = 3,
                                                                                                 children = [

                                                                                                     dbc.FormFloating(children = [

                                                                                                         dbc.Input(n_submit = 0,
                                                                                                                   debounce = True,
                                                                                                                   type = 'password',
                                                                                                                   id = 'passwordInputId',
                                                                                                                   placeholder = 'Password',
                                                                                                                   style = style['passwordInputStyle']),
                                                                                                         dbc.Label('Password')

                                                                                                     ])

                                                                                                 ])

                                                                                     ]),

                                                                             # Forgot Password <
                                                                             dbc.Row(justify = 'center',
                                                                                     children = [

                                                                                         dbc.Col(width = 'auto',
                                                                                                 children = [

                                                                                                     dbc.Badge(children = 'Forgot Password',
                                                                                                               href = style['forgotPasswordBadgeHref'],
                                                                                                               color = style['forgotPasswordBadgeColor'],
                                                                                                               style = style['forgotPasswordBadgeStyle'])

                                                                                                 ])

                                                                                     ]),

                                                                             # >

                                                                             # Submit <
                                                                             dbc.Row(justify = 'center',
                                                                                     children = [

                                                                                         dbc.Col(width = 'auto',
                                                                                                 children = [

                                                                                                     dbc.Badge(href = '#',
                                                                                                               n_clicks = 0,
                                                                                                               children = 'Submit',
                                                                                                               id = 'submitBadgeId',
                                                                                                               color = style['submitBadgeColor'],
                                                                                                               style = style['submitBadgeStyle'])

                                                                                                 ])

                                                                                     ])

                                                                         ], style = style['inputDivStyle'])

                                                            ])

                                                ]),

                                        # >

                                        # Redirect <
                                        dbc.Row(justify = 'center',
                                                children = [

                                                    dbc.Col(width = 10,
                                                            children = [

                                                                html.Div(id = 'redirectDivId',
                                                                         children = [

                                                                             dbc.Badge(children = '3ASJW6',
                                                                                       href = style['redirectBadgeHref'],
                                                                                       color = style['redirectBadgeColor'],
                                                                                       style = style['redirectBadgeStyle'])

                                                                         ], style = style['redirectDivStyle'])

                                                            ])

                                                ])

                                        # >

                                    ], style = style['divDivLoginLayoutStyle'])

                       ])
