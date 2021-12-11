# Import <
from dash import html, dcc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application, Login, Verify
from backEnd.API.Event import Event
from backEnd.API.Member import Member
import dash_bootstrap_components as dbc

# >

# Declaration <
style = getJSON(file = '/frontEnd/Resource/Event.json')
eventObject = Event()
Member = Member()
info = eventObject.getEvent(123456)


def eventViewLayout(username):
    '''  '''
    userEvent = Member.getMember(username)
    info = eventObject.getEvent(userEvent['eventId'])
    return html.Div(
    [
        dbc.Button(info['Title'], id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(info['Title'], style = style['headerStyle'])),
                dbc.ModalBody(
                    [
                        html.Div(id = 'eventLayout',
                                 children = [
                                     dcc.Tabs(id="event-tabs", value='tab-1-example-graph', children=[
                                         dcc.Tab(label='DETAILS', value='details-tab'),
                                         dcc.Tab(label='PERSON INFO', value='person-info-tab'),
                                     ]),
                                     html.Div(id='tabs-content-example-graph')
                                 ])
                    ]
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)


def eventCreateLayout(userId):
    '''  '''

    return html.H1('create')


def eventUpdateLayout(username):
    '''  '''

    return html.H1('update')


def eventCancelLayout(username):
    '''  '''

    return html.H1('cancel')


@application.callback(
    Output("tabs-content-example-graph", "children"),
    Input('event-tabs', 'value'),
)
def render_content(tab):
    if tab == 'details-tab':
        return html.Div([
            html.Div("Course: " + info['Course']),
            html.Div("Description: " + info['Description']),
            html.Div("Times: " + str(info['startTime']) + ' - ' + str(info['endTime'])),
            html.Div("Date: " + str(info['Month']) + '/' + str(info['Day']) + '/' + str(info['Year']))
        ])
    elif tab == 'person-info-tab':
        return html.Div([
            html.H3('Tab content 2')

        ])


@application.callback(
    Output("modal", "is_open"),
    Input("open", "n_clicks"),
    Input("close", "n_clicks"),
    State("modal", "is_open")
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
