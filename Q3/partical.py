import random
### Guess format
#  [random x, random y, distance in meters, importance]
class partical:
    def __init__(self, mapSize):
        self.mapSizeX = mapSize[0]
        self.mapSizeY = mapSize[1]
    def first_guess(self, numGuess):
        guesses = []
        for i in range(numGuess):
            guesses.append([random.randrange(0, self.mapSizeX), random.randrange(0, self.mapSizeY),0, 0])
        return guesses
    def sense(reading, guess, error = 1):
        for i in range(guess):
            guess[i][3] = -abs(guess[i][2]-reading)
