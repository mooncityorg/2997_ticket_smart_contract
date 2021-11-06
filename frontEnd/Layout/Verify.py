# Import <
from dash import dcc, html
from backEnd.Tool import getJSON, application
from dash.dependencies import Input, Output, State

# >


style = getJSON(file = '/frontEnd/Resource/Verify.json')
verifyLayout = html.Div(id = 'verifyLayoutId',
                        children = [

                            # Warning <
                            dcc.ConfirmDialog(id = 'verifyWarningId',
                                              message = 'The authentication you entered was incorrect.'),

                            # >

                            # Input <
                            html.Div(id = 'divInputId',
                                     children = [

                                         # Code <
                                         html.Div(id = 'divCodeId',
                                                  children = [

                                                      dcc.Input(value = '',
                                                                n_submit = 0,
                                                                debounce = True,
                                                                id = 'inputCodeId',
                                                                style = style['inputStyle'],
                                                                placeholder = '6-Digit Code')

                                                  ], style = style['divCodeStyle']),

                                         # >

                                         # Verify <
                                         html.Div(id = 'divVerifyId',
                                                  children = [

                                                      html.Button(n_clicks = 0,
                                                                  children = 'Verify',
                                                                  id = 'buttonVerifyId',
                                                                  style = style['verifyStyle'])

                                                  ], style = style['divVerifyStyle'])

                                         # >

                                     ], style = style['divInputStyle'])

                            # >

                        ])


@application.callback(Output('verifyLayoutId', 'children'),
                      Output('verifyWarningId', 'displayed'),
                      Input('inputCodeId', 'n_submit'),
                      Input('buttonVerifyId', 'n_clicks'),
                      State('inputCodeId', 'value'),
                      State('verifyLayoutId', 'children'))
def verifyFunction(submit: int, click: int, code: str, layout: list):
    ''' return:
            layout: does user proceed?
            warning: has user encountered error?
    '''

    # if (Verify) <
    if (click or submit):

        return layout, False

    # >

    return layout, False
