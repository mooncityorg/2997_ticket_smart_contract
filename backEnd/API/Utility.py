# Import <
from os import path
from json import load
from dash import Dash
from time import sleep
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
        try:

            driver.find_element_by_xpath(setting['Select']).click(), sleep(1)

        except NoSuchElementException: pass

        # >

        # Code <
        driver.find_element_by_xpath(setting['codeInput']).send_keys(code), sleep(1)
        driver.find_element_by_xpath(setting['codeClick']).click(), sleep(1)
        driver.find_element_by_xpath(setting['pathwayCheck'])

        # >

        return driver

    # >

    # except (then invalid) <
    except NoSuchElementException: return None

    # >
