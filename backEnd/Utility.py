# Import <
from os import path
from json import load
from dash import Dash
from time import sleep
from string import punctuation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# >


# Declaration <
application = Dash(suppress_callback_exceptions = True)
server = application.server

# >


def getJSON(file: str) -> dict:
    '''  '''

    directory = ('/'.join(path.realpath(__file__).split('/')[:-2]))
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)


def Login(username: str, password: str):
    '''  '''

    # Password Validation <
    hasUpper, hasDigit, hasPunctuation = False, False, False
    for c in password:

        if (c.isupper()): hasUpper = True
        if (c.isdigit()): hasDigit = True
        if (c in punctuation): hasPunctuation = True

    # >

    # if (passing) <
    if (hasUpper and hasDigit and hasPunctuation):

        # Declaration <
        #options = Options()
        #options.headless = True
        setting = getJSON(file = '/backEnd/Resource/Utility.json')['Login']
        driver = webdriver.Chrome(ChromeDriverManager().install())#, options = options)

        # >

        # Website <
        driver.get(setting['Website']), sleep(1)
        driver.find_element_by_xpath(setting['websiteClick']).click(), sleep(1)

        # >

        # try (passing) <
        try:

            # Username <
            username += '@umsystem.edu'
            driver.find_element_by_xpath(setting['Username']).send_keys(username), sleep(1)
            driver.find_element_by_xpath(setting['usernameClick']).click(), sleep(1)

            # >

            # Password <
            driver.find_element_by_xpath(setting['Password']).send_keys(password), sleep(1)
            driver.find_element_by_xpath(setting['passwordClick']).click(), sleep(1)

            # >

            # Select <
            driver.find_element_by_xpath(setting['Select']).click(), sleep(1)

            # >

            return (driver, True)

        # >

        # except (not passing) <
        except:

            return (None, False)

        # >

    # >

    # else (not passing)
    else:

        return (None, False)

    # >


def Verify(username: str, password: str, code: str):
    '''  '''

    # Declaration <
    driver, status = Login(username, password)
    setting = getJSON(file = '/backEnd/Resource/Utility.json')['Verify']

    # >

    # if (passing) <
    try:

        # Code <
        driver.find_element_by_xpath(setting['codeInput']).send_keys(code), sleep(1)
        driver.find_element_by_xpath(setting['codeClick']).click(), sleep(1)
        driver.find_element_by_xpath(setting[''])

        # >

        return (driver, True)

    # >

    # except(not passing) <
    except:

        return (None, False)

    # >
