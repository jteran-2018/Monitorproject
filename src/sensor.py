"""
sensor.py
"""

from config import SIMULATION_MODE

if not SIMULATION_MODE:
    from gpiozero import MotionSensor

    pir = MotionSensor(17)


def wait_for_motion():

    if SIMULATION_MODE:

        input("Press ENTER to simulate motion...")

        print("[SENSOR] Motion detected!")

    else:

        pir.wait_for_motion()

        print("[SENSOR] Motion detected!")