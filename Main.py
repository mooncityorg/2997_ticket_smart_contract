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


