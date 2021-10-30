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



                                                 ], style = style['divInputStyle'])

                                        # >

                                    ], style = style['divBackgroundStyle']),

                           # >

                           # Markdown <
                           html.Div(id = 'divMarkdownId',
                                    children = [

                                        dcc.Markdown(id = 'markdownId',
                                                     style = style['markdownStyle'],
                                                     children = '### **{}**'.format(''.join(i for i in style['markdownChildren'])))

                                    ], style = style['divMarkdownStyle'])

                           # >

                       ], style = style['layoutStyle'])
