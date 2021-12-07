# Import <
from backEnd.API.Utility import parentQuery, setQuery


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

    def setCourse(self, userId, courseDict):
        '''insert a new course into the database'''
        # Declaration <
        courseList = list()
        # >

        # Data Processing <
        for i in courseDict:

            # Split input data <
            title = i['Title'].split(" - ")
            dates = i['Start/End Date'].split(" - ")
            startDate, endDate = dates[0].split("/"), dates[1].split("/")
            times = i['Days & Times'].split(" ")
            days = ('Mo', 'Tu', 'We', 'Th', 'Fr')
            timeStr = str()
            for j in days:
                if j in times[0]: timeStr += '1'
                else: timeStr += '0'
            # >

            # Create new dictionaries <
            newCourse = {
                'courseId': i['Class Nbr'],
                'userId': userId,
                'Title': title[0],
                'Description': title[1],
                'dayOfWeek': timeStr,
                'startTime': times[1],
                'endTime': times[3],
                'startMonth': startDate[0],
                'startDay': startDate[1],
                'endMonth': endDate[0],
                'endDay': endDate[1],
                'instructor': i['Instructor'].split(",\n")[0],
                'location': i['Room'],
                # 'isOnline': ,
                # 'studentOf':
            }
            courseList.append(newCourse)
            # >

        print("\ncourses to be added, after processing\n-----")
        for i in courseList:
            print(i)

        # >

        # Pass new dictionary to set query <
        setQuery("Course_Info", courseList)
        # >
    # >
