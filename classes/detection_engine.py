from rules.rename_to_exe import RenameToExeRule

class DetectionEngine:
  def __init__(self):
    self.rules = [RenameToExeRule()]

  def check_event(self, event):
    findings = []
    for rule in self.rules:
      result = rule.check(event=event)
      if result:
        findings.append(result)
    return findings