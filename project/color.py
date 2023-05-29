#import RPi.GPIO as GPIO
import machine 
import time


pin = machine.Pin
s2 = 3
s3 = 2
signal = 4
NUM_CYCLES = 10
ps2 = pin(s2, pin.OUT)
ps3 = pin(s3, pin.OUT)
pSignal = pin(signal, pin.IN, pin.PULL_UP)


def setup():    
   print("\n")
  
def dud():
      pass
def loop():
  temp = 1
  while(1):  
    ps2.low
    ps3.low
    
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      pSignal.irq(handler = dud,trigger= pin.IRQ_FALLING)

    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    print("red value - ",red)

    ps2.low
    ps3.high
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      pSignal.irq(handler = dud,trigger= pin.IRQ_FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    ps2.high
    ps3.high
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      pSignal.irq(handler = dud,trigger= pin.IRQ_FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)
    time.sleep(2)  


def endprogram():
    #GPIO.cleanup()
    pass
  
while True:
      loop()
#if __name__=='__main__':
    
 #   setup()

  #  try:
   #     loop()

    #except KeyboardInterrupt:
     #   endprogram()