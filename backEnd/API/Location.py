# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery
# >


class Location:

    def __init__(self):
        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )
        self.cursor = connection_string.cursor()

    # get all location options for a specific user
    def getLocationList(self, userId):

        return parentQuery(self.cursor, "Location_Info", "*", ("userId", userId))

    # get information about a location
    def getLocation(self, locationId):

        return parentQuery(self.cursor, "Location_Info", "*", ("locationId", locationId))