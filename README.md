# 🛡️ Filesystem Event Monitor with Suspicious Behavior Detection

This project is a lightweight detection system that monitors file changes in real time and flags suspicious behavior — such as renamed executables and unauthorized file drops — then logs those events to **Splunk** in structured JSON format.

It simulates some techniques used by real malware (e.g., Emotet or ransomware), and is designed with modularity, scalability, and security awareness in mind.

> 🎯 Built to demonstrate endpoint-style detection logic inspired by tools like CrowdStrike Falcon.

---

## 🔍 Features

- ✅ Real-time directory monitoring using `watchdog`
- ✅ Modular `DetectionEngine` with plug-and-play rules
- ✅ Rules detect:
  - Renaming to `.exe` from non-executable types
  - (More rules easily added)
- ✅ Structured JSON logs sent to **Splunk**
- ✅ Metadata included: source path, destination path, rule name, severity, timestamp
- ✅ Comes with a safe **attack simulation script** to demo detections

---

## 🎥 Demo

> 🕒 Duration: 3m 42s  
> 🔗 [https://youtu.be/qe-RiYsNDZ4]

The demo walks through:
1. The system architecture
2. Key code structure for clean detection
3. Simulated attack (`invoice.pdf` → `invoice.pdf.exe` → moved to `Startup`)
4. Detection printed in terminal
5. Structured event logs shown in Splunk

---

## 🧠 Architecture

```text
[ FileSystem Events (Watchdog) ]
               ↓
     [ DetectionEngine ]
               ↓
    [ Rule 1 | Rule 2 | ... ]
               ↓
     [ Structured Splunk Log ]
```
## 📦 Requirements
Python 3.9+

watchdog

splunklib

Access to a running Splunk instance (tested on Splunk Enterprise)

## 📌 Why This Project?
I’m currently pursuing a career in cybersecurity with a focus on detection engineering. This project demonstrates:

Clean Python architecture

Real-world security use cases

Knowledge of malware behavior patterns

Experience with Splunk integration and log analysis

## 📫 Contact
Jared Head
Email: [jaredheadd@gmail.com]
LinkedIn: [https://www.linkedin.com/in/jared-c-head/]
