# Import <
from backEnd.API.Utility import parentQuery, joinQuery

# >


class Event:

    # Constructor <

    def __init__(self):
        pass

    # >

    # Methods <

    def getUpcoming(self, userId):
        ''''''
        return joinQuery("Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId))

    def getUpdates(self, userId):
        '''this function gets the 10 most recent event actions (event creation, event updating, and event deletion)'''
        return joinQuery("Event_Info", "e", "locationId", "Location_Info", "l", "locationId", "*", ("userId", userId), True)

    def getEvent(self, eventId):
        '''get all event info based on eventId'''
        return parentQuery("Event_Info", "*", ("eventId", eventId))

    # >
