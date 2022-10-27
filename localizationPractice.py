map = [True, False, False, True, False, False, False, True, False]
sensor = False
belief = [1/len(map)for i in range(len(map))]
def prob_of_belief(sensor, worldP, belief_):
    world_ = worldP
    # top half of Bayes formula
    for i in range(len(world_)):
        if sensor == world_[i]:
            belief_[i] *= 0.87 
        elif sensor != world_[i]:
            belief_[i] *= 0.13 
    sum = 0 
    #find bottom half of Bayes formula (normalizer)
    for i in belief_:
        sum += i
    #complete Bayes Formula
    for i in range(len(belief_)):
        belief_[i] /= sum
    belief_ = [round(belief_[i], 3) for i in range(len(belief_))]
    return belief_
def move(map, belief, movement = -3, pU = 0.05, pA = 0.85, pO = 0.1):
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
senses = map
stuff = [False, False, False, False]
for i in range(2):
    for i in range(len(senses)):
        belief = prob_of_belief(senses[i], map, belief)
        #print(belief)
        belief = move(map, belief, 1)
        #print(belief)
print(belief)

