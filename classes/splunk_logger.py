import splunklib.client as client
import functools
import json

class SplunkLogger:
  def __init__(self, host="localhost", port=8089, username='jhead', password='hellosplunk123', scheme="https"):
    self.service = client.connect(host=host, port=port, username=username, password=password, scheme=scheme)
    self.index = self.service.indexes['main']

  def log_event(self, message, metadata=None):
    if metadata:
      full_log = {
        "message": message,
        "metadata": metadata
      }
      self.index.submit(json.dumps(full_log))
    else:
      self.index.submit(message)
    print(f"Logged event")

def log_to_splunk(func):
  """
  A decorator to log events to Splunk before calling the original function.
  """
  @functools.wraps(func)
  def wrapper(self, event, *args, **kwargs):
    event_message = f"{func.__name__} event: {event.src_path}"
    self.splunk_logger.log_event(event_message)

    return func(self, event, *args, **kwargs)
  return wrapper