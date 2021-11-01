from Main import app
from dash import dcc
from dash import html
from backEnd.Tool import getJSON
from dash.dependencies import Input, Output

style = getJSON(file = '/frontEnd/Resource/Login.json')

#---crud code -========================
# loginLayout = html.Div(id = 'divId',
#                        children = [
#
#                            # Background <
#                            html.Div(id = 'divDivId',
#                                     children = [
#
#                                         # UMKC Logo <
#                                         html.Div(id = 'divDivDivIdA',
#                                                  children = [
#
#                                                      html.Img(src = style['divDivDivImgSrc'],
#                                                               style = style['divDivDivImgStyle'])
#
#                                                  ], style = style['divDivDivStyleA']),
#
#                                         # email Input <
#                                         html.Div(id = 'EmailEntry',
#                                                  children = [
#                                                     dcc.Input(
#                                                          id = 'email',
#                                                          type = "email",
#                                                          placeholder  = "Enter email",
#                                                          debounce=True,
#                                                          autoComplete = "on",
#
#                                                      ),
#                                                  ], style = style['divDivDivStyleB']),
#
#                                         # password Input <
#                                         html.Div(id='PasswordEntry',
#                                                  children = [
#                                                     dcc.Input(
#                                                          id = 'Password',
#                                                          type = "password",
#                                                          placeholder  = "Enter password",
#                                                          debounce=True,
#                                                          autoComplete = "on",
#
#                                                      ),
#
#                                                  ])
#                            ],
#                                     style = style['divDivStyle']),
#
#                                         html.Div(id='SubmitButton',
#                                             children = [
#                                                 html.Button('Submit', id='submit-val', n_clicks=0
#                                         )
#                                     ],
#                                         style = style['Button'])
#
#                       ], style = style['divStyle'])
#
# # this is where callback goes
# # we grab states of username and password
# # input is button id # output is uncertain
# # back end is called here

#not crud code but styling integrated =-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def mainLayout():
    dcc.Location(id='url', refresh=False),
    return html.Div(
        children = [
            html.Div(style = {
                "top": 0,
                "left" : 0,
                "right": 0,
                "bottom": 0,
                "textAlign": "center",
                "position": "fixed",
                "backgroundColor" : "#04487F"}),
        html.Div(
            children=[
                html.Div(style={"top": 60,
                    "left": 80,
                    "right": 80,
                    "bottom": 100,
                    "borderRadius": 10,
                    "padding": 10,
                    "textAlign": "center",
                    "position": "absolute",
                    "border": "5px solid #FFD52F",
                    "backgroundPosition": "center",
                    "background": "url(https://www.umkc.edu/global-assets/images/Womens-Soccer-at-the-Liberty-Memorial.jpg)"}),
            html.Div(
                children=[
                    html.Div(html.Img(src="https://2.bp.blogspot.com/-0Dy52Hi8_Kw/UXAZK8YX9uI/AAAAAAAAB34/57cWrXS6uXU/s320/UMKC-logo.png"),
                            style={"top": 60,
                            "left": 80,
                            "right": 80,
                            "bottom": 100,
                            "borderRadius": 10,
                            "padding": 10,
                            "textAlign": "center",
                            "position": "absolute",
                            "border": "5px solid #FFD52F",
                            "backgroundPosition": "center"}),
                html.Div(
                    children=[
                        html.Div(style = {
                            "width": 380,
                            "height": 315,
                            "border": 1,
                            "backgroundColor": "#FFD52F ",
                            "position": "absolute",
                            "left": 767,
                            "marginTop": 70,
                            "bottom" : 382,
                            "border-radius" : 25,
                            }),
                    html.Div(
                        children=[
                            html.Div(style = {
                                "width": 365,
                                "height": 300,
                                "border": 1,
                                "backgroundColor": "#04487F",
                                "position": "absolute",
                                "left": 775,
                                "marginTop": 70,
                                "bottom" : 390,
                                "border-radius" : 25,
                                }),
                        html.Div (
                            children = [
                                html.Div(dcc.Input(
                                    id = 'Email',
                                    type = "email",
                                    placeholder  = "Enter email",
                                    debounce=True,
                                    autoComplete = "on"), style = {
                                    "bottom": 575,
                                    "left": 870,
                                    "position": "absolute",
                                    "border-radius" : 25}),
                            html.Div(
                                children=[
                                    html.Div(html.Button(children=[
                                        html.Img(
                                            src="https://freepngimg.com/thumb/categories/1428.png",
                                            id='submit',
                                            n_clicks=0,
                                            style={
                                                "bottom": 450,
                                                "left": 895,
                                                "height": 130,
                                                "width": 120,
                                                "position": "absolute",
                                            })]))]),
                                html.Div(
                                    children=[
                                        html.Div(dcc.Input(
                                          id = 'Password',
                                          type = "password",
                                          placeholder  = "Enter password",
                                          debounce=True,
                                          autoComplete = "on",), style ={
                                          "bottom": 545,
                                          "left": 870,
                                          "position": "absolute",
                                          "border-radius" : 25})
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )

                            ]
                        )
                    ]
                ),
            html.Div(id="results")
        ])

@app.callback(
    [Output(component_id='results', component_property='children')],
    [Input(component_id="Email", component_property='value'),
    Input(component_id="Password", component_property='value'),
    Input(component_id='submit', component_property='n_clicks')]

)
def showemailpass(email, password, n_clicks):
    print (email)
    print(password)
    print(n_clicks)
    return["working"]