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

#robot makes sence of envirment
#sensing green is the same as not sensing red
currentSenorReading = 'g'

#upade prob belief of robot's position in the world(map)
print(wLen)
print(belief)
#dsa