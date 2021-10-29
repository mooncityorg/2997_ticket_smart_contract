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

                                                     #dcc.Input(id = 'inputId')
                                                     # we need to adjust size, color, etc...
                                                     # the position is correct, marginTop needs
                                                     # to be adjusted.
                                                     # id values for both input should be renamed to
                                                     # username, password respectively.
                                                     # a login button should be added that appears to be
                                                     # similar appearance to input boxes

                                                     # this is where login button goes

                                                 ], style = style['divDivDivStyleB'])

                                        # >

                                    ], style = style['divDivStyle'])

                                # this is where markdown-like text goes with redirects to the
                                # corresponding pages. merge with bottom of gold border to appear
                                # as extension to the background's border.

                           # >

                       ], style = style['divStyle'])

# this is where callback goes
# we grab states of username and password
# input is button id # output is uncertain
# back end is called here
