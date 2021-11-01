from frontEnd.Layout.Login import loginLayout
from backEnd.Tool import application


if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)
