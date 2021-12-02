# Import <
from dash import dcc, html
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application
from backEnd.API.Utility import Submit, Verify, Authenticate

# >


# Declaration <
style = getJSON(file = '/frontEnd/Resource/Login.json')
driver, backupLayout, backupSubLayout = None, None, None

# >


loginLayout = html.Div(id = 'divLoginLayoutId',
                       children = [

                           # Submit Modal <
                           dbc.Modal(fade = True,
                                     is_open = False,
                                     centered = True,
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
                           dbc.Modal(is_open = False,
                                     centered = True,
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
                           dbc.Modal(is_open = False,
                                     centered = True,
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

                                                                             # >

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

                                                                             # >

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


@application.callback(Output('submitModalId', 'is_open'),
                      Output('submitBadgeId', 'children'),
                      Output('usernameInputId', 'disabled'),
                      Input('submitBadgeId', 'n_clicks'),
                      Input('passwordInputId', 'n_submit'),
                      State('passwordInputId', 'value'),
                      State('divLoginLayoutId', 'children'),
                      State('divDivLoginLayoutId', 'children'))
def submitFunction(click: int, submit: int, password: str, layout: list, subLayout: list):
    '''  '''

    global backupLayout
    global backupSubLayout

    # if (submit) <
    if (click or submit):

        # if (valid) else (invalid) <
        if (Submit(password)): return (False, dbc.Spinner(size = 'sm'), True)
        else: return (True, 'Submit', False)

        # >

    # >

    backupLayout = layout
    backupSubLayout = subLayout
    return (False, 'Submit', False)


@application.callback(Output('verifyModalId', 'is_open'),
                      Output('passwordInputId', 'disabled'),
                      Output('divLoginLayoutId', 'children'),
                      Output('authenticateModalId', 'is_open'),
                      Input('usernameInputId', 'disabled'),
                      State('usernameInputId', 'value'),
                      State('passwordInputId', 'value'),
                      State('divLoginLayoutId', 'children'))
def verifyFunction(disabled: bool, username: str, password: str, layout: list):
    '''  '''

    global driver

    # if (locked) <
    if (disabled):

        driver = Verify(username, password)

        # if (verify) <
        if (driver):

            print('here')

            cond = True # *insert method to check is username exists in database *

            # if (new) else (existing) <
            if (cond): return (False, True, layout, True)
            else: return (False, False, homeLayout, False)

            # >

        # >

        else: return (True, False, layout, False)

    # >

    else: return (False, False, layout, False)


#@application.callback()
