# Import <
from backEnd.API.Utility import parentQuery, setQuery

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

    def setUser(self, userDict):
        '''insert a new user into the database'''
        userList = list()
        userList.append(userDict)
        setQuery("User_Info", userList)
    # >
