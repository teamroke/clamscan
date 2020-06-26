from watchdog.events import FileSystemEventHandler

'''
    This a custom handler for running clamscan after a file is created or modified.
'''

class ClamHandler(FileSystemEventHandler):

    def __init__(self):
        super.__init__()

    def on_created(self, event):
        print(event.src_path)

    def on_modified(self, event):
        print(event.src_path)
