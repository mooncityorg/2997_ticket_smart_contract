# Import <
import pyodbc
from backEnd.API.User import User
from backEnd.API.Event import Event
from backEnd.API.Course import Course
from backEnd.API.Member import Member
from backEnd.API.Location import Location
from backEnd.API.Utility import application, parentQuery, childQuery
from frontEnd.Layout.Login import loginLayout
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
temp = parentQuery(cursor, "Course_Info", "*", ("userId", "JAD6TJ"))
print("result = ")
for i in temp: print(i)

print("\n\*---------------------------------------------------------------*\ \nchild query test")
print("result = \n", childQuery(cursor, "Course_Info", "*", ("courseId", "1234"), ("userId", "JAD6TJ")))

print("\n\*---------------------------------------------------------------*\ \nuser class test")
person = User()
print("getUser result = \n", person.getUser("JAD6TJ"))
temp = person.getAllUser()
print("getAllUser result = ")
for i in temp: print(i)

print("\n\*---------------------------------------------------------------*\ \ncourse class test")
course = Course()
temp = course.getCourseList("JAD6TJ")
print("getCourseList result = ")
for i in temp: print(i)
print("getCourse result = \n", course.getCourse("1234"))

print("\n\*---------------------------------------------------------------*\ \nmember class test")
myMember = Member()
print("getMember result = \n", myMember.getMember("JAD6TJ"))
print("isHost result = ", myMember.isHost("12345"))
print("getHost result = ", myMember.getHost("12345"))

print("\n\*---------------------------------------------------------------*\ \nlocation class test")
location = Location()
print("getLocationList result = \n", location.getLocationList("JAD6TJ"))
print("getLocation result = \n", location.getLocation("1234"))

print("\n\*---------------------------------------------------------------*\ \nevent class test")
event = Event()
print("getEvent result = \n", event.getEvent("123456"))

