# Import <
from dash import dcc, html
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application
from backEnd.API.Utility import scrapeUser, scrapeCourse
from backEnd.API.Utility import Submit, Verify, Authenticate

# >


# Declaration <
driver = None
style = getJSON(file = '/frontEnd/Resource/Login.json')

# >


def loginLayout():
    '''  '''

    return html.Div(id = 'loginLayoutDivId',
                    style = style['loginLayoutDivStyle'],
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

                                                                                         dbc.Input(disabled = False,
                                                                                                   id = 'usernameInputId',
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
                                                                                 id = 'forgotPasswordColId',
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


@application.callback(Output('submitBadgeId', 'children'),
                      Output('usernameInputId', 'disabled'),
                      Output('passwordInputId', 'disabled'),
                      Output('forgotPasswordColId', 'children'),
                      Input('submitBadgeId', 'n_clicks'),
                      Input('usernameInputId', 'disabled'),
                      Input('passwordInputId', 'disabled'),
                      Input('passwordInputId', 'n_submit'),
                      State('usernameInputId', 'value'),
                      State('passwordInputId', 'value'),
                      State('forgotPasswordColId', 'children'))
def submitFunction(click: int, usernameDisabled: bool, passwordDisabled: bool, submit: int,
                   usernameInput: str, passwordInput: str, children: list):
    '''  '''

    global driver

    # if (Submit) <
    if (click or submit):

        if (passwordDisabled):

            pass

        elif (usernameDisabled):

            pass

        else:

            pass

    # >


@application.callback(Output('loginLayoutDivId', 'children'),
                      Input('codeInputId', 'n_submit'),
                      Input('codeInputId', 'disabled'),
                      Input('submitBadgeId', 'n_clicks'))
def codeFunction(submit: int, disabled: bool, click: int):
    '''  '''

    pass
