# Import <
from backEnd.API.Utility import parentQuery

# >


class Course:

    # Constructor <

    def __init__(self):
        pass

    # >

    # Methods <

    def getCourseList(self, userId) -> list:
        '''get a list of courses based on userId'''
        return parentQuery("Course_Info", "*", ("userId", userId))

    def getCourse(self, courseId) -> dict:
        '''get course info'''
        return parentQuery("Course_Info", "*", ("courseId", courseId))

    # >
