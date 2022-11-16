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
                belief[i][j] *= 0.9
            else: belief[i][j] *= 0.1
    normilizer = 0
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            normilizer += belief[i][j]
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            belief[i][j] /= normilizer
    return belief
def bay(belief1, belief2):
    normilizer =0
    belief = []
    for i in range(len(belief1)):
        belief.append([])
        for j in range(len(belief1[i])):
            belief[i].append(0)
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            belief[i][j] = belief1[i][j]*belief2[i][j]
    for i in range(len(belief2)):
        for j in range(len(belief2[i])):
            normilizer += belief[i][j]
    for i in range(len(belief)):
        for j in range(len(belief[i])):
            belief[i][j] /= normilizer
    return belief
    #still in progress

def move(world, belief, move_amount):
    moveBelief = []
    for i in range(len(world)):
        moveBelief.append([])
        for j in range(len(world[i])):
            moveBelief[i].append(0)
    # move in directions
    directionx = move_amount[0]/abs(move_amount[0])
    directiony = move_amount[1]/abs(move_amount[0])
    for i in range(len(moveBelief)):
        # move in x direction 
        for j in range(len(moveBelief[i])):
            unShootIx = int(move_amount[0]+i - directionx) % len(world) 
            acShootIx = (move_amount[0]+i) % len(world) 
            ovShootIx = int(move_amount[0]+i + directionx) % len(world)
            moveBelief[i][unShootIx] += belief[i][j] * 0.1
            moveBelief[i][acShootIx] += belief[i][j] * 0.8
            moveBelief[i][ovShootIx] += belief[i][j] * 0.1
    moveBelief2 = []
    for i in range(len(world)):
        moveBelief2.append([])
        for j in range(len(world[i])):
            moveBelief2[i].append(0)
        # move in y direction
    for i in range(len(belief[0])):
        for j in range(len(belief)):
            unShootIy = int(move_amount[1]+i - directiony) % len(world) 
            acShootIy = (move_amount[1]+i) % len(world) 
            ovShootIy = int(move_amount[1]+i + directiony) % len(world)
            moveBelief2[unShootIy][j] += belief[j][i] * 0.1
            moveBelief2[acShootIy][i] += belief[j][i] * 0.8
            moveBelief2[ovShootIy][i] += belief[j][i] * 0.1
    return bay(moveBelief, moveBelief2)
belief = sense(map, belief, 'r')
print(belief)
belief = move(map, belief, [2,0])
print("")
sum = 0
print(belief)