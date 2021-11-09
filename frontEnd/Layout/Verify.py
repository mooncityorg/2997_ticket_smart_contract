# Import <
from dash import dcc, html
from backEnd.Utility import getJSON, application
from dash.dependencies import Input, Output, State

# >


# Declaration <
loginStyle = getJSON(file = '/frontEnd/Resource/Login.json')
verifyStyle = getJSON(file = '/frontEnd/Resource/Verify.json')

# >


verifyLayout = html.Div(id = 'verifyLayoutId',
                        children = [

                            # Confirm <
                            dcc.ConfirmDialog(id = 'verifyConfirmId',
                                              message = 'The verification you entered was incorrect.'),

                            # >

                            # Background <
                            html.Div(id = 'divBackgroundId',
                                     children = [

                                         # Image <
                                         html.Div(id = 'divImageId',
                                                  children = [

                                                      html.Img(src = loginStyle['imgSrc'],
                                                               style = loginStyle['imgStyle'])

                                                  ], style = loginStyle['divImageStyle']),

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
                                                                             placeholder = '6-Digit Code',
                                                                             style = verifyStyle['codeStyle'])

                                                               ], style = verifyStyle['divCodeStyle']),

                                                      # >

                                                      # Verify <
                                                      html.Div(id = 'divVerifyId',
                                                               children = [

                                                                   html.Button(n_clicks = 0,
                                                                               children = 'Verify',
                                                                               id = 'buttonVerifyId',
                                                                               style = verifyStyle['verifyStyle'])

                                                               ], style = verifyStyle['divVerifyStyle'])

                                                      # >

                                                  ], style = loginStyle['divInputStyle']),

                                         # >

                                         # Redirect <
                                         dcc.Markdown(id = 'redirectId',
                                                      children = [

                                                          ('### ' + ''.join(i for i in loginStyle['redirectChildren']))

                                                      ], style = loginStyle['redirectStyle'])

                                         # >

                                     ], style = loginStyle['divBackgroundStyle'])

                            # >

                        ], style = loginStyle['layoutStyle'])


@application.callback(Output('verifyLayoutId', 'children'),
                      Output('verifyConfirmId', 'displayed'),
                      Input('inputCodeId', 'n_submit'),
                      Input('buttonVerifyId', 'n_clicks'),
                      State('inputCodeId', 'value'),
                      State('verifyLayoutId', 'children'))
def verifyFunction(submit: int, click: int, code: str, layout: list):
    '''  '''

    # if (Verify) <
    if (click or submit):

        return (layout, False)

    # >

    return (layout, False)
