from secrets import randbelow


world = ['r','g','r','g','g']
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
    #find bottom half of Bayes formula (normalizer)
    for i in belief_:
        sum += i
    #complete Bayes Formula
    for i in range(len(belief_)):
        belief_[i] =belief[i] /sum
        round(belief[i],3)
        
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
def move(map, belief, movement = 2):
    newBelief = [0 for i in range(len(map))]
    for i in range(len(map)):
        #movement for accurate movement
        newiAC = (i + movement) % len(belief)
        #movement for under shoot
        newiUN = (i + movement-1) % len(belief)
        #movement for over shoot
        newiON = (i + movement+1) % len(belief)
        # new belief after moving assuming 80% accuracy 
        newBelief[newiAC] += (belief[i] *0.8)
        # belief update overshoot
        newBelief[newiON] += (belief[i] *0.1)
        # belief update undershoot
        newBelief[newiUN] += (belief[i] *0.1)
    return newBelief

belief = prob_of_belief('g', world, belief)
newBelief = move(world, belief)
print(belief)
print(newBelief)