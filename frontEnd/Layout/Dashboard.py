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
        dbc.Col(style = style['leftColStyle'],
                children = [

                    #

                    # Calendar <
                    dbc.Row(style = style['calendarStyle'],
                            children = [

                                html.H1('calendar')

                            ]),

                    # >

                    # UMKC Roo News <
                    dbc.Row(style = style['umkcRooNewsStyle'],
                            children = [

                                html.H1('roo news')

                            ])

                    # >

                ]),

        # >

        # Center <
        dbc.Col(style = style['centerColStyle'],
                children = [

                    # Agenda <
                    dbc.Row(style = style['agendaStyle'],
                            children = [

                                html.H1('agenda')

                            ])

                    # >

                ]),

        # >

        # Right <
        dbc.Col(style = style['rightColStyle'],
                children = [

                    # Event Create <
                    dbc.Row(style = style['eventCreateStyle'],
                            children = [

                                html.H1('create')

                            ]),

                    # >

                    # Event Update <
                    dbc.Row(style = style['eventUpdateStyle'],
                            children = [

                                html.H1('update')

                            ]),

                    # >

                    # Event Cancel <
                    dbc.Row(style = style['eventCancelStyle'],
                            children = [

                                html.H1('cancel')

                            ])

                    # >

                ])

        # >

    ])
