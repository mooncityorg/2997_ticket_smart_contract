from os import path
from json import load


def getJSON(arg: str):
    '''  '''

    directory = path.realpath(__file__)[:-17]
    with open(f'{directory}{arg}', 'r') as file:

        return load(file)
