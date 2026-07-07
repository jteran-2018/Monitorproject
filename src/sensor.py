"""
sensor.py

Simulates a PIR motion sensor during development.
Later, this file will use the Raspberry Pi GPIO pins.
"""


def wait_for_motion():
    """
    Wait for the user to press Enter to simulate motion.
    """

    input("Press ENTER to simulate motion...")

    print("[SENSOR] Motion detected!")