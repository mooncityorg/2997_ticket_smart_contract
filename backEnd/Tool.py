from os import path
from json import load
from dash import Dash


application = Dash(suppress_callback_exceptions = True)
server = application.server


def getJSON(file: str) -> dict:
    '''  '''

    directory = path.realpath(__file__)[:-16]
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)
