from dash import dcc
from dash import html
from backEnd.Tool import getJSON, application
from dash.dependencies import Input, Output, State


style = getJSON(file = '/frontEnd/Resource/Login.json')
loginLayout = html.Div(id = 'layoutId',
                       children = [

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


@application.callback(Output('layoutId', 'children'),
                      Input('buttonLoginId', 'n_clicks'),
                      Input('inputPasswordId', 'n_submit'),
                      State('layoutId', 'children'),
                      State('inputUsernameId', 'value'),
                      State('inputPasswordId', 'value'))
def submitFunction(click: int, submit: int, layout: list, username: str, password: str):
    '''  '''

    # if (clicked) <
    if (click != 0):

        print()
        print('username: ', username)
        print('password: ', password)

        return layout

    # >

    else:

        return layout
