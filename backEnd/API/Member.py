# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery

# >


class Member:

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

    def getMember(self, userId):
        '''get all events a specific user is a member of'''
        return parentQuery(self.cursor, "Member_Info", "*", ("userId", userId))

    def isHost(self, memberId) -> bool:
        '''get isHost boolean for a specific member of an event'''
        data = parentQuery(self.cursor, "Member_Info", "*", ("memberId", memberId))
        return data['isHost']

    def getHost(self, eventId) -> str:
        '''get the userId of an event's host'''
        hostdata = childQuery(self.cursor, "Member_Info", "*", ("eventId", eventId), ("isHost", True))
        return hostdata['userId']

    # >
