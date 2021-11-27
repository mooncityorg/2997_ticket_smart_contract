# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application

# >


# Declaration <
# note: we get a user's data in here
# and not in Login.py. in Login.py we
# set the data for a user.
style = getJSON(file = '/frontEnd/Resource/Home.json')

# >


homeLayout = dbc.Container([

    # Header <
    dbc.Row([dbc.Col(

        # Background <
        html.Div(id = 'divHeaderBackgroundId',
                 children = [

                     dbc.Row([dbc.Col(

                         # Navigation Bar <
                         dbc.InputGroup([

                             # Username <
                             dbc.Button(id = 'usernameId',
                                        children = 'ala2q6',
                                        style = style['usernameStyle']),

                             # >

                             # Spacer <
                             dbc.InputGroupText(style = style['spacerStyle']),

                             # >

                             # Calendar <
                             dbc.Button(id = 'calendarId',
                                        children = 'Calendar',
                                        style = style['calendarStyle']),

                             # >

                             # Spacer <
                             dbc.InputGroupText(style = style['spacerStyle']),

                             # >

                             # Dashboard <
                             dbc.Button(id = 'dashboardId',
                                        children = 'Dashboard',
                                        style = style['dashboardStyle']),

                             # >

                             # Spacer <
                             dbc.InputGroupText(style = style['spacerStyle']),

                             # >

                             # Event <
                             dcc.Dropdown(id = 'eventId',
                                          searchable = False,
                                          placeholder = 'Event',
                                          style = style['eventStyle'],
                                          options = [

                                              {'label' : l, 'value' : v}

                                          for l, v in style['eventOptions'].items()]),

                             # >

                             # Spacer <
                             dbc.InputGroupText(style = style['spacerStyle']),

                             # >

                             # Search <
                             dcc.Dropdown(id = 'searchId',
                                          placeholder = 'Search',
                                          style = style['searchStyle']),
                                          #options = [

                                              #{'label' : name, 'value' : userId}

                                          #for name, userId in ])
                                          # requirement: a method that returns all
                                          # names and userIds

                             # >

                             # Spacer <
                             dbc.InputGroupText(style = style['spacerStyle']),

                              #>

                             # Role <
                             dcc.Dropdown(id = 'roleId',
                                          searchable = False,
                                          placeholder = 'Role',
                                          style = style['roleStyle'],
                                          options = [

                                              {'label' : l, 'value' : v}

                                          for l, v in style['roleOptions'].items()]),

                             # >

                         ]),

                         # >

                     width = 'auto')], justify = 'center', style = style['headerRowStyle'])

                 ], style = style['divHeaderBackgroundStyle']),

        # >

        width = True)

    ]),

    # >

    # Main <
    dbc.Row([dbc.Col(

        html.Div(id = 'divMainId',
                 children = [

                     dbc.Row([

                         dbc.Col(

                             #

                         )

                     ])

                 ], style = style['divMainBackgroundStyle'])

    )])

    # >

], fluid = True)
