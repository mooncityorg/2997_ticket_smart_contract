from os import path
from json import load

class Tool:

    def __init__(self):

        self.path = path.realpath(__file__)[:-17]


    def getJSON(self, file: str):
        '''  '''

        with open(f'{path}{file}', 'r') as fileVariable:

            return load(fileVariable)


