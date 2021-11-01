from dash import dcc
from dash import html
from backEnd.Tool import getJSON


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

                                                                  dcc.Input(type = 'text',
                                                                            id = 'inputUsernameId',
                                                                            placeholder = 'Username')

                                                              ], style = style['divUsernameStyle']),

                                                     # >

                                                     # Password <
                                                     html.Div(id = 'divPasswordId',
                                                              children = [

                                                                  dcc.Input(type = 'password',
                                                                            id = 'inputPasswordId',
                                                                            placeholder = 'Password')

                                                              ], style = style['divPasswordStyle']),

                                                     # >

                                                     # Submit <
                                                     html.Div(id = 'divSubmitId',
                                                              children = [

                                                                  ###

                                                              ], style = style['divSubmitStyle'])

                                                     # >

                                                 ], style = style['divInputStyle'])

                                        # >

                                    ], style = style['divBackgroundStyle']),

                           # >

                           # Markdown <
                           html.Div(id = 'divMarkdownId',
                                    children = [

                                        dcc.Markdown(id = 'markdownId',
                                                     children = [

                                                         '{}'.format(''.join(i for i in style['markdownChildren']))

                                                     ], style = style['markdownStyle'])

                                    ], style = style['divMarkdownStyle'])

                           # >

                       ], style = style['layoutStyle'])
