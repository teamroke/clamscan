
class Project:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory

    def __str__(self):
        return self.name
