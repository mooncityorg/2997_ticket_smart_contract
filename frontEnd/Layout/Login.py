# Import <
from dash import dcc, html
from selenium import webdriver
from dash.dependencies import Input, Output, State
from frontEnd.Layout.Dashboard import dashboardLayout
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from backEnd.API.Utility import getJSON, application, Login, Verify

# >


# Declaration <
options = Options()
options.headless = True
style = getJSON(file = '/frontEnd/Resource/Login.json')
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

# >


loginLayout = html.Div(id = 'loginLayoutId',
                       children = [

                           # Login Confirm Dialog <
                           dcc.ConfirmDialog(id = 'loginConfirmDialogId',
                                             message = 'Login information was invalid.'),

                           # >

                           # Verify Confirm Dialog <
                           dcc.ConfirmDialog(id = 'verifyConfirmDialog',
                                             message = 'Verify information was invalid.'),

                           # >

                           # Login <
                           html.Div(id = 'divLoginId',
                                    children = [

                                        # Image <
                                        html.Div(id = 'divImageId',
                                                 children = [

                                                     html.Img(src = style['imgSrc'],
                                                              style = style['imgStyle'])

                                                 ], style = style['divImageStyle']),

                                        # >

                                        # Input <
                                        html.Div(id = 'divInputId',
                                                 children = [

                                                     # Username <
                                                     html.Div(id = 'divUsernameId',
                                                              children = [

                                                                  dcc.Input(value = '',
                                                                            id = 'inputUsernameId',
                                                                            placeholder = 'Username',
                                                                            style = style['usernameStyle'])

                                                              ], style = style['divUsernameStyle']),

                                                     # >

                                                     # Password <
                                                     html.Div(id = 'divPasswordId',
                                                              children = [

                                                                  dcc.Input(value = '',
                                                                            n_submit = 0,
                                                                            debounce = True,
                                                                            type = 'password',
                                                                            id = 'inputPasswordId',
                                                                            placeholder = 'Password',
                                                                            style = style['passwordStyle'])

                                                              ], style = style['divPasswordStyle']),

                                                     # >

                                                     # Submit <
                                                     html.Div(id = 'divSubmitId',
                                                              children = [

                                                                  html.Button(n_clicks = 0,
                                                                              children = 'Submit',
                                                                              id = 'buttonSubmitId',
                                                                              style = style['submitStyle'])

                                                              ], style = style['divSubmitStyle']),

                                                     # >

                                                 ], style = style['divInputStyle']),

                                        # >

                                        # Redirect <
                                        dcc.Markdown(id = 'markdownRedirectId',
                                                     children = [

                                                         ('### ' + ''.join(i for i in style['redirectChildren']))

                                                     ], style = style['markdownRedirectStyle'])

                                        # >

                                    ], style = style['divLoginStyle'])

                           # >

                       ], style = style['loginLayoutStyle'])


@application.callback(Output('divPasswordId', 'children'),
                      Output('buttonSubmitId', 'n_clicks'),
                      Output('inputUsernameId', 'disabled'),
                      Output('loginConfirmDialogId', 'displayed'),
                      Input('buttonSubmitId', 'n_clicks'),
                      Input('inputPasswordId', 'n_submit'),
                      State('inputUsernameId', 'value'),
                      State('inputPasswordId', 'value'),
                      State('divPasswordId', 'children'))
def loginFunction(click: int, submit: int, username: str, password: str, div: list):
    '''  '''

    # if (login) <
    if (click or submit):

        # global driver # < UNCOMMENT AFTER NOVEMBER 20th < #
        # condition = Login(driver, username, password) # < UNCOMMENT AFTER NOVEMBER 20th < #
        # driver = condition if (condition) else (driver) # < UNCOMMENT AFTER NOVEMBER 20th < #
        condition = True # < REMOVE AFTER NOVEMBER 20th < #

        if (condition):

            # if (existing user): call custom dashboard
            # else (new user): push to verify

            return ((html.Div(id = 'divCodeId',
                             children = [

                                 dcc.Input(value = '',
                                           n_submit = 0,
                                           debounce = True,
                                           type = 'password',
                                           id = 'inputCodeId',
                                           placeholder = '6-Digit Code',
                                           style = style['passwordStyle'])

                             ], style = style['divPasswordStyle'])

                    ), 0, True, False)

        # >

        # else (not passed) <
        else: return (div, False, True)

        # >

    # >

    else: return (div, False, False)


@application.callback(Output('loginLayoutId', 'children'),
                      Output('verifyConfirmDialog', 'displayed'),
                      Input('inputCodeId', 'n_submit'),
                      Input('buttonSubmitId', 'n_clicks'),
                      State('inputCodeId', 'value'),
                      State('loginLayoutId', 'children'))
def verifyFunction(submit: int, click: int, code: str, div: list):
    '''  '''

    # if (verify) <
    if (submit or click):

        # condition = Verify(driver, code) # < UNCOMMENT AFTER NOVEMBER 20th < #
        condition = True # < REMOVE AFTER NOVEMBER 20th < #

        # if (passed) <
        if (condition):

            # set data
            # username dashboard element
            dashboard = dashboardLayout
            return (dashboardLayout, False)

        # >

        # else (not passed) <
        else: return (div, True)

        # >

    # >

    else:

        # Send Code <
        # Verify(driver, code) # < UNCOMMENT AFTER NOVEMBER 20th < #
        return (div, False)

        # >
