# Import <
from dash import dcc, html
from frontEnd.Layout.Verify import verifyLayout
from backEnd.Utility import getJSON, application
from dash.dependencies import Input, Output, State

# >


# Declaration <
style = getJSON(file = '/frontEnd/Resource/Login.json')

# >


loginLayout = html.Div(id = 'loginLayoutId',
                       children = [

                           # Confirm <
                           dcc.ConfirmDialog(id = 'loginConfirmId',
                                             message = 'The login you entered was incorrect.'),

                           # >

                           # Background <
                           html.Div(id = 'divBackgroundId',
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

                                                     # Login <
                                                     html.Div(id = 'divLoginId',
                                                              children = [

                                                                  html.Button(n_clicks = 0,
                                                                              children = 'Login',
                                                                              id = 'buttonLoginId',
                                                                              style = style['loginStyle'])

                                                              ], style = style['divLoginStyle']),

                                                     # >

                                                 ], style = style['divInputStyle']),

                                        # >

                                        # Redirect <
                                        dcc.Markdown(id = 'redirectId',
                                                     children = [

                                                         ('### ' + ''.join(i for i in style['redirectChildren']))

                                                     ], style = style['redirectStyle'])

                                        # >

                                    ], style = style['divBackgroundStyle']),

                           # >

                       ], style = style['layoutStyle'])


@application.callback(Output('loginLayoutId', 'children'),
                      Output('loginConfirmId', 'displayed'),
                      Input('buttonLoginId', 'n_clicks'),
                      Input('inputPasswordId', 'n_submit'),
                      State('inputUsernameId', 'value'),
                      State('inputPasswordId', 'value'),
                      State('loginLayoutId', 'children'))
def loginFunction(click: int, submit: int, username: str, password: str, layout: list):
    '''  '''

    # if (Login) <
    if (click or submit):

        return verifyLayout, False

    # >

    return layout, False

