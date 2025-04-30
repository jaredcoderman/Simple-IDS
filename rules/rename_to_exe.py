import os

class RenameToExeRule:
  def check(self, event):
    if hasattr(event, "dest_path"):
      old_ext = os.path.splitext(event.src_path)[1].lower()
      new_ext = os.path.splitext(event.dest_path)[1].lower()
      if old_ext != ".exe" and new_ext == ".exe":
        metadata = {
          "src_path": event.src_path,
          "dest_path": event.dest_path,
          "rule": "RenameToExe",
          "severity": "medium"
        }
        return "file renamed to .exe from a non-executable type", metadata
    return None