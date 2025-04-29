from watchdog.events import FileSystemEventHandler
from datetime import datetime

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")