# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout

from frontEnd.Layout.Home import homeLayout # remove
from backEnd.API.Utility import Verify, Authenticate # remove

# >


# Main <

if (__name__ == '__main__'):

    #application.layout = loginLayout
    #application.run_server(debug = True)

    driver = Verify('username', 'password')
    driver = Authenticate(driver)

# >
