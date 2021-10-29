from os import path


class Tools:

    def __init__(self):

        self.path = path.realpath(__file__)[:-16]

    def getPath(self):
        '''  '''

        return self.path
