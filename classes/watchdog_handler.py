from watchdog.events import FileSystemEventHandler
from datetime import datetime
from classes.splunk_logger import log_to_splunk
from classes.detection_engine import DetectionEngine

class WatchdogHandler(FileSystemEventHandler):
    def __init__(self, splunk_logger):
        self.splunk_logger = splunk_logger
        self.detector = DetectionEngine()

    # @log_to_splunk
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")

    # @log_to_splunk
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")

    # @log_to_splunk
    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"{datetime.now()} Event: {event.event_type} | File: {event.src_path}")
        
    # @log_to_splunk
    def on_moved(self, event):
        print(f"{event.src_path} moved to -> {event.dest_path}")
        for finding, metadata in self.detector.check_event(event):
            self.splunk_logger.log_event(
                f"SUSPICIOUS: {finding}", 
                metadata=metadata
            )
        if event.is_directory:
            return