# Import <
from dash import dcc, html
#from selenium import webdriver
import dash_bootstrap_components as dbc
from frontEnd.Layout.Home import homeLayout
from dash.dependencies import Input, Output, State
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from backEnd.API.Utility import getJSON, application, Login, Verify

# >


# Declaration <
#options = Options()
#options.headless = True
style = getJSON(file = '/frontEnd/Resource/Login.json')
#driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

# >


loginLayout = html.Div(id = 'loginLayoutId',
                       children = [

                           # Logo <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divLogoId',
                                        children = [

                                            html.Img(src = style['logoSrc'],
                                                     style = style['logoStyle']),

                                        ], style = style['divLogoStyle']),

                           width = 4)], justify = 'center'),

                           # >

                           # Input <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divInputId',
                                        children = [

                                            # Username <
                                            dbc.Row([dbc.Col(

                                                dbc.Input(id = 'inputUsernameId',
                                                          placeholder = 'Username',
                                                          style = style['usernameStyle']),

                                            width = 3)], justify = 'center'),

                                            # >

                                            # Password <
                                            dbc.Row([dbc.Col(

                                                dbc.Input(n_submit = 0,
                                                          debounce = True,
                                                          type = 'password',
                                                          id = 'inputPasswordId',
                                                          placeholder = 'Password',
                                                          style = style['passwordStyle']),

                                            width = 3)], justify = 'center'),

                                            # >

                                            # Forgot Password <
                                            dbc.Row([dbc.Col(

                                                dbc.Badge(children = 'Forgot Password?',
                                                          href = style['forgotPasswordHref'],
                                                          color = style['forgotPasswordColor'],
                                                          style = style['forgotPasswordStyle']),

                                            width = 3)], justify = 'center'),

                                            # >

                                            # Submit <
                                            dbc.Row([dbc.Col(

                                                #

                                            width = 3)], justify = 'center')

                                            # >

                                        ], style = style['divInputStyle']),

                           width = 10)], justify = 'center'),

                           # >

                           # Redirect <
                           dbc.Row([dbc.Col(

                               html.Div(id = 'divRedirectId',
                                        children = [

                                            dbc.Badge(children = '3ASJW6',
                                                      href = style['redirectHref'],
                                                      color = style['redirectColor'])

                                        ], style = style['divRedirectStyle']),

                           width = 10)], justify = 'center')

                           # >

                       ], style = style['loginLayoutStyle'])
