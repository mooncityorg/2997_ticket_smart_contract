from dash import dcc
from dash import html
from backEnd.Tool import getJSON


style = getJSON(file = '/frontEnd/Resource/Login.json')
loginLayout = html.Div(id = 'divId',
                       children = [

                           html.Div(id = 'divDivId',
                                    children = [

                                        html.Div(id = 'divDivDivId',
                                                 children = [



                                                 ], style = style['divDivDivStyle'])

                                    ], style = style['divDivStyle'])

                       ], style = style['divStyle'])


#
