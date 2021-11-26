# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery

# >


class Member:

    def __init__(self):
        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )
        self.cursor = connection_string.cursor()

    # get all events a specific user is a member of
    def getMember(self, userId):

        return parentQuery(self.cursor, "Member_Info", "*", ("userId", userId))

    def isHost(self, memberId) -> bool:
        data = parentQuery(self.cursor, "Member_Info", "*", ("memberId", memberId))
        return data['isHost']

    def getHost(self, eventId) -> str:
        hostdata = childQuery(self.cursor, "Member_Info", "*", ("eventId", eventId), ("isHost", True))
        return hostdata['userId']
