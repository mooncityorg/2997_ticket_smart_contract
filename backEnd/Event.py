
class Event:

    # input should be list in specified order
    def __init__(self, info):
        self.ID, self.type, self.time, self.location, self.organizer, self.invitee, self.classNum, self.topic, self.notes = info

    # updates database from user input
    # def update(self, info):


