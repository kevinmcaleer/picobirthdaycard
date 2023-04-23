from machine import Pin
from time import sleep
touch = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    if touch.value() == 0:
        print('not Touched!')
    else:
        print('touched!')
    sleep(0.1)