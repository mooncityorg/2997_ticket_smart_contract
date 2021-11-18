# Import <
from os import path
from json import load
from dash import Dash
from time import sleep
from time import strftime
from string import punctuation
from selenium.common.exceptions import NoSuchElementException

# >

# Declaration <
application = Dash(suppress_callback_exceptions = True)
server = application.server

# >


def getJSON(file: str) -> dict:
    '''  '''

    directory = ('/'.join(path.realpath(__file__).split('/')[:-3]))
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)


def Login(driver, username: str, password: str):
    '''  '''

    # Check Password <
    hasUpper, hasDigit, hasPunctuation = False, False, False
    for c in password:

        if (c.isupper()): hasUpper = True
        if (c.isdigit()): hasDigit = True
        if (c in punctuation): hasPunctuation = True

    # >

    # if (valid) <
    if (hasUpper and hasDigit and hasPunctuation):

        # Declaration <
        username += '@umsystem.edu'
        setting = getJSON(file = '/backEnd/Resource/Utility.json')['Login']

        # >

        # Website <
        driver.get(setting['Website']), sleep(1)
        driver.find_element_by_xpath(setting['websiteClick']).click(), sleep(1)

        # >

        # try (if valid) <
        try:

            # Username <
            driver.find_element_by_xpath(setting['Username']).send_keys(username), sleep(1)
            driver.find_element_by_xpath(setting['usernameClick']).click(), sleep(1)

            # >

            # Passowrd <
            driver.find_element_by_xpath(setting['Password']).send_keys(password), sleep(1)
            driver.find_element_by_xpath(setting['passwordClick']).click(), sleep(1)

            # >

            return driver

        # >

        # except (then invalid) <
        except NoSuchElementException: return None

        # >

    # >

    # else (invalid) <
    else: return None

    # >


def Verify(driver, code: str):
    '''  '''

    # Declaration <
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Verify']

    # >

    # try (if valid) <
    try:

        # Select <
        driver.find_element_by_xpath(setting['Select']).click(), sleep(1)

        # >

        # Code <
        driver.find_element_by_xpath(setting['codeInput']).send_keys(code), sleep(1)
        driver.find_element_by_xpath(setting['codeClick']).click(), sleep(1)

        # >

        # Student Center <
        driver.find_element_by_xpath(setting['studentCenter']).click(), sleep(1)

        # >

        return driver

    # >

    # except (then invalid) <
    except NoSuchElementException: return None

    # >


def scrapeUser(driver):
    '''  '''

    # Declaration <
    schedule, isTutor = [], False
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['scrapeUser']

    # >

    # get Name <
    driver.get(setting['nameWebsite']), sleep(1)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    name = driver.find_element_by_xpath(setting['Name']).text

    # >

    # get Tutor <
    driver.get(setting['tutorWebsite']), sleep(1)

    # >

    # iterate (course) <
    for i in range(25):

        # try (if valid) <
        try:

            course = driver.find_element_by_xpath(setting['Title'].replace('<>', str(i))).text
            schedule.append(course)
            isTutor = True

        # >

        # except (then invalid) <
        except NoSuchElementException: pass

        # >

    # >

    return {'name' : name, 'isTutor' : isTutor, 'schedule' : schedule}


def scrapeCourse(driver):
    '''  '''

    # Declaration <
    schedule = []
    month, year = strftime('%m %Y').split()
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['scrapeCourse']
    semester = [key for key, value in setting['Semester'].items() if (month in value)][0]

    # >

    # Website <
    driver.get(setting['Website']), sleep(1)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

    # >

    # Select <
    for i in range(50):

        # try (if valid) <
        try:

            termA = f'{year} {semester} Semester'
            termB = driver.find_element_by_xpath(setting['Term'].replace('<>', str(i))).text

            # if (match) <
            if (termA == termB):

                driver.find_element_by_xpath(setting['Button'].replace('<>', str(i))).click()
                driver.find_element_by_xpath(setting['Continue']).click(), sleep(1)

            # >

        # >

        # except (then invalid) <
        except NoSuchElementException: pass

        # >

    # >

    # Filter Schedule <
    driver.find_element_by_xpath(setting['Dropped']).click()
    driver.find_element_by_xpath(setting['Waitlisted']).click()
    driver.find_element_by_xpath(setting['Filter']).click()

    # >

    # iterate (course) <
    for i in range(0, 50, 2):

        # try (if valid) <<
        try:

            course = {}
            for k, v in setting['Course'].items():

                course[k] = driver.find_element_by_xpath(v.replace('<>', str(i))).text

            schedule.append(course)

        # >

        # except (then invalid) <
        except NoSuchElementException: pass

        # >

    # >

    return schedule
