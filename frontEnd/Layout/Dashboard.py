# Import <
from time import strftime
from dash import html, dcc
from backEnd.API.Event import Event
import dash_bootstrap_components as dbc
from backEnd.API.Utility import scrapeUMKCRooNews
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application
from frontEnd.Layout.Event import eventViewLayout
# >


# Declaration <
articles = []
style = getJSON(file = '/frontEnd/Resource/Dashboard.json')

# >


def dashboardLayout(userId):
    '''  '''

    return dbc.Row(children = [

        # Left <
        dbc.Col(style = style['leftColStyle'],
                children = [

                    # Calendar <
                    dbc.Row(justify = 'center',
                            style = style['calendarStyle'],
                            children = calendarFunction(userId)),

                    # >

                    # UMKC Roo News <
                    dbc.Row(children = umkcRooNewsFunction(),
                            style = style['umkcRooNewsStyle'])

                    # >

                ]),

        # >

        # Center <
        dbc.Col(style = style['centerColStyle'],
                children = [

                    # Agenda <
                    dbc.Row(style = style['agendaStyle'],
                            children = agendaFunction(userId))

                    # >

                ]),

        # >

        # Right <
        dbc.Col(style = style['rightColStyle'],
                children = [

                    # Event Create <
                    dbc.Row(style = style['eventCreateStyle'],
                            children = [
                                eventViewLayout(userId)
                                # html.H1('create')

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


def calendarFunction(userId):
    '''  '''

    return dbc.Col(width = 'auto',
                  align = 'center',
                  children = [

                      # Date <
                      html.H4(children = strftime('%d %B %Y'),
                              style = style['calendarDateStyle'])

                      # >

                  ])


def umkcRooNewsFunction():
    '''  '''

    global articles

    # if (default) <
    if (articles == []):

        articles = [dbc.Card(style = {'border' : 0,
                                      'padding' : 10,
                                      'height' : 'auto',
                                      'borderRadius' : 10,
                                      'backgroundSize' : 'cover',
                                      'backgroundPosition' : 'center',
                                      'background' : 'url({})'.format(article['Picture'])

                                      },

                             # iterate (articles) <
                             children = [

                                 # Title <
                                 html.H4(className = 'card-title',
                                         children = article['Title'],
                                         style = style['umkcRooNewsCardH4Style']),

                                 # >

                                 # Date & Author <
                                 html.P(className = 'card-title',
                                        style = style['umkcRooNewsCardH4Style'],
                                        children = [

                                            'by {}'.format(article['Author']),
                                            ' on {}'.format(article['Date'])

                                        ]),

                                 # >

                                 # Redirect <
                                 dbc.Badge(children = 'Redirect',
                                           href = article['Link'],
                                           color = style['umkcRooNewsCardBadgeColor'],
                                           style = style['umkcRooNewsCardBadgeStyle'])

                                 # >

                             ]) for article in scrapeUMKCRooNews()]

                             # >

        return articles

    # >

    # else (not default) <
    else: return articles

    # >


def agendaFunction(userId):
    '''  '''

    global articles

    # Declaration <
    events = Event()
    output, sortedEvents = [], []
    events = events.getUpcoming(userId)
    s = sorted(['{}/{}/{} {}'.format(e['Year'], e['Month'], e['Day'], e['startTime']) for e in events])

    # >

    # while (list) <
    while (len(s) != 0):

        # iterate (events) <
        for e in events:

            # if (match) <
            if ('{}/{}/{} {}'.format(e['Year'], e['Month'], e['Day'], e['startTime']) == s[0]):

                sortedEvents.append(e)
                s.pop(0)

            # >

        # >

    # >

    # iterate (sorted events) <
    [output.append(e['Title']) for e in sortedEvents]

    # >

    # the above columns should contain card views to be presented to children
    # in return statement
