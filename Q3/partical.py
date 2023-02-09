import random
import statistics

### Guess format
#  [random x, distance in meters, importance]
# recreate so that partical is the object
class partical:
    def __init__(self, map, x, ):
        self.map = map
        self.mapSizeX = len(map[0])
        self.distribution = []
        self.median = 0
        self.x = x
        
    @staticmethod
    def show_map(map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j], end = "")
            print()
    def first_guess(self, numGuess):
        guesses = []
        for i in range(numGuess):
            guesses.append([random.randrange(0, self.mapSizeX), 0, 0])
        return guesses
    # hide height off the ground
    def find_altitude():
        pass
    # assign a importance weight
    def weight(): 
        pass
    
    def move(self,dX):
        self.x = (self.x + dX)% self.mapSizeX
        

    def fuzz():
        pass

    def __repr__(self):
        return "{} {}".format(self.x, 0)

