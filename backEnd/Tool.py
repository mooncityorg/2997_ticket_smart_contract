from os import path
from json import load


def getJSON(file: str) -> dict:
    '''  '''

    directory = path.realpath(__file__)[:-16]
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)
