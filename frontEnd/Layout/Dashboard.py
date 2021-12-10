# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc


# >


# Declaration <


# >


def dashboardLayout(userId):
    '''  '''

    return dbc.Row(children = [

        dbc.Col(children = [

            dbc.Row(html.H1('1'), style = {'backgroundColor' : '#0066cc'}),
            dbc.Row(html.H1('2'), style = {'backgroundColor' : '#0066cc'}),
            dbc.Row(html.H1('3'), style = {'backgroundColor' : '#0066cc'})

        ]),

        dbc.Col(children = [

            dbc.Row(html.H1('4'), style = {'backgroundColor' : '#0066cc',
                                            'height' : '40vh'})

        ]),

        dbc.Col(children = [

            dbc.Row(html.H1('5'), style = {'backgroundColor' : '#0066cc',
                                            'height' : '30vh'}),
            dbc.Row(html.H1('6'), style = {'backgroundColor' : '#0066cc'})

        ])

    ])
