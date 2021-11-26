# Import <
import pyodbc
from backEnd.API.Utility import parentQuery, childQuery
# >


class Course:

    def __init__(self):
        connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )
        self.cursor = connection_string.cursor()

    # get a list of courses based on userId
    def getCourseList(self, userId) -> list:

        return parentQuery(self.cursor, "Course_Info", "*", ("userId", userId))

    # get course info
    def getCourse(self, courseId) -> dict:

        return parentQuery(self.cursor, "Course_Info", "*", ("courseId", courseId))
