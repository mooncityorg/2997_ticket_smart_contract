# Import <

from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout

# >


# Main <

if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)
    
# >

