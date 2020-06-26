from os import path, getcwd, listdir
import json
from projects import Project


'''
    This will load the config.json file and read in the values.
    It will only read on load so any changes will need a restart to be picked up.
'''


class ConfigLoader:

    def __init__(self):
        self.config_file = path.join(getcwd(), 'config.json')
        self.projects = []
        try:
            with open(self.config_file) as configuration:
                config = json.load(configuration)
            self.base_path = config['base_config']['base_project_dir']
            self.scanner = config['base_config']['clamscan_location']
            for project in config['projects']:
                self.projects.append(Project(project['name'], path.join(self.base_path, project['dir'])))
        except OSError():
            print(f'Cannot open the configuration file')

    def list_config(self):
        print(self.base_path)
        print(self.scanner)
        for project in self.projects:
            print(project.name)
            print(listdir(project.directory))

    def list_project_dirs(self):
        for project in self.projects:
            yield project.directory



