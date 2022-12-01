# using tuples
world = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]

start = world[0][0]
end = world[4][5]
up, dowm = (0,-1),(0,1)
left, right = (-1,0),(1,0)
for row in range(len(world)):
    for colom in range(len(world[row])):
        print(world[row][colom])
        #dowm
        if row +1 < len(world) and row-1 >0:
            print(world[row+1][colom])
            #up
            print(world[row-1][colom])
        #left
        if colom +1 < len(world[row]) and colom -1 > 0:
            print(world[row][colom-1])
            #right
            print(world[row][colom+1])
#print(start)
#print(end)