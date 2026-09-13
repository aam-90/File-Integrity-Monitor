"""
File Integrity Monitor

Monitors files using SHA-256 hashes and detects
created, modified, and deleted files.
"""



import json
VERSION = "1.0.0"

from config import (
    MONITOR_DIRECTORY,
    BASELINE_FILE,
    JSON_REPORT,
    CSV_REPORT
)

from monitor.baseline import create_baseline
from monitor.checker import check_integrity
from monitor.reporter import (
    generate_alerts,
    display_alerts,
    save_json,
    save_csv
)


def main():
    print(f"=== File Integrity Monitor v{VERSION} ===")

    # Create baseline if it does not exist
    try:
        with open(BASELINE_FILE, "r") as file:
            baseline = json.load(file)

        print("Existing baseline loaded.")

    except FileNotFoundError:
        print("No baseline found. Creating a new baseline...")

        create_baseline(
            MONITOR_DIRECTORY,
            BASELINE_FILE
        )

        with open(BASELINE_FILE, "r") as file:
            baseline = json.load(file)

    # Check file integrity
    modified, deleted, created = check_integrity(
        MONITOR_DIRECTORY,
        baseline
    )

    # Generate alerts
    alerts = generate_alerts(
        modified,
        deleted,
        created
    )

    # Display alerts
    display_alerts(alerts)

    # Save reports
    save_json(alerts, JSON_REPORT)
    save_csv(alerts, CSV_REPORT)

    print("\nIntegrity check completed.")


if __name__ == "__main__":
    main()