# Import <
from backEnd.API.Utility import parentQuery

# >


class User:

    # Constructor <

    def __init__(self):
        pass
    # >

    # Methods <

    def getUser(self, userId) -> dict:
        '''get a user based on a userId'''
        return parentQuery("User_Info", "*", ("userId", userId))

    def getAllUser(self) -> dict:
        '''get all users'''
        return parentQuery("User_Info", "*", ("", ""))

    # >
