#Sensor sences red or no red
#sensor is 90% accrurate
#grids are red or green


print("Hello World")

world = ['r','g','g','r','g']
#comprehension
wLen = 1/len(world)
belief = [wLen for i in range(len(world))]
# Intial prob belief of robot being in any position on the map 
# (descrete uniform distrobution)
currentSenorReading = 'g'
def prob_of_belief(sensor, world, belief):
    cSenorReading = sensor
    world = world
    belief = belief
    for i in range(len(world)):
        if currentSenorReading == world[i]:
            belief[i] *= 0.9 
        elif currentSenorReading != world[i]:
            belief[i] *= 0.1 
    sum = 0 
    for i in belief:
        sum += i
    for i in range(len(belief)):
        belief[i] /= sum
#robot makes sence of envirment
#sensing green is the same as not sensing red

#upade prob belief of robot's position in the world(map)
prob_of_belief(currentSenorReading, world, belief)
print(wLen)
print(belief)
