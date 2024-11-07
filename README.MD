# DualShock 3 Pico Charger

## What?

A simple Raspberry Pi Pico-based device that lets you charge your DualShock 3 controller (Sixaxis should work as well) from any USB power source.

## Why?

- The DualShock 3 requires an USB handshake before it will start to charge.
- If you want to charge while playing, an USB host with the correct driver will connect to the controller instead of just charging it.
- The project only requires a very cheap Raspberry Pi Pico microcontroller and a minimal amount of soldering.

## How?

The Raspberry Pi Pico can use USB devices connected to its GPIO. The basic setup is enough to perform the initial handshake the DS3 needs. As no drivers are initialized, the DS3 will remain connected to its host via Bluetooth while charging.


## Make Your Own

You can use other GPIO pins than the ones pictured, see code for more information.

## Software

- Flash [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) onto the Pi Pico.
- Copy `boot.py` and `code.py` to the CIRCUITPY drive.

## Notes

The device can be hooked up to any 5V power source, either through the Pico's integrated USB port or by hooking up the VBUS and GND pins.

The Pico will go to into deep sleep (unmeasurable on my cheapo USB meter) if no controller is found within 10 seconds from plugging in power, so it can be left plugged into a USB power supply without worrying about phantom drain. Plugging in the controller will trigger communication on the USB pins, triggering the wake up alarm.

The sleep/alarm code is just a personal QoL feature and everything will work without it.

Although this was made with a Pi Pico, any microcontroller with CircuitPython support that can use the libraries in the code should work.
