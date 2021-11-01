from Main import app
from frontEnd.Layout.Login import mainLayout

if __name__ == '__main__':
    app.layout = mainLayout()
    app.run_server(debug=True)