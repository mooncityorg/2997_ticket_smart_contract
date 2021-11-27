# Import <
import pyodbc
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

    # Methods <

    def getEvent(self, eventId):
        '''get all event info based on eventId'''
        return parentQuery(self.cursor, "Event_Info", "*", ("eventId", eventId))

    # >
