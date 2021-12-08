# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application

# >


# Declaration <
# * method to get user data *
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
                                                                              children = [

                                                                                  # Navigation Bar <
                                                                                  dbc.InputGroup(children = [

                                                                                      # Username <
                                                                                      dbc.Button(children = username,
                                                                                                 id = 'usernameButtonId',
                                                                                                 style = style['usernameButtonStyle']),

                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Calendar <
                                                                                      dbc.Button(children = 'Calendar',
                                                                                                 id = 'calendarButtonId',
                                                                                                 style = style['calendarButtonStyle']),

                                                                                      # >

                                                                                      # Spacer <
                                                                                      dbc.InputGroupText(style = style['spacerStyle']),

                                                                                      # >

                                                                                      # Dashboard <
                                                                                      dbc.Button(children = 'Dashboard',
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
                                                                                                   style = style['searchDropdownStyle']),
                                                                                                   # options =
                                                                                                      # a method that gets all (name, userId)

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


'''@application.callback(Output(),
                      Input(),
                      State())
def homeCallback():
    '''  '''

    pass
'''
