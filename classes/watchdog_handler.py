from watchdog.events import FileSystemEventHandler
from datetime import datetime
from classes.splunk_logger import log_to_splunk

class WatchdogHandler(FileSystemEventHandler):
    def __init__(self, splunk_logger):
        self.splunk_logger = splunk_logger

    @log_to_splunk
    def on_modified(self, event):
        if event.is_directory:
            return

    @log_to_splunk
    def on_created(self, event):
        if event.is_directory:
            return

    @log_to_splunk
    def on_deleted(self, event):
        if event.is_directory:
            return