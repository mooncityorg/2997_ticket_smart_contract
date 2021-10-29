from dash import dcc
from dash import html
from backEnd.Tool import getJSON


style = getJSON(file = '/frontEnd/Resource/Login.json')
loginLayout = html.Div(id = 'divId',
                       children = [

                           # Background <
                           html.Div(id = 'divDivId',
                                    children = [

                                        # UMKC Logo <
                                        html.Div(id = 'divDivDivIdA',
                                                 children = [

                                                     html.Img(src = style['divDivDivImgSrc'],
                                                              style = style['divDivDivImgStyle'])

                                                 ], style = style['divDivDivStyleA']),

                                        # >

                                        # Input <
                                        html.Div(id = 'divDivDivIdB',
                                                 children = [



                                                 ], style = style['divDivDivStyleB'])

                                        # >

                                    ], style = style['divDivStyle'])

                           # >

                       ], style = style['divStyle'])
