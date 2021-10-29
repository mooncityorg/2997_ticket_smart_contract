import Event

class Person:

    def __init__(self, info):
        self.role, self.name, self.email, self.phNum, self.phProv, self.password, self.department, self.createBool, self.cancelBool, self.editBool, self.viewStud, self.classList, self.apptList = info

    def createAppt(self, info):
        if self.createBool:
            event = Event(info)
            self.apptList.append(event)

    def cancelAppt(self, ID):
        if self.cancelBool:
            # how do you use list methods when referencing class attributes?
            # self.apptList.index(Event.getattr(ID), ID)
            for j in self.apptList:
                if j.ID == ID: self.apptList.remove(j)

    # def editAppt(self, info):
    #     if self.editBool:
    #         # pass and mostly empty list? # need to parse info?
    #         for j in self.apptList:
    #             if j.ID == info[0]:
                    # assign changed values


    # def checkAppt(self, time):
        # check if there is an upcoming event?

    # updates database from user input
    # def update(self, info):
