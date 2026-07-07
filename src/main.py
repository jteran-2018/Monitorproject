"""
main.py

Main entry point for the Wildlife Motion Detection System.
"""

from sensor import wait_for_motion
from led import turn_on, turn_off
from logger import log_event
from pdf_report import generate_report


def main():
    print("=" * 40)
    print(" Wildlife Motion Detection System")
    print("=" * 40)

    print("\nSystem initialized.")
    print("Waiting for motion...\n")

    while True:
        wait_for_motion()

        turn_on()

        log_event()

        generate_report()

        print("Processing motion event...\n")

        turn_off()

        print("Waiting for motion...\n")


if __name__ == "__main__":
    main()