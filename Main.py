# Import <
from backEnd.Utility import application, Verify
from frontEnd.Layout.Login import loginLayout


# >


# Main <
if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)

    #Verify('ala2q6', 'muhatTracer@1999')

# >
