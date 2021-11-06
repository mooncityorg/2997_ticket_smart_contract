# Import <
from dash import dcc, html
from backEnd.Tool import getJSON, application

# >


# Import <
from dash.dependencies import Input, Output, State
from frontEnd.Layout.Authentication import authenticationLayout

# >


style = getJSON(file = '/frontEnd/Resource/Login.json')
loginLayout = html.Div(id = 'loginLayoutId',
                       children = [

                           # Warning <
                           dcc.ConfirmDialog(id = 'warningId',
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
                                                                            type = 'text',
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


'''authenticationLayout = html.Div(id = 'authenticationLayoutId',
                                children = [



                                ])


# note: we should output to replace the input div with an authentication box,
# and then the authentication box should output the replacement of the entire
# variable's children should it be successful. after authentication- we login
# and take the data for new users. profile picture, the classes they're in. etc.
@application.callback(Output('layoutId', 'children'), # should be transitioned to authentication
                      Output('loginWarningId', 'displayed'), # selenium login status, kept here
                      Input('buttonLoginId', 'n_clicks'), # if user clicks submission, keep here
                      Input('inputPasswordId', 'n_submit'), # if user hits enter to submit, keep here
                      State('layoutId', 'children'), # if fail, keep curernt state
                      State('inputUsernameId', 'value'), # get username
                      State('inputPasswordId', 'value')) # get password
def loginFunction(click: int, submit: int, layout: list, username: str, password: str):
    #output[1] : if (true), then new layout; if (false), then old layout
     #   output[2] : if (incorrect), then true; if (correct), then false

    # if (clicked) <
    if (click != 0):

        print()
        print('username: ', username)
        print('password: ', password)

        return layout, True

    # >

    else:

        return layout, False


# a second callback that replaces the contents of input box with a verification screen'''
