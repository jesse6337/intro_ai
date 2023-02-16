from machine import Pin
import time
import local

map = [['r', 'r','g'],
        ['g', 'r','g'],
        ['r','g','r']]

postion = local.localize(map)

pin = Pin(25, Pin.OUT)
pins = [Pin(i, Pin.OUT) for i in range(0,3)]

while True:
    pin.toggle()
    time.sleep_ms(1000)