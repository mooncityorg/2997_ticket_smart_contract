# Import <
import pyodbc
from backEnd.API.Utility import parentQuery

# >


class Location:

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

    def getLocationList(self, userId):
        '''get all location options for a specific user'''
        return parentQuery(self.cursor, "Location_Info", "*", ("userId", userId))

    def getLocation(self, locationId):
        '''get information about a location'''
        return parentQuery(self.cursor, "Location_Info", "*", ("locationId", locationId))

    # >
