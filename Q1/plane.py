from matplotlib import pyplot as plt
#possible possitions
map = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#sensor accuratcy 
# completely acc
sensorAcc1 = 0.7
# off by exactly +- 100ft
sensorAcc2 = 0.2
# off by exactly +- 200ft or more
sensorAcc3 = 0.1
#what sensor read
currentSensorReading = 400
#funtion to find pron
def findProb(world, sReading):
    #create belief list 
    belief = [1/len(world) for i in range(len(world))]
    #iterate through all indexes and multiplying by the acc
    for i in range(len(belief)):
        if world[i] == sReading:
            belief[i] *= sensorAcc1
        elif world[i] == sReading + 100 or world[i] == sReading -100:
            belief[i] *= sensorAcc2
        else:belief[i] *= sensorAcc3
    # create normalizer
    normalizer = sum(belief)
    # complete bayes rule equation
    for i in range(len(belief)):
        belief[i] /= normalizer
    return belief
# call function
probDistribution1 = findProb(map,currentSensorReading)
probDistribution2 = findProb(map,500)
x_values = [i for i in range(len(probDistribution1))]
print(probDistribution1)
print("")
print(probDistribution2)
plt.plot(x_values, probDistribution1)
plt.show()