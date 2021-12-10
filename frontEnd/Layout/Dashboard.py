# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application


# >


# Declaration <
style = getJSON(file = '/frontEnd/Resource/Dashboard.json')

# >


def dashboardLayout(userId):
    '''  '''

    return dbc.Row(children = [

        # Left <
        dbc.Col(children = [

            # Calendar <
            dbc.Row(style = style['calendarStyle'],
                    children = [

                        #

                    ]),

            # >

            # UMKC Roo News <
            dbc.Row(style = style['umkcRooNewsStyle'],
                    children = [

                        #

                    ])

            # >

        ]),

        # >

        # Center <
        dbc.Col(children = [

            # Agenda <
            dbc.Row(style = style['agendaStyle'],
                    children = [

                        #

                    ])

            # >

        ]),

        # >

        # Right <
        dbc.Col(children = [

            # Event Create <
            dbc.Row(style = style['eventCreateStyle'],
                    children = [

                        #

                    ]),

            # >

            # Event Update <
            dbc.Row(style = style['eventUpdateStyle'],
                    children = [

                        #

                    ]),

            # >

            # Event Cancel <
            dbc.Row(style = style['eventCancelStyle'],
                    children = [

                        #

                    ])

            # >

        ])

        # >

    ])
