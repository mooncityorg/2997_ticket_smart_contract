from backEnd.Tool import application
from frontEnd.Layout.Login import loginLayout


if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)
