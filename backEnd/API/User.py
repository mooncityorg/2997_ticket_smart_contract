# Import <
import pyodbc
from backEnd.API.Utility import parentQuery

# >


class User:

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

    def getUser(self, userId) -> dict:
        '''get a user based on a userId'''
        return parentQuery(self.cursor, "User_Info", "*", ("userId", userId))

    def getAllUser(self) -> dict:
        '''get all users'''
        return parentQuery(self.cursor, "User_Info", "*", ("", ""))

    # >
