from machine import Pin

class motor:
    def __init__(self):
        self.pins = [Pin(i, Pin.OUT) for i in range(0,3)]
    def move(self, power):
        rotation = [[power,0,0,0],
                    [0,power,0,0],
                    [0,0,power,0],
                    [0,0,0,power]]
        for each_stator in rotation:
            for each_pin in self.pins:
                #self.pins[each_stator].value(ea)
                pass
