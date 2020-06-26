from watchdog.events import FileSystemEventHandler


class ClamHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event.src_path)

    def on_modified(self, event):
        print(event.src_path)
