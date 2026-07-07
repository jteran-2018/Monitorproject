"""
led.py
"""

from config import SIMULATION_MODE

if not SIMULATION_MODE:
    from gpiozero import LED

    led = LED(18)


def turn_on():

    if SIMULATION_MODE:
        print("[LED] ON")
    else:
        led.on()


def turn_off():

    if SIMULATION_MODE:
        print("[LED] OFF")
    else:
        led.off()