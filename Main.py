# Import <
import pyodbc
from backEnd.API.Course import Course
from backEnd.API.Member import Member
from backEnd.API.User import User
from backEnd.API.Utility import application, parentQuery, childQuery
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
cursor = connection_string.cursor()

print("\n\*---------------------------------------------------------------*\ \nparent query test")
print("result = ", parentQuery(cursor, "Course_Info", "*", ("userId", "JAD6TJ")))

print("\n\*---------------------------------------------------------------*\ \nchild query test")
print("result = ", childQuery(cursor, "Course_Info", "*", ("courseId", "1234"), ("userId", "JAD6TJ")))

print("\n\*---------------------------------------------------------------*\ \nuser class test")
person = User()
print("result = ", person.getUser("JAD6TJ"))
temp = person.getAllUser()
print("result = ")
for i in temp:
    print(i)


# myCourse = Course()
# print("getCourse = ", myCourse.getCourse("JAD6TJ"))
#
# myMember = Member()
# print("getMember = ", myMember.getMember("JAD6TJ"))
# print("isHost = ", myMember.isHost("JAD6TJ"))