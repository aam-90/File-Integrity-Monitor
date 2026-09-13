import os
import json
from config import MONITOR_DIRECTORY, BASELINE_FILE
from monitor.hasher import calculate_sha256


def create_baseline(directory, baseline_file):
    """Create a SHA-256 baseline for all files in a directory."""

    baseline = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            file_hash = calculate_sha256(file_path)

            baseline[file_path] = file_hash

    with open(baseline_file, "w") as file:
        json.dump(baseline, file, indent=4)

    print(f"Baseline created successfully: {baseline_file}")
    print(f"Files recorded: {len(baseline)}")


if __name__ == "__main__":
    create_baseline(
        MONITOR_DIRECTORY,
        BASELINE_FILE
    )