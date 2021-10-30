from Event import Event


class Person:

    # this will only work if we have this many values to unpack
    def __init__(self, info):
        self.infoDict = {**info}

    def createAppt(self, event: Event):
        if self.infoDict["createBool"]:
            self.infoDict["apptList"].append(event)

    def cancelAppt(self, ID):
        if self.infoDict["cancelBool"]:
            # how do you use list methods when referencing class attributes?
            # self.apptList.index(Event.getattr(ID), ID)
            for j in self.infoDict["apptList"]:
                if j.infoDict["id"] == ID: self.infoDict["apptList"].remove(j)

    def editAppt(self, info):
        # user is allowed to change value
        if self.infoDict["editBool"]:
            # find which appointment with list needs to change
            for i in self.infoDict["apptList"]:
                if i.infoDict["id"] == info["id"]:
                    event = i
                else:
                    print("no matching id found")
                    return 0

            # enumerate through each value in given info
            for i, (key, value) in enumerate(info.items()):
                if event.infoDict[key]: event.infoDict[key] = value

    # def checkAppt(self, time):
    # check if there is an upcoming event?

    # updates database from user input
    # def update(self, info):


if __name__ == "__main__":
    info = {"role": "Tutor", "name": "Ben Garver", "email": "BLGFQY", "phNum": "8371942885", "phProv": "Verison",
            "password": "tryOGhard", "department": "ASM", "createBool": True, "cancelBool": True, "editBool": True,
            "viewStudBool": True, "classes": [], "apptList": []}
    # test create Person class
    temp = Person(info)
    # text create Event class
    info = Event({"id": "123456", "type": "Office Hours", "time": "3:00pm", "location": "Atterbury"})
    # test createAppt
    temp.createAppt(info)
    print(temp.infoDict["apptList"])
    # get reference to first element in apptList
    ref = temp.infoDict["apptList"][0]
    # print for change verification
    print(ref.infoDict["time"])

    # random info to test editAppt
    info = {"id": "123456", "time": "15:00pm"}
    temp.editAppt(info)
    # print for change verification
    print(ref.infoDict["time"])

    # test cancelAppt
    temp.cancelAppt("123456")
    print(temp.infoDict["apptList"])

