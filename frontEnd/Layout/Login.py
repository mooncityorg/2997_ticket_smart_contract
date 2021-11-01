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

                                                              ]),

                                                     # >

                                                     # Password <
                                                     html.Div(id = 'divPasswordId',
                                                              children = [

                                                                  dcc.Input(value = '',
                                                                            debounce = True,
                                                                            type = 'password',
                                                                            id = 'inputPasswordId',
                                                                            placeholder = 'Password',
                                                                            style = style['passwordStyle'])

                                                              ]),

                                                     # >

                                                     # Submit <
                                                     html.Div(id = 'divSubmitId',
                                                              children = [

                                                                  html.Button(type = 'submit',
                                                                              n_clicks = 0,
                                                                              children = 'Submit',
                                                                              id = 'buttonSubmitId',
                                                                              style = style['submitStyle'])

                                                              ]),

                                                     # >

                                                     # Forgot Password <
                                                     html.Div(id = 'divForgotPasswordId',
                                                              children = [

                                                                  dcc.Markdown(id = 'forgotPasswordId',
                                                                               children = [

                                                                                   style['forgotPasswordChildren']

                                                                               ])

                                                              ])


                                                     # >

                                                 ], style = style['divInputStyle'])

                                        # >

                                    ], style = style['divBackgroundStyle']),

                           # >

                           # Redirect <
                           html.Div(id = 'divRedirectId',
                                    children = [

                                        dcc.Markdown(id = 'redirectId',
                                                     children = [

                                                         '{}'.format(''.join(i for i in style['redirectChildren']))

                                                     ], style = style['redirectStyle'])

                                    ], style = style['divRedirectStyle'])

                           # >

                       ], style = style['layoutStyle'])


@application.callback(Output('layoutId', 'children'),
                      Input('buttonSubmitId', 'n_clicks'),
                      State('layoutId', 'children'),
                      State('inputUsernameId', 'value'),
                      State('inputPasswordId', 'value'))
def submitFunction(click: int, layout: list, username: str, password: str):
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
