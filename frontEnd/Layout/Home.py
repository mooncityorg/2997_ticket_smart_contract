# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from frontEnd.Layout.Search import searchLayout
from dash.dependencies import Input, Output, State
from frontEnd.Layout.Calendar import calendarLayout
from backEnd.API.Utility import getJSON, application
from frontEnd.Layout.Dashboard import dashboardLayout
from frontEnd.Layout.Preference import preferenceLayout
from frontEnd.Layout.Event import eventCancelLayout, eventViewLayout
from frontEnd.Layout.Event import eventCreateLayout, eventUpdateLayout

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

                                                                                      # Preference <
                                                                                      dbc.Button(n_clicks = 0,
                                                                                                 children = username,
                                                                                                 id = 'preferenceButtonId',
                                                                                                 style = style['preferenceButtonStyle']),

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


@application.callback(Output('bodyDivId', 'children'),
                      Output('roleDropdownId', 'value'),
                      Output('eventDropdownId', 'value'),
                      Output('searchDropdownId', 'value'),
                      Output('calendarButtonId', 'n_clicks'),
                      Output('dashboardButtonId', 'n_clicks'),
                      Output('preferenceButtonId', 'n_clicks'),

                      Input('eventDropdownId', 'value'),
                      Input('searchDropdownId', 'value'),
                      Input('preferenceButtonId', 'value'),
                      Input('calendarButtonId', 'n_clicks'),
                      Input('dashboardButtonId', 'n_clicks'),
                      Input('preferenceButtonId', 'n_clicks'),

                      State('roleDropdownId', 'value'))
def headerCallback(eventValue, searchValue, userId, calendarClick, dashboardClick, preferenceClick,
                   roleValue):
    '''  '''

    # if (header) <
    if (eventValue or searchValue or calendarClick or dashboardClick or preferenceClick):

        # Declaration <
        name = searchValue if (searchValue) else None
        inputs = [eventValue] if (eventValue) else []
        keys = ('searchId', 'calendarId', 'dashboardId', 'preferenceId')

        # >

        for c, i in enumerate([searchValue, calendarClick, dashboardClick, preferenceClick]):

            if (i not in [0, None]): inputs.append(keys[c])

        print(inputs)

        callbacks = {

            'createId' : eventCreateLayout(userId),
            'cancelId' : eventCancelLayout(userId),
            'updateId' : eventUpdateLayout(userId),
            'viewId' : eventViewLayout(userId),
            'preferenceId' : preferenceLayout(userId),
            'dashboardId' : dashboardLayout(userId),
            'calendarId' : calendarLayout(userId),
            'searchId' : searchLayout(userId, name, roleValue)

        }[inputs[0]]

        return (callbacks, None, None, None, 0, 0, 0)

    # >

    # else (default) <
    else: return (dashboardLayout(userId), None, None, None, 0, 0, 0)

    # >
