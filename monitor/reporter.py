from datetime import datetime
import json
import csv
import os

def generate_alerts(modified, deleted, created):
    """Generate readable security alerts."""

    alerts = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for file_path in modified:
        alerts.append({
            "timestamp": timestamp,
            "file": file_path,
            "event": "MODIFIED",
            "severity": "HIGH",
            "reason": "SHA-256 hash does not match the baseline"
        })

    for file_path in deleted:
        alerts.append({
            "timestamp": timestamp,
            "file": file_path,
            "event": "DELETED",
            "severity": "HIGH",
            "reason": "File exists in the baseline but is no longer present"
        })

    for file_path in created:
        alerts.append({
            "timestamp": timestamp,
            "file": file_path,
            "event": "CREATED",
            "severity": "MEDIUM",
            "reason": "New file was not present in the original baseline"
        })

    return alerts


def display_alerts(alerts):
    """Display alerts in a readable format."""

    print("\n=== Security Alerts ===")

    if not alerts:
        print("No file changes detected.")
        return

    for alert in alerts:
        print("\n[ALERT]")
        print(f"Timestamp : {alert['timestamp']}")
        print(f"File      : {alert['file']}")
        print(f"Event     : {alert['event']}")
        print(f"Severity  : {alert['severity']}")
       
        print(f"Reason    : {alert['reason']}")


def save_json(alerts, file_path):
    """Save alerts to a JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(alerts, file, indent=4)

    print(f"JSON report saved: {file_path}")


def save_csv(alerts, file_path):
    """Save alerts to a CSV file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    fieldnames = [
        "timestamp",
        "file",
        "event",
        "severity",
        "reason"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(alerts)

    print(f"CSV report saved: {file_path}")        