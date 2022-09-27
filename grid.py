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
def prob_of_belief(sensor, worldP, beliefP):
    cSenorReading = sensor
    world_ = worldP
    belief_ = beliefP
    # top half of Bayes formula
    for i in range(len(world_)):
        if sensor == world_[i]:
            belief_[i] *= 0.9 
        elif sensor != world_[i]:
            belief_[i] *= 0.1 
    sum = 0 
    #find bottom half of Bayes formula
    for i in belief_:
        sum += i
    #complete Bayes Formula
    for i in range(len(belief_)):
        belief_[i] /= sum
    return belief_
def find_highst_prob_indexs(list): # returns list of the indexs w/ the highest prob
    pI = 0
    highest = 0
    highestI = []
    for i in range(len(list)):
        if list[i] > highest:
            highest = list[i]
            highestI.append(i)
        elif list[i] == highest:
            highestI.append(i)
    return highestI
#robot makes sence of envirment
#sensing green is the same as not sensing red

#upade prob belief of robot's position in the world(map)
belief =prob_of_belief(currentSenorReading, world, belief)
print(wLen)
print(find_highst_prob_indexs(belief))
print(belief)
