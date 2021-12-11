# Import <
import pyodbc
from os import path
from json import load
from dash import Dash
from time import sleep
from time import strftime
from string import punctuation
from selenium import webdriver
import dash_bootstrap_components as dbc
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# >


# Declaration <

application = Dash(suppress_callback_exceptions = True,
                   external_stylesheets = [dbc.themes.BOOTSTRAP])

server = application.server

# "Driver=ODBC Driver 17 for SQL Server;" # Linux
# "Driver={SQL Server};" # Windows
connection_string = pyodbc.connect(
            "Driver=ODBC Driver 17 for SQL Server;"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
        )

cursor = connection_string.cursor()

# >


def getJSON(file: str) -> dict:
    '''  '''

    delimiter = '/'
    realpath = path.realpath(__file__)
    while (True):

        # try (if Linux) <
        try:

            directory = delimiter.join(realpath.split(delimiter)[:-3])
            with open(f'{directory}{file}', 'r') as fin:

                return load(fin)

        # >

        # except (then Windows) <
        except FileNotFoundError:

            delimiter = '\\'
            realpath = realpath[2:]

        # >


def Verify(password: str) -> bool:
    '''  '''

    # try (if password) <
    try:

        hasUpper, hasDigit, hasPunctuation = False, False, False
        for c in password:

            if (c.isupper()): hasUpper = True
            if (c.isdigit()): hasDigit = True
            if (c in punctuation): hasPunctuation = True

        # if (valid) else (not valid) <
        if (hasUpper and hasDigit and hasPunctuation): return True
        else: return False

        # >

    # >

    # except (then not password) <
    except TypeError: return False

    # >


def Login(username: str, password: str) -> bool:
    '''  '''

    # Declaration <
    #options = Options()
    #options.headless = True
    username += '@umsystem.edu'
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Verify']
    driver = webdriver.Chrome(ChromeDriverManager().install())#, options = options)

    # >

    # Website <
    driver.get(setting['Website'])


    # >

    # try (if valid) <
    try:

        # Username <
        driver.find_element_by_xpath(setting['usernameInput']).send_keys(username)
        driver.find_element_by_xpath(setting['usernameButton']).click(), sleep(1)

        # >

        # Password <
        driver.find_element_by_xpath(setting['passwordInput']).send_keys(password)
        driver.find_element_by_xpath(setting['passwordButton']).click(), sleep(1)

        # >

        # Check <
        driver.find_element_by_xpath(setting['Check']).text

        # >

        return driver

    # >

    # except (then invalid) <
    except NoSuchElementException: return None

    # >


def Authenticate(driver, code = None):
    '''  '''

    # Declaration <
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Authenticate']

    # >

    # try (if valid) <
    try:

        # if (code) <
        if (code):

            # Code <
            driver.find_element_by_xpath(setting['codeInput']).send_keys(code)
            driver.find_element_by_xpath(setting['codeButton']).click(), sleep(5)

            # >

        # >

        else:

            # Select <
            driver.find_element_by_xpath(setting['textButton']).click(), sleep(1)

            # >

        return driver

    # >

    # except (then invalid) <
    except NoSuchElementException: return None

    # >


def scrapeUser(driver):
    '''  '''

    # Declaration <
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['scrapeUser']

    # >
    # a tab to check if user is a tutor in which case we return
    # the driver and then a dictionary of if they are a tutor and
    # their name. then if they are a tutor we execute future
    # 'scrapeTutor' function to gather the classes they tutor in

    # (-> Personal Information -> Names) <
    driver.find_element_by_xpath(setting['personalInformationButton']).click(), sleep(1)
    driver.find_element_by_xpath(setting['namesButton']).click(), sleep(1)

    # >

    # (-> Name) <
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    name = driver.find_element_by_xpath(setting['nameText']).text
    # >

    # (-> Back) <
    driver.switch_to.default_content()
    driver.find_element_by_xpath(setting['backButton']).click(), sleep(1)

    # >

    return (driver, {'name' : name})


def scrapeCourse(driver):
    '''  '''

    # Declaration <
    schedule = []
    month, year = strftime('%m %Y').split()
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['scrapeSchedule']
    semester = [key for key, value in setting['Semester'].items() if (month in value)][0]

    # >

    # (-> Manage Classes -> My Class Schedule) <
    driver.find_element_by_xpath(setting['manageClassesButton']).click(), sleep(1)
    driver.find_element_by_xpath(setting['myClassScheduleButton']).click(), sleep(2)

    # >

    # (-> Select Term) <
    termA = (f'{year} {semester} Semester')
    driver.find_element_by_xpath(setting['menuButton']).click(), sleep(1)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    for i in range(50):

        # try (if term) <
        try:

            termB = driver.find_element_by_xpath(setting['termText'].replace('<>', str(i))).text

            # if (termA is termB) <
            if (termA == termB):

                driver.find_element_by_xpath(setting['termButton'].replace('<>', str(i))).click()
                driver.find_element_by_xpath(setting['continueButton']).click(), sleep(1)

            # >

        # except (then not term) <
        except NoSuchElementException: pass

        # >

    # >

    # Filter Schedule <
    driver.find_element_by_xpath(setting['droppedButton']).click()
    driver.find_element_by_xpath(setting['waitlistedButton']).click()
    driver.find_element_by_xpath(setting['filterButton']).click(), sleep(0.25)

    # >

    # iterate (course) <
    for i in range(0, 50, 2):

        # try (if course) <
        try:

            course = {}
            for k, v in setting['Course'].items():

                course[k] = driver.find_element_by_xpath(v.replace('<>', str(i))).text

            schedule.append(course)

        # >

        # except (then not course) <
        except NoSuchElementException: pass

        # >

    # >

    # (-> Back) <
    driver.switch_to.default_content()
    driver.find_element_by_xpath(setting['backButton']).click(), sleep(1)

    # >

    return (driver, schedule)


def scrapeUMKCRooNews():
    '''  '''

    # Declaration <
    articles = []
    #options = Options()
    #options.headless = True
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['umkcRooNews']
    driver = webdriver.Chrome(ChromeDriverManager().install())#, options = options)

    # >

    # Website <
    driver.get(setting['Website'])
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(0.25)

    # >

    # iterate (articles)
    for i in range(1, 13):

        article = {}
        for key, value in setting['Article'].items():

            value = value.replace('<>', str(i))

            # if (link) <
            if (key == 'Link'):

                link = driver.find_element_by_xpath(value).get_attribute('href')
                article[key] = link

            # >

            # elif (picture) <
            elif (key == 'Picture'):

                picture = driver.find_element_by_xpath(value).value_of_css_property('background-image')
                picture = picture.split('"')[1]
                article[key] = picture

            # >

            # else (title, author, date) <
            else:

                other = driver.find_element_by_xpath(value).text
                article[key] = other

            # >

        articles.append(article)

    return articles


def parentQuery(tableName, columns, primary: tuple):
    '''gets information from a table based on single key input'''

    # Declaration <
    columnNames = list()
    query = str()

    # >

    # Column Names <
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(tableName)
    cursor.execute(query)
    for x in cursor.fetchall(): columnNames.append(x[0])
    # print(columnNames)

    # >

    # Build Query <
    if primary[0] == "":
        # if primary key argument is empty, get all column info from table
        query = "SELECT {} FROM {}".format(columns, tableName)
    else:
        # if primary key argument is filled, get column info based on key
        query = "SELECT {} FROM {} WHERE {}='{}'".format(columns, tableName, primary[0], primary[1])

    # >

    # Execute Query <
    print('\n', "query = ", query)
    cursor.execute(query)
    columnsInfo = list(cursor.fetchall())
    # print("\n", columnsInfo)

    # >

    # Format Output <
    if len(columnsInfo) == 1:
        # if list would only be one element, return just that element
        return dict(zip(columnNames, columnsInfo[0]))
    else:
        # return list of dictionaries
        datalist = list()
        for i in range(len(columnsInfo)):
            datalist.append(dict(zip(columnNames, columnsInfo[i])))
        return datalist

    # >


def childQuery(tableName, columns, primary: tuple, secondary: tuple):
    '''gets information from a table based on double key input'''

    # Declaration <
    columnNames = list()

    # >

    # Column Names <
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(tableName))
    for x in cursor.fetchall(): columnNames.append(x[0])
    # print("column names = ", columnNames)

    # >

    # Build Query <
    query = "SELECT {} FROM {} WHERE {}='{}' AND {}='{}'".format(columns, tableName, primary[0], primary[1], secondary[0], secondary[1])
    print('\n', "query = ", query)

    # >

    # Execute Query <
    cursor.execute(query)
    columnsInfo = list(cursor.fetchall())

    # >

    # Format Output <
    if len(columnsInfo) == 1:
        # if list would only be one element, return just that element
        return dict(zip(columnNames, columnsInfo[0]))
    else:
        # return list of dictionaries
        datalist = list()
        for i in range(len(columnsInfo)):
            datalist.append(dict(zip(columnNames, columnsInfo[i])))
        return datalist

    # >


def joinQuery(table1, table1Alias, table1JoinCol, table2, table2Alias, table2JoinCol, columns, primary: tuple, sort = False):
    '''gets information from two joined tables'''

    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}' OR TABLE_NAME = '{}'".format(table1, table2))
    temp = cursor.fetchall()
    columnNames = list()
    for x in temp:
        columnNames.append(x[0])
    # print(columnNames)

    if primary[0] == "":
        query = "SELECT {} FROM {} {} INNER JOIN {} {} ON {}.{} = {}.{}".format(columns, table1, table1Alias, table2, table2Alias, table1Alias, table1JoinCol, table2Alias, table2JoinCol)
    else:
        query = "SELECT {} FROM {} {} INNER JOIN {} {} ON {}.{} = {}.{} WHERE {}='{}'".format(columns, table1, table1Alias, table2, table2Alias, table1Alias, table1JoinCol, table2Alias, table2JoinCol, primary[0], primary[1])

    print('\n', "query = ", query)
    cursor.execute(query)
    columnsInfo = list(cursor.fetchall())

    if sort:

        columnsInfo.sort(key=lambda x : x.updateTime, reverse=False)
    # print("\n", columnsInfo)

    if len(columnsInfo) == 1:
        return dict(zip(columnNames, columnsInfo[0]))
    else:
        count = 0
        datalist = list()
        while count < 10 and count < len(columnsInfo):
            datalist.append(dict(zip(columnNames, columnsInfo[count])))
            count += 1
        return datalist


def setQuery(tableName, input: list):
    print("\nqueries to be executed\n-----")
    for i in input:
        # Declaration <
        columnList = list(i.keys())
        valueList = list(i.values())
        # >

        # Column Names <
        columnStr = "(" + ", ".join(columnList) + ")"
        # >

        # Values <
        valueStr = "(\'" + "\', \'".join(valueList) + "\')"
        # >

        # Build Query <
        query = "INSERT INTO {} {}\n VALUES {}".format(tableName, columnStr, valueStr)
        print("query = ", query)
        # >

        cursor.execute(query)

