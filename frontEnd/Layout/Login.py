# Import <
from dash import dcc, html
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application
from backEnd.API.Utility import Submit, Verify, Authenticate

# >


# Declaration <
driver, backupLayout = None, None
style = getJSON(file = '/frontEnd/Resource/Login.json')

# >


def loginLayout():
    '''  '''

    return html.Div(id = 'loginLayoutDivId',
                    children = [

                        # Submit Modal <
                        dbc.Modal(is_open = False,
                                  centered = True,
                                  id = 'submitModalId',
                                  children = [

                                      dbc.ModalBody(style = style['modalStyle'],
                                                    children = [

                                                        html.H4(style = style['submitH4Style'],
                                                                children = 'There was an error.'),

                                                        dbc.FormText(style = style['submitFormTextStyle'],
                                                                     children = 'The information you input was invalid.')

                                                    ])

                                  ]),

                        # >

                        # Verify Modal <
                        dbc.Modal(is_open = False,
                                  centered = True,
                                  id = 'verifyModalId',
                                  children = [

                                      dbc.ModalBody(style = style['modalStyle'],
                                                    children = [

                                                        html.H4(style = style['verifyH4Style'],
                                                                children = 'There was an error.'),

                                                        dbc.FormText(style = style['verifyFormTextStyle'],
                                                                    children = 'The information you input was invalid.')

                                                    ])

                                  ]),

                        # >

                        # Authenticate Modal <
                        dbc.Modal(is_open = False,
                                  centered = True,
                                  id = 'authenticateModalId',
                                  children = [

                                      dbc.ModalBody(style = style['modalStyle'],
                                                    children = [

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
                                                                html.Hr(style = style['textBodyStyle']),

                                                                html.H6(style = style['bodyH6Style'],
                                                                        children = 'We use the code you received to log into '
                                                                                   'your UMKC Pathway account in order to get '
                                                                                   'your name and current class schedule.'),

                                                                html.H6(style = style['bodyH6Style'],
                                                                        children = 'This can take up to twenty seconds.'),

                                                                html.Hr(style = style['textBodyStyle']),

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
                                                                                          id = 'authenticateInputId',
                                                                                          style = style['authenticateInputStyle'])

                                                                            ]),

                                                                    dbc.Col(width = 'auto',
                                                                            children = [

                                                                                dbc.Button(n_clicks = 0,
                                                                                           children = 'Authenticate',
                                                                                           id = 'authenticateButtonId',
                                                                                           style = style['authenticateButtonStyle'])

                                                                            ])

                                                                    # >

                                                                ])

                                                        # >

                                                    ])

                                  ]),

                        # >

                        html.Div(id = 'loginLayoutDivDivId',
                                 style = style['loginLayoutDivDivStyle'],
                                 children = [

                                     # Logo <
                                     dbc.Row(justify = 'center',
                                             children = [

                                                 dbc.Col(width = 4,
                                                         children = [

                                                             html.Div(id = 'logoDivId',
                                                                      style = style['logoDivStyle'],
                                                                      children = [

                                                                          html.Img(src = style['logoImgSrc'],
                                                                                   style = style['logoImgStyle'])

                                                                      ])

                                                         ])

                                             ]),

                                     # >

                                     # Input <
                                     dbc.Row(justify = 'center',
                                             children = [

                                                 dbc.Col(width = 10,
                                                         children = [

                                                             html.Div(id = 'inputDivId',
                                                                      style = style['inputDivStyle'],
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

                                                                      ])

                                                         ])

                                             ]),

                                     # >

                                     # Redirect <
                                     dbc.Row(justify = 'center',
                                             children = [

                                                 dbc.Col(width = 10,
                                                         children = [

                                                             html.Div(id = 'redirectDivId',
                                                                      style = style['redirectDivStyle'],
                                                                      children = [

                                                                          dbc.Badge(children = '3ASJW6',
                                                                                    href = style['redirectBadgeHref'],
                                                                                    color = style['redirectBadgeColor'],
                                                                                    style = style['redirectBadgeStyle'])

                                                                      ])

                                                         ])

                                             ])

                                     # >

                                 ])

                    ])


@application.callback(Output('submitModalId', 'is_open'),
                      Output('submitBadgeId', 'children'),
                      Output('usernameInputId', 'disabled'),
                      Input('submitBadgeId', 'n_clicks'),
                      Input('passwordInputId', 'n_submit'),
                      State('passwordInputId', 'value'),
                      State('loginLayoutDivId', 'children'))
def submitFunction(click: int, submit: int, password: str, layout: list):
    '''  '''

    global backupLayout

    # if (submit) <
    if (click or submit):

        # if (valid) else (invalid) <
        if (Submit(password)): return (False, dbc.Spinner(size = 'sm'), True)
        else: return (True, 'Submit', False)

        # >

    # >

    backupLayout = layout
    return (False, 'Submit', False)


@application.callback(Output('verifyModalId', 'is_open'),
                      Output('passwordInputId', 'disabled'),
                      Output('loginLayoutDivId', 'children'),
                      Input('usernameInputId', 'disabled'),
                      State('usernameInputId', 'value'),
                      State('passwordInputId', 'value'),
                      State('loginLayoutDivId', 'children'))
def verifyFunction(disabled: bool, username: str, password: str, layout: list):
    '''  '''

    global driver

    # if (locked) <
    if (disabled):

        driver = Verify(username, password)

        # if (verify) <
        if (driver):

            # if (new) <
            if (1 in [1]): # * method to check if new *

                layout[2]['props']['is_open'] = True
                driver = Authenticate(driver)
                return (False, True, layout)

            # >

            # else (existing) <
            else:

                layout = homeLayout(username)
                return (False, False, layout)

            # >

        # >

        else: return (True, False, layout)

    # >

    else: return (False, False, layout)
