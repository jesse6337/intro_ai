map = [100,200,300,400,500,600,700,800,900,1000]
belief = [1/len(map) for i in range(len(map))]

#funtion to find pron
def findProb(world, sReading, belief, ac = 0.93, over1 = 0.05, over2 = 0.02):
    #create belief list 
    #iterate through all indexes and multiplying by the acc
    for i in range(len(belief)):
        if world[i] == sReading:
            belief[i] *= ac
        elif world[i] == sReading + 100 or world[i] == sReading -100:
            belief[i] *= over1
        else:belief[i] *= over2
    # create normalizer
    normalizer = sum(belief)
    # complete bayes rule equation
    for i in range(len(belief)):
        belief[i] /= normalizer
    belief = [round(belief[i], 3) for i in range(len(belief))]
    return belief
def move(map, belief, movement, pU = 0.04, pA = 0.91, pO = 0.05):
    newBelief = [0 for i in range(len(map))]
    direction = int(movement/abs(movement))
    for i in range(len(map)):
        #movement for accurate movement
        newiAC = (i + movement) % len(belief)
        #movement for under shoot
        newiUN = (i + movement- direction) % len(belief)
        #movement for over shoot
        newiOV= (i + movement+ direction) % len(belief)
        # belief update overshoot
        newBelief[newiOV] += (belief[i] *pO)
        # new belief after moving assuming 80% accuracy 
        newBelief[newiAC] += (belief[i] *pA)
        # belief update undershoot
        newBelief[newiUN] += (belief[i] *pU)
    newBelief = [round(newBelief[i], 3) for i in range(len(newBelief))]
    return newBelief
print(belief)
belief = findProb(map, 200, belief)
print(belief)
belief = move(map, belief, 4)
print(belief)
belief = findProb(map, 700, belief)
print(belief)
belief = move(map, belief, -1)
print(belief)