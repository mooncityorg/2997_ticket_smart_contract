# Import <
import pyodbc
from backEnd.API.Course import Course
from backEnd.API.Member import Member
from backEnd.API.User import User
from backEnd.API.Utility import application, childQueryTwo
from frontEnd.Layout.Login import loginLayout
from backEnd.API.User import User
# >

connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
)

mycursor = connection_string.cursor()

print(childQueryTwo(mycursor, "Course_Info", "*", "courseId", "1234", "userId", "JAD6TJ"))

# person = User()
# print("getUser = ", person.getUser(mycursor, "JAD6TJ"))
#
# myCourse = Course()
# print("getCourse = ", myCourse.getCourse(mycursor, "JAD6TJ"))
#
myMember = Member()
print("getMember = ", myMember.getMember(mycursor, "JAD6TJ"))
print("isHost = ", myMember.isHost(mycursor, "JAD6TJ"))