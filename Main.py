# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout
from frontEnd.Layout.Home import homeLayout # remove

# >


# Main <
if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)

# >



'''
                                                dbc.Input(id = 'inputUsernameId',
                                                          placeholder = 'Username',
                                                          style = style['usernameStyle']),

                                                dbc.Input(n_submit = 0,
                                                          debounce = True,
                                                          type = 'password',
                                                          id = 'inputPasswordId',
                                                          placeholder = 'Password',
                                                          style = style['passwordStyle']),

'''



