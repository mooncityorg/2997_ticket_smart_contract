# Import <
from backEnd.API.Utility import parentQuery

# >


class Location:

    # Constructor <

    def __init__(self):
        pass

    # >

    # Methods <

    def getLocationList(self, userId):
        '''get all location options for a specific user'''
        return parentQuery("Location_Info", "*", ("userId", userId))

    def getLocation(self, locationId):
        '''get information about a location'''
        return parentQuery("Location_Info", "*", ("locationId", locationId))

    # >
