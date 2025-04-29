import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
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

    def on_moved(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | From: {event.src_path} | To: {event.dest_path}")

def watch_directory(directory):
  observer = Observer()
  event_handler = Watcher()
  observer.schedule(event_handler, path=directory, recursive=True)
  observer.start()
  print(f"Watching directory: /{directory}")

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

directories_to_watch = ["test_dir1", "test_dir2", "test_dir3"]
threads = []
for directory in directories_to_watch:
  thread = threading.Thread(target=watch_directory, args=(directory,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()
