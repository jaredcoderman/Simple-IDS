from watchdog.observers import Observer
from classes.watchdog_handler import WatchdogHandler
import time
from classes.splunk_logger import SplunkLogger

def watch_directories(directories):
  
  splunk_logger = SplunkLogger()

  observer = Observer()
  event_handler = WatchdogHandler(splunk_logger=splunk_logger)

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
