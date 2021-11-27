# Import <
from dash import dcc, html
#from selenium import webdriver
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from backEnd.API.Utility import getJSON, application, Submit

# >


# Declaration <
#options = Options()
#options.headless = True
style = getJSON(file = '/frontEnd/Resource/Login.json')
#driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

# >


loginLayout = html.Div(id = 'loginLayoutId',
                       children = [

                           # Submit Confirm Dialog <
                           dcc.ConfirmDialog(id = 'submitConfirmDialog',
                                             message = 'Error: Invalid Credentials.'),

                           # >

                           # Verify Confirm Dialog <
                           dcc.ConfirmDialog(id = 'verifyConfirmDialog',
                                             message = 'Error: Invalid Credentials.'),

                           # >

                           # Logo <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divLogoId',
                                        children = [

                                            html.Img(src = style['logoSrc'],
                                                     style = style['logoStyle']),

                                        ], style = style['divLogoStyle']),

                           width = 4)], justify = 'center'),

                           # >

                           # Input <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divInputId',
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
                                            dbc.Row([dbc.Col(

                                                dbc.FormFloating([

                                                    dbc.Input(disabled = False,
                                                              id = 'inputUsernameId',
                                                              placeholder = 'Username',
                                                              style = style['usernameStyle']),
                                                    dbc.Label('Username')

                                                ]),

                                            width = 3)], justify = 'center'),

                                            # >

                                            # Password <
                                            dbc.Row([dbc.Col(

                                                dbc.FormFloating([

                                                    dbc.Input(n_submit = 0,
                                                              disabled = True,
                                                              debounce = True,
                                                              type = 'password',
                                                              id = 'inputPasswordId',
                                                              placeholder = 'Password',
                                                              style = style['passwordStyle']),
                                                    dbc.Label('Password')

                                                ]),

                                            width = 3)], justify = 'center'),

                                            # >

                                            # Forgot Password <
                                            dbc.Row([dbc.Col(

                                                dbc.Badge(children = 'Forgot Password?',
                                                          href = style['forgotPasswordHref'],
                                                          color = style['forgotPasswordColor'],
                                                          style = style['forgotPasswordStyle']),

                                            width = 'auto')], justify = 'center'),

                                            # >

                                            # Submit <
                                            dbc.Row([dbc.Col(

                                                dbc.Badge(href = '#',
                                                          n_clicks = 0,
                                                          id = 'submitId',
                                                          children = 'Submit',
                                                          color = style['submitColor'],
                                                          style = style['submitStyle']),

                                            width = 'auto')], justify = 'center')

                                            # >

                                        ], style = style['divInputStyle']),

                           width = 10)], justify = 'center'),

                           # >

                           # Redirect <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divRedirectId',
                                        children = [

                                            dbc.Badge(children = '3ASJW6',
                                                      href = style['redirectHref'],
                                                      color = style['redirectColor'],
                                                      style = style['redirectStyle'])

                                        ], style = style['divRedirectStyle']),

                           width = 10)], justify = 'center')

                           # >

                       ], style = style['loginLayoutStyle'])


@application.callback(Output('submitId', 'children'),
                      Output('inputUsernameId', 'disabled'),
                      Output('inputPasswordId', 'disabled'),
                      Output('submitConfirmDialog', 'displayed'),
                      Input('submitId', 'n_clicks'),
                      Input('inputPasswordId', 'n_submit'),
                      State('inputPasswordId', 'value'))
def submitFunction(click: int, submit: int, password: str):
    '''  '''

    # if (submit) <
    if (click or submit):

        # if (valid) <
        if (Submit(password)):

            return (dbc.Spinner(size = 'sm'), True, True, False)

        # >

        return ('Submit', False, False, True)

    # >

    return ('Submit', False, False, False)


@application.callback(Output('verifyConfirmDialog', 'displayed'),
                      Input('inputUsernameId', 'disabled'),
                      State('inputUsernameId', 'value'),
                      State('inputPasswordId', 'value'))
def verifyFunction(disabled: bool, username: str, password: str):
    '''  '''

    # if (verify) <
    if (disabled):

        print('disabled', disabled)
        return False

    # >

    return False
