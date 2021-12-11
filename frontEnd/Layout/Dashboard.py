# Import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from backEnd.API.Utility import scrapeUMKCRooNews
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application

# >


# Declaration <
driver = None
style = getJSON(file = '/frontEnd/Resource/Dashboard.json')

# >


def dashboardLayout(userId):
    '''  '''

    global driver

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

                                dbc.Card(style = {'border' : 0,
                                                  'height' : 'auto',
                                                  'borderRadius' : 10,
                                                  'backgroundSize' : 'cover',
                                                  'backgroundPosition' : 'center',
                                                  'background' : 'url({})'.format(article['Picture'])},

                                         children = [

                                             dbc.CardBody(children = [

                                                 # Header <
                                                 html.H4(className = 'card-title',
                                                         children = article['Title']),

                                                 # >

                                                 # Author & Date <
                                                 html.P(className = 'card-text',
                                                        children = [

                                                            'by {}'.format(article['Author']),
                                                            'on {}'.format(article['Date'])

                                                        ]),

                                                 # >

                                                 # Redirect <
                                                 dbc.Badge(children = 'Redirect',
                                                           href = article['Link'],
                                                           color = style['umkcRooNewsCardBadgeColor'],
                                                           style = style['umkcRooNewsCardBadgeStyle'])

                                                 # >

                                             ])

                                             # >

                                         ])

                            for article in scrapeUMKCRooNews(driver)])

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
