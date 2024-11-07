import time
import alarm
import board
import usb.core
import usb_host
import microcontroller

microcontroller.cpu.frequency = 120000000
# change D+/D- pins if needed, D- needs to be the next pin after D+
usb_host.Port(board.GP0, board.GP1)
i = 0

while True:
    # Check if device is connected
    con = usb.core.find()

    # If any device is found, do nothing; the DS3 will now charge
    if con != None:
        time.sleep(5)
        i = 0

    # If no device is found for 10 seconds, go to sleep. The USB D+ pin will act as a wake-up trigger
    if i > 20:
        # change to the D+ pin if not using default USB pins
        # the Pico won't properly go to sleep if the D+ pin isn't pulled down beforehand
        pin_alarm = alarm.pin.PinAlarm(pin=board.GP0, value=True, pull=True)
        alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

    time.sleep(0.5)
    i = i + 1
