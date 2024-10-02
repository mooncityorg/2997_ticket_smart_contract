# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout

from frontEnd.Layout.Home import homeLayout # remove
from backEnd.API.Event import Event

# >


# Main <
if (__name__ == '__main__'):

    application.layout = loginLayout() # homeLayout('JAD6TJ')
    # application.run_server()

# >

