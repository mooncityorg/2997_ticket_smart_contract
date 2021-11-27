# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery, joinQuery

# >


class Event:

    def __init__(self):
        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )
        self.cursor = connection_string.cursor()

    def getEvent(self, eventId):

        return parentQuery(self.cursor, "Event_Info", "*", ("eventId", eventId))

    def getUpcoming(self, userId):

        items = joinQuery(self.cursor, "Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId))

    #this function gets the 10 most recent event actions (event creation, event updating, and event deletion)
    def getUpdates(self, userId):

        items = joinQuery(self.cursor, "Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId), True)



