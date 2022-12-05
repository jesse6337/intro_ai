world = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]

start = [0,0]
end = [4,5]
moves = [[-1,0], [0,-1], [0,1], [1,0]]
found = False
r=start[0]
#?
c= start[1]
open_paths = [[0,0]]
while not found:
    for p in range(len(world)):
        r = open_paths [p][0]
        c = open_paths[p][1]
        for i in range(len(moves)):
            newR = r+moves[i][0]# amount to move a row
            newC = c + moves[i][1] # amount to move colom
            if newR >= 0 and newR <= len(world)-1:
                if newC >= 0 and newR <= len(world[0])-1:
                    open_paths.append([newR, newC])
                    print(open_paths)
    break
    

#print(start)
#print(end)