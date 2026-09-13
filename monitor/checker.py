import os

from monitor.hasher import calculate_sha256

from monitor.reporter import (
    generate_alerts,
    display_alerts,
    save_json,
    save_csv
)
from config import (
    MONITOR_DIRECTORY,
    BASELINE_FILE,
    JSON_REPORT,
    CSV_REPORT
)

def check_integrity(directory, baseline):
    """Compare current files against the saved baseline."""

    current_files = {}

    # Calculate hashes for current files
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Don't scan the baseline itself if it is inside the directory
            file_hash = calculate_sha256(file_path)
            current_files[file_path] = file_hash

    modified = []
    deleted = []
    created = []

    # Check for modified or deleted files
    for file_path, old_hash in baseline.items():

        if file_path not in current_files:
            deleted.append(file_path)

        elif current_files[file_path] != old_hash:
            modified.append(file_path)

    # Check for newly created files
    for file_path in current_files:

        if file_path not in baseline:
            created.append(file_path)

    return modified, deleted, created


if __name__ == "__main__":
    import json

    with open(BASELINE_FILE, "r") as file:
        baseline = json.load(file)

    modified, deleted, created = check_integrity(
        MONITOR_DIRECTORY,
        baseline
    )

    print("\n=== Integrity Check ===")

    print("\nModified files:")
    for file in modified:
        print("  ", file)

    print("\nDeleted files:")
    for file in deleted:
        print("  ", file)

    print("\nCreated files:")
    for file in created:
        print("  ", file)    

if __name__ == "__main__":
    
    import json

    from monitor.reporter import generate_alerts, display_alerts

    with open("baseline.json", "r") as file:
        baseline = json.load(file)

    modified, deleted, created = check_integrity(
        "test_data",
        baseline
    )

    alerts = generate_alerts(
        modified,
        deleted,
        created
    )

    display_alerts(alerts)

    save_json(alerts, JSON_REPORT)
    save_csv(alerts, CSV_REPORT)