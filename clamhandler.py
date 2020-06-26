from watchdog.events import FileSystemEventHandler
import subprocess

'''
    This a custom handler for running clamscan after a file is created or modified.
'''


class ClamHandler(FileSystemEventHandler):

    def __init__(self, clamscan_location):
        super.__init__()
        self.clamscan_location = clamscan_location

    def on_created(self, event):
        proc = subprocess.Popen(self.clamscan_location, stdout=subprocess.PIPE)
        output = proc.communicate()
        print(output)

    def on_modified(self, event):
        proc = subprocess.Popen(self.clamscan_location, stdout=subprocess.PIPE)
        output = proc.communicate()
        print(output)
