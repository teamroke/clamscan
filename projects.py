
'''
    Small class to hold the properties of a project. Kept it separate to be extendable in the future.
'''


class Project:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory

    def __str__(self):
        return self.name
