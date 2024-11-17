from machine import Pin
import time
import request

button = Pin(0, Pin.IN, Pin.OUT)
led = Pin(2, Pin.OUT)

# http request

# companion IP and port
companion = "127.0.0.1:8000"

# location of button to press
page = 1
row = 1
column = 1

req = f"{companion}/api/location/{page}/{row}/{column}/press"

state = 0

if __name__ == "main":
    while True:
        if button.value() == 0:
            # check if the LED is off
            if state == 0:
                # if it is off, turn if on
                led.value(1)

                # send the HTTP request to Companion
                request.get(req)

                while button.value() == 0:
                    # update the state of the LED
                    state = 1

            else:
                # if the LED is on, turn it off
                led.value(0)

                while button.value() == 0:
                    state = 0

        time.sleep(0.01)
