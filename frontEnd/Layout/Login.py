# Import <
from dash import dcc, html
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application
from backEnd.API.Utility import scrapeUser, scrapeCourse
from backEnd.API.Utility import Verify, Login, Authenticate

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

                                    dbc.Col(width = 'auto',
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
                                                                                                   disabled = False,
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
                                                                                 id = 'submitColId',
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
                      Input('submitBadgeId', 'n_clicks'),
                      Input('passwordInputId', 'n_submit'),
                      State('passwordInputId', 'value'))
def verifyCallback(click: int, submit: int,
                   passwordInput: str):
    '''  '''

    # Declaration <
    isValid = Verify(passwordInput)

    # >

    # if ((verify) and (valid)) else (default) <
    if ((click or submit) and (isValid)): return (dbc.Spinner(size = 'sm'), True)
    else: return ('Submit', False)

    # >


@application.callback(Output('submitColId', 'children'),
                      Output('passwordInputId', 'disabled'),
                      Output('forgotPasswordColId', 'width'),
                      Output('forgotPasswordColId', 'children'),
                      Input('usernameInputId', 'disabled'),
                      State('submitColId', 'children'),
                      State('usernameInputId', 'value'),
                      State('passwordInputId', 'value'),
                      State('forgotPasswordColId', 'children'))
def loginCallback(usernameDisabled: bool,
                  submitChildren: list, usernameInput: str, passwordInput: str, forgotPasswordChildren: list):
    '''  '''

    global driver

    # if (login) <
    if (usernameDisabled):

        # Declaration <
        isUser = 1 in [11] # * method *
        isDisabled = True if (isUser) else False
        driver = Login(usernameInput, passwordInput)
        if ((driver) and (not isUser)): driver = Authenticate(driver)

        # >

        return (

            dbc.Badge(href = '#',
                      n_clicks = 0,
                      children = 'Authenticate',
                      id = 'authenticateBadgeId',
                      color = style['submitBadgeColor'],
                      style = style['submitBadgeStyle']),

            True,
            3,

            dbc.FormFloating(children = [

                dbc.Input(n_submit = 0,
                          debounce = True,
                          id = 'codeInputId',
                          placeholder = 'Code',
                          disabled = isDisabled,
                          style = style['passwordInputStyle']),
                dbc.Label('Code')

            ])

        )

    # >

    # else (default) <
    else: return (submitChildren, False, 'auto', forgotPasswordChildren)

    # >


@application.callback(Output('loginLayoutDivId', 'children'),
                      Input('codeInputId', 'n_submit'),
                      Input('authenticateBadgeId', 'n_clicks'),
                      State('codeInputId', 'value'),
                      State('codeInputId', 'disabled'),
                      State('usernameInputId', 'value'),
                      State('loginLayoutDivId', 'children'))
def authenticateCallback(submit: int, click: int,
                         codeInput: str, codeDisabled: bool, usernameInput: str, children: list):
    '''  '''

    global driver

    # if (submit) <
    if (submit or click):

        driver = Authenticate(driver, code = codeInput)

        # if (passed) <
        if (driver):

            driver, user = scrapeUser(driver)
            driver, course = scrapeCourse(driver)
            return (homeLayout('JAD6TJ'))

        # >

        # else (not passed) <
        else: return loginLayout()

        # >

    # >

    # elif (not new) <
    elif (codeDisabled): return homeLayout(usernameInput)

    # >

    # else (default) <
    else: return children

    # >
