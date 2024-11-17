# Baptistry Ready Button

This is for a momentary button which is connected to a [Pico Pi](https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico) in order to send a GET request to the [Bitfocus Companion](https://bitfocus.io/companion) API.

## Using the Script

### MicroPython

- Make sure MicroPython is installed on the Pico Pi. Instructions: [raspberrypi.org](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/1) and the subsequent pages.

- Customize the `page`, `row`, and `column` variables in the `main.py` to the appropriate values for the desired button in Companion.

- Load `main.py` onto the Pi.

### Wiring

- The button should be connected to GPIO pins 1 and 3 (ground).

- The LED should be connected to GPIO pins 4 and 8 (ground).

### How It Works

The script runs in a continuous loop.
When you press the button, the LED should turn on and the GET command sent to the Companion instance on your network.
When you press the button again the LED turns off.

(I haven't tested this yet, so hopefully it works. I could set the LED on a timer to turn off after 30 seconds or something.)
