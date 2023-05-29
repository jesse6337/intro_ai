import machine
#import time
import utime
#import local
#import RPi.GPIO as GPIO
#from RpiMotorLib import RpiMotorLib



Pin = machine.Pin
pins = [Pin(i, Pin.OUT) for i in range(0,3)]
power = 0.5
rotation = [[power,0,0,0],
                    [0,power,0,0],
                    [0,0,power,0],
                    [0,0,0,power]]
#help = wheels.motor
#mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
#mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function , pass the parameters


map = [['r', 'r','g'],
        ['g', 'r','g'],         
        ['r','g','r']]

#postion = local.localize(map)

i2c = machine.I2C(0,
                  scl=machine.Pin(17),
                  sda=machine.Pin(16),
                  freq=400000)

pin = Pin(25, Pin.OUT)
#pins = [Pin(i, Pin.OUT) for i in range(0,3)]

while True:
    #pin.high()
    
    #mymotortest.motor_run(GpioPins , .01, 100, False, False, "half", .05)
    #help.move(power = 0.5) # type: ignore
    for each_stator in rotation:
            for each_pin in range(len(pins)):
                pins[each_pin].value(each_stator)
                utime.sleep(0.001)
