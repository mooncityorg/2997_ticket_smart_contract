# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application

# >


# Declaration <
style = getJSON(file = '/frontEnd/Resource/Home.json')

# >


def homeLayout(username):
    '''  '''

    return dbc.Container(fluid = True,
                         children = [

                             # Header <
                             dbc.Row(children = [

                                 dbc.Col(width = True,
                                         children = [

                                             # Background <
                                             html.Div(id = 'backgroundDivId',
                                                      style = style['headerBackgroundDivStyle'],
                                                      children = [

                                                          dbc.Row(justify = 'center',
                                                                  style = style['backgroundRowStyle'],
                                                                  children = [

                                                                      dbc.Col(width = 'auto',
                                                                              id = 'backgroundRowColId',
                                                                              children = [

                                                                                  # Navigation Bar <
                                                                                  dbc.InputGroup(children = [

                                                                                      # Username <
                                                                                      dbc.Button(n_clicks = 0,
                                                                                                 children = username,
                                                                                                 id = 'usernameButtonId',
                                                                                                 style = style['usernameButtonStyle']),

                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Calendar <
                                                                                      dbc.Button(n_clicks = 0,
                                                                                                 children = 'Calendar',
                                                                                                 id = 'calendarButtonId',
                                                                                                 style = style['calendarButtonStyle']),

                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Dashboard <
                                                                                      dbc.Button(n_clicks = 0,
                                                                                                 children = 'Dashboard',
                                                                                                 id = 'dashboardButtonId',
                                                                                                 style = style['dashboardButtonStyle']),
                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Event <
                                                                                      dcc.Dropdown(searchable = False,
                                                                                                   placeholder = 'Event',
                                                                                                   id = 'eventDropdownId',
                                                                                                   style = style['eventDropdownStyle'],
                                                                                                   options = [

                                                                                                       {'label' : l, 'value' : v}

                                                                                                   for l, v in style['eventDropdownOptions'].items()]),

                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Search <
                                                                                      dcc.Dropdown(placeholder = 'Search',
                                                                                                   id = 'searchDropdownId',
                                                                                                   style = style['searchDropdownStyle'],
                                                                                                   options = [{'label' : 'temp', 'value' : 'ok'}]),

                                                                                      # >

                                                                                      # Role <
                                                                                      dcc.Dropdown(searchable = False,
                                                                                                   placeholder = 'Role',
                                                                                                   id = 'roleDropdownId',
                                                                                                   style = style['roleDropdownStyle'],
                                                                                                   options = [

                                                                                                       {'label' : l, 'value' : v}

                                                                                                   for l, v in style['roleDropdownOptions'].items()])

                                                                                      # >

                                                                                  ])

                                                                                  # >
                                                                              ])

                                                                  ])

                                                      ])

                                             # >

                                         ])

                             ]),

                             # >

                             # Body <
                             dbc.Row(children = [

                                 dbc.Col(children = [

                                     html.Div(children = None,
                                              id = 'bodyDivId',
                                              style = style['bodyDivStyle'])

                                 ])

                             ])

                             # >

                         ])


@application.callback(output = [Output('usernameButtonId', 'style'),
                                Output('calendarButtonId', 'style'),
                                Output('dashboardButtonId', 'style'),
                                Output('eventDropdownId', 'style'),
                                Output('searchDropdownId', 'style'),
                                Output('roleDropdownId', 'style'),

                                Output('roleDropdownId', 'value'),
                                Output('eventDropdownId', 'value'),
                                Output('searchDropdownId', 'value'),
                                Output('usernameButtonId', 'n_clicks'),
                                Output('calendarButtonId', 'n_clicks'),
                                Output('dashboardButtonId', 'n_clicks'),

                                Output('bodyDivId', 'children')],

                      inputs = [Input('usernameButtonId', 'n_clicks'),
                                Input('calendarButtonId', 'n_clicks'),
                                Input('dashboardButtonId', 'n_clicks'),
                                Input('eventDropdownId', 'value'),
                                Input('searchDropdownId', 'value'),
                                Input('roleDropdownId', 'value')],

                      state = [State('usernameButtonId', 'style'),
                               State('calendarButtonId', 'style'),
                               State('dashboardButtonId', 'style'),
                               State('eventDropdownId', 'style'),
                               State('searchDropdownId', 'style'),
                               State('roleDropdownId', 'style')])
def headerCallback(*args):
    '''  '''

    return [{}, {}, {}, {}, {}, {}, None, None, None, 0, 0, 0, None]
