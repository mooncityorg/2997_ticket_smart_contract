# Import <
#from backEnd.User import User
from backEnd.Utility import application
#from backEnd.Appointment import Appointment
from frontEnd.Layout.Login import loginLayout

# >


# Main <
if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)

    pass # remove

# >
