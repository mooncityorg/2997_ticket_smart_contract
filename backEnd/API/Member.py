# Import <
from backEnd.API.Utility import childQueryOne

# >


class Member:

    def __init__(self):
        '''  '''

        pass

    def getMember(self, cursor, userId):

        return childQueryOne(cursor, "Member_Info", "*", "userId", userId)

    # def isHost(self, cursor, memberId) -> bool:


