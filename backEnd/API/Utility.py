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


def Authenticate(driver):
    '''  '''

    # Declaration <
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Authenticate']

    # >

    # Select <
    driver.find_element_by_xpath(setting['Select']).click(), sleep(1)

    # >

    return driver


def scrapeUser(driver):
    '''  '''

    pass


def scrapeSchedule(driver):
    '''  '''

    pass
