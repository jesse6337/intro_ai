import time
startTime = time.time()
map = [['r', 'r','g'],
        ['g', 'r','g'],
        ['r','g','r']]

x= 0
for i in range(len(map)):
    x += len(map[i])
pX = 1/x
belief = []
for i in range(len(map)):
    belief.append([])
    for j in range(len(map[i])):
        belief[i].append(pX)
def sense(map, belief, reading):
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            if reading == map[i][j]:
                belief[i][j] *= 0.988
            else: belief[i][j] *= 0.012
    normilizer = 0
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            normilizer += belief[i][j]
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            belief[i][j] /= normilizer
    return belief
def average(belief1, belief2):
    belief = []
    for i in range(len(belief1)):
        belief.append([])
        for j in range(len(belief1[i])):
            belief[i].append(0)
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            belief[i][j] = (belief1[i][j]+belief2[i][j])/2
    return belief

def move(world, belief, move_amount):
    moveBelief = []
    for i in range(len(world)):
        moveBelief.append([])
        for j in range(len(world[i])):
            moveBelief[i].append(0)
    # move in directions
    if move_amount[0] == 0:
        directionx = 0
    else:
        directionx = move_amount[0]/abs(move_amount[0])
    if move_amount[1] == 0:
        directiony = 0
    else:
        directiony = move_amount[1]/abs(move_amount[1])
    for i in range(len(moveBelief)):
        # move in x direction 
        for j in range(len(moveBelief[i])):
            unShootIx = int(move_amount[0]+j - directionx) % len(world) 
            acShootIx = (move_amount[0]+j) % len(world) 
            ovShootIx = int(move_amount[0]+j + directionx) % len(world)
            moveBelief[i][unShootIx] += (belief[i][j] * 0.01)
            moveBelief[i][acShootIx] +=( belief[i][j] * 0.98)
            moveBelief[i][ovShootIx] += (belief[i][j] * 0.01)
    moveBelief2 = []
    for i in range(len(world)):
        moveBelief2.append([])
        for j in range(len(world[i])):
            moveBelief2[i].append(0)
        # move in y direction
    for i in range(len(belief[0])):
        for j in range(len(belief)):
            #un index is currentsly an issue
            unShootIy = int(move_amount[1]+i - directiony) % len(world) 
            acShootIy = (move_amount[1]+i) % len(world) 
            ovShootIy = int((move_amount[1]+i) + directiony) % len(world)
            #print(unShootIy)
            #print(acShootIy)
            #print(ovShootIy)
            moveBelief2[unShootIy][j] += (belief[i][j] * 0.005)
            moveBelief2[acShootIy][j] += (belief[i][j] * 0.99)
            moveBelief2[ovShootIy][j] += (belief[i][j] * 0.005)
    return average(moveBelief, moveBelief2)
readings = ['r','r','r', 'g', 'g','r']
moves = [[1,1], [1,1], [0,-1], [1,0], [1,0], [1,0]]
for i in range(len(readings)):
    belief = sense(map, belief, readings[i])
    #print(belief)
    belief = move(map, belief, moves[i])
    #print("")
print(belief)
belief = sense(map, belief, 'g')
print(belief)
endTime = time.time()
print(endTime - startTime)