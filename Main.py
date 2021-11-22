# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout
from frontEnd.Layout.Home import homeLayout # remove

# >


# Main <
if (__name__ == '__main__'):

    application.layout = homeLayout
    application.run_server(debug = True)

# >
