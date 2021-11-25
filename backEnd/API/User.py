# Import <
import pyodbc
from backEnd.API.Utility import parentQuery
# >


class User:

    def __init__(self):
        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )
        self.cursor = connection_string.cursor()

    # get a user based on a userId
    def getUser(self, userId) -> dict:

        return parentQuery(self.cursor, "User_Info", "*", ("userId", userId))

    # get all users
    def getAllUser(self) -> dict:

        return parentQuery(self.cursor, "User_Info", "*", ("", ""))
