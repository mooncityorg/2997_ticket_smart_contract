# Import <
import dash
from dash import html, dcc
from backEnd.API import User
from backEnd.API.Utility import getJSON, application
from dash import Dash, html, Input, Output, callback_context, State
# >

userClass = User.User()
def searchLayout(name):
    global printStringName
    global printStringUserId
    global printStringRole
    global printStringZoomId
    global temp
    temp = []
    printStringName = []
    printStringUserId = []
    printStringRole = []
    printStringZoomId = []
    people = userClass.getAllUser()
    for i in people:
        if name == "All":
            printStringName.append(i["Name"])
            printStringUserId.append(i["userId"])
            printStringRole.append(i["Role"])
            printStringZoomId.append(i["zoomId"])
        elif name == "Students":
            if i["Role"] == "Student":
                printStringName.append(i["Name"])
                printStringUserId.append(i["userId"])
                printStringRole.append(i["Role"])
                printStringZoomId.append(i["zoomId"])
        elif name == "Tutors":
            if i["Role"] == "Tutor":
                printStringName.append(i["Name"])
                printStringUserId.append(i["userId"])
                printStringRole.append(i["Role"])
                printStringZoomId.append(i["zoomId"])



    for i in printStringName:
        temp.append(html.Div([
            html.Br(),
            html.H6(i),
            html.Button("Details",id = "infoButton",n_clicks=0),
            html.Div(id='infoOut')
        ],
            style = {"text-colo":"#FFD52F ","marginTop":5,"position": "relative", "left":800,"background-color": "#0066CC", "height": 110, "width": 325,"text-align":"center","border-radius":25},
        ))

    return temp


@application.callback(
    Output('infoOut','children'),
    Input('infoButton','n_clicks')
)
def displayClick(data):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    #return html.H1(data)