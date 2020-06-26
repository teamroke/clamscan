from watchdog.observers import Observer
from clamhandler import ClamHandler
from configloader import ConfigLoader

config = ConfigLoader()
event_handler = ClamHandler(config.scanner)
observer = Observer()
observers = []
for project_dir in config.list_project_dirs():
    observer.schedule(event_handler, project_dir)
    observers.append(observer)

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.unschedule_all()
    observer.stop()

observer.join()
