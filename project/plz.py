import GPIOSimulator as GPIO
from EmulatorGUI import GPIO


BTN_PIN = 1 # Pin number of button
LED_PIN = 2 # Pin number of LED

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(BTN_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    if GPIO.input(BTN_PIN) == 0 : GPIO.output(LED_PIN, 0)
    else                        : GPIO.output(LED_PIN, 1)