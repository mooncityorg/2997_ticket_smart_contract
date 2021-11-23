# Import <
from backEnd.API.Utility import childQueryOne

# >


class Course:

    def __init__(self):
        '''  '''

        pass

    def getCourse(self, cursor, userId) -> list:

        return childQueryOne(cursor, "Course_Info", "*", "userId", userId)

