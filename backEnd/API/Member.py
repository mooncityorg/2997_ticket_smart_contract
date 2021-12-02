# Import <
from backEnd.API.Utility import parentQuery, childQuery

# >


class Member:

    # Constructor <

    def __init__(self):
        pass

    # >

    # Methods <

    def getMember(self, userId):
        '''get all events a specific user is a member of'''
        return parentQuery("Member_Info", "*", ("userId", userId))

    def isHost(self, memberId) -> bool:
        '''get isHost boolean for a specific member of an event'''
        data = parentQuery("Member_Info", "*", ("memberId", memberId))
        return data['isHost']

    def getHost(self, eventId) -> str:
        '''get the userId of an event's host'''
        hostdata = childQuery("Member_Info", "*", ("eventId", eventId), ("isHost", True))
        return hostdata['userId']

    # >
