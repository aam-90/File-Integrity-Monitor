# File Integrity Monitor

## Description

The File Integrity Monitor is a Python-based cybersecurity tool that monitors files for unexpected changes.  
It uses SHA-256 cryptographic hashing to create a secure baseline of the monitored files.  
When the monitor runs, it calculates the current hash of each file and compares it with the stored baseline.  
If the hash changes, the file is detected as **MODIFIED** and a high-severity alert is generated.  
Files that disappear from the directory are detected as **DELETED**, while newly added files are detected as **CREATED**.  
Each detected change is recorded with a timestamp, file path, event type, severity, and reason.  
The alerts are displayed in the terminal and exported as **JSON and CSV reports**.

## Project Structure

```text
file-integrity-monitor/
│
├── main.py
│   --> Main program entry point
│
├── config.py
│   --> Stores project configuration
│
├── baseline.json
│   --> Stores the original SHA-256 hashes
│
├── monitor/
│   ├── __init__.py
│   │   --> Makes monitor a Python package
│   │
│   ├── hasher.py
│   │   --> Calculates SHA-256 file hashes
│   │
│   ├── baseline.py
│   │   --> Creates the file integrity baseline
│   │
│   ├── checker.py
│   │   --> Compares current files with the baseline
│   │
│   └── reporter.py
│       --> Generates and saves security alerts
│
├── test_data/
│   └── sample.txt
│       --> Test file monitored by the tool
│
├── reports/
│   ├── alerts.json
│   │   --> JSON security alert report
│   │
│   └── alerts.csv
│       --> CSV security alert report
│
└── README.md
    --> Project documentation

```

## Outputs

### Modified File

```text
[ALERT]
Timestamp : 2026-09-13 11:30:00
File      : test_data\sample.txt
Event     : MODIFIED
Severity  : HIGH
Reason    : SHA-256 hash does not match the baseline
```

### Created File

```text
[ALERT]
Timestamp : 2026-09-13 11:30:00
File      : test_data\new_file.txt
Event     : CREATED
Severity  : MEDIUM
Reason    : New file was not present in the original baseline
```

### Deleted File

```text
[ALERT]
Timestamp : 2026-09-13 11:30:00
File      : test_data\sample.txt
Event     : DELETED
Severity  : HIGH
Reason    : File exists in the baseline but is no longer present
```
