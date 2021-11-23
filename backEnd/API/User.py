# Import <
import pyodbc
from backEnd.API.Utility import parentQuery
# >


class User:

    def __init__(self):
        '''  '''

        pass

    def getUser(self, cursor, userId) -> dict:

        return parentQuery(cursor, "User_Info", "*", userId)[0]