# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout
from backEnd.API.User import User
from backEnd.API.Course import Course
# >


# Main <
# if (__name__ == '__main__'):
#
#     application.layout = loginLayout
#     application.run_server(debug = True)

print("\n\*---------------------------------------------------------------*\ \n set user test")
person = User()

print("adding info to table")
dict = {'name' : 'Alex Arbuckle', 'userId' : 'ala2q6'}
person.setUser(dict)

print("table after addition")
temp = person.getAllUser()
for i in temp:
    print(i)

print("\n\*---------------------------------------------------------------*\ \n set course test")
course = Course()

courseInput = [

        {
            'Title': 'COMP-SCI 320 - Data Com. and Networking',
            'Class Nbr': '47030',
            'Days & Times': 'MoWe 4:00PM - 5:15PM',
            'Room': 'MNLC-Rm 452',
            'Instructor': 'Farid Nait-Abdesselam,\nKhalid Almalki',
            'Start/End Date': '08/23/2021 - 12/17/2021'
        },

        {
            'Title': 'COMP-SCI 451R - Software Engineering Capstone',
            'Class Nbr': '40198',
            'Days & Times': 'MoWe 5:30PM - 6:45PM',
            'Room': 'Haag Hall-Rm 00301',
            'Instructor': 'Sravya Chirandas',
            'Start/End Date': '08/23/2021 - 12/17/2021'
        },

        {
            'Title': 'COMP-SCI 461 - Intro Artificial Intell',
            'Class Nbr': '45164',
            'Days & Times': 'MoWeFr 1:00PM - 1:50PM',
            'Room': 'Education-Rm 00119',
            'Instructor': 'Brian Hare,\nVineeth Reddy Sheri',
            'Start/End Date': '08/23/2021 - 12/17/2021'
        }
]

course.setCourse("blgfqy", courseInput)

print("\ntable (where userId) after addition\n-----", end="")
temp = course.getCourseList("blgfqy")
for i in temp:
    print(i)

# >

