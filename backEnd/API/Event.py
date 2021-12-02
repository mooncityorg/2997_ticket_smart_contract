# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery, joinQuery
from backEnd.API.Utility import parentQuery

# >


class Event:

    # Constructor <

    def __init__(self):

        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )

        self.cursor = connection_string.cursor()

    # >

    def getUpcoming(self, userId):

        return joinQuery(self.cursor, "Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId))

    #this function gets the 10 most recent event actions (event creation, event updating, and event deletion)
    def getUpdates(self, userId):

        return joinQuery(self.cursor, "Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId), True)

    # Methods <

    def getEvent(self, eventId):
        '''get all event info based on eventId'''
        return parentQuery(self.cursor, "Event_Info", "*", ("eventId", eventId))

    # >
