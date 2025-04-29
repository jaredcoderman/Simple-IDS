from watchdog.observers import Observer
from classes.watcher import Watcher
import time

def watch_directories(directories):
  observer = Observer()
  event_handler = Watcher()

  for directory in directories:
    observer.schedule(event_handler, path=directory, recursive=True)

  observer.start()
  print(f"Watching directories: {', '.join(directories)}")

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("Stopping watchers...")
  finally:
    observer.stop() 
    observer.join() 

directories_to_watch = ["test_dir1", "test_dir2", "test_dir3"]

watch_directories(directories_to_watch)
