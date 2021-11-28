# Import <
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


def Submit(password: str) -> bool:
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


def Verify(username: str, password: str) -> bool:
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
    except NoSuchElementException:

        driver.quit()
        return None

    # >


def Authenticate(driver, code = None):
    '''  '''

    # Declaration <
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Authenticate']

    # >

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


def scrapeSchedule(driver):
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

    return (driver, {'schedule' : schedule})
