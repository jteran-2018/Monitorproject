"""
main.py

Main entry point for the Wildlife Motion Detection System.
"""

from datetime import datetime

from sensor import wait_for_motion
from led import turn_on, turn_off
from logger import log_event
from pdf_report import generate_report


def main():

    session_start = datetime.now()

    motion_count = 0

    last_detection = "None"

    print("=" * 45)
    print(" Wildlife Motion Detection System")
    print("=" * 45)

    print("\nSystem initialized.")
    print("Monitoring for motion...\n")

    try:

        while True:

            wait_for_motion()

            motion_count += 1

            runtime = datetime.now() - session_start

            session_duration = str(runtime).split(".")[0]

            last_detection = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

            turn_on()

            log_event(session_duration)

            generate_report()

            print("\n========== Motion Detected ==========")
            print(f"Motion Event #: {motion_count}")
            print(f"Last Detection: {last_detection}")
            print(f"Session Time : {session_duration}")
            print("CSV Updated")
            print("PDF Updated")
            print("=====================================\n")

            turn_off()

            print("Waiting for motion...\n")

    except KeyboardInterrupt:

        runtime = datetime.now() - session_start

        print("\n=====================================")
        print(" Session Summary")
        print("=====================================")
        print(f"Program Runtime : {runtime}")
        print(f"Motion Events   : {motion_count}")
        print("CSV Log         : logs/motion_log.csv")
        print("PDF Report      : reports/motion_report.pdf")
        print("Program terminated successfully.")
        print("=====================================")


if __name__ == "__main__":
    main()