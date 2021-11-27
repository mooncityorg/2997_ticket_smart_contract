# Import <
from os import path
from json import load
from dash import Dash
from time import sleep
from time import strftime
from string import punctuation
import dash_bootstrap_components as dbc
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

    try:

        hasUpper, hasDigit, hasPunctuation = False, False, False
        for c in password:

            if (c.isupper()): hasUpper = True
            if (c.isdigit()): hasDigit = True
            if (c in punctuation): hasPunctuation = True

        if (hasUpper and hasDigit and hasPunctuation): return True
        else: return False

    except TypeError: return False
