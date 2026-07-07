"""
logger.py

Handles saving motion detection events to a CSV file.
"""

import csv
import os
from datetime import datetime


from config import LOG_FILE

def log_event():
    """
    Saves one motion detection event to the CSV file.
    """

    # Current date and time
    now = datetime.now()

    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%I:%M:%S %p")

    # Create the logs folder/file if it doesn't exist
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        # Write header only once
        if not file_exists:
            writer.writerow(["Detection", "Date", "Time"])

        # Count previous detections
        detection_number = 1

        if file_exists:
            with open(LOG_FILE, "r") as f:
                detection_number = sum(1 for line in f)

        writer.writerow([detection_number, date, time])

    print("[LOGGER] Event saved.")