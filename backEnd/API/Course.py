# Import <
import pyodbc
from backEnd.API.Utility import parentQuery

# >


class Course:

    # Constructor <

    def __init__(self):

        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )

        self.cursor = connection_string.cursor()

    # >

    # Methods <

    def getCourseList(self, userId) -> list:
        '''get a list of courses based on userId'''
        return parentQuery(self.cursor, "Course_Info", "*", ("userId", userId))

    def getCourse(self, courseId) -> dict:
        '''get course info'''
        return parentQuery(self.cursor, "Course_Info", "*", ("courseId", courseId))

    # >
