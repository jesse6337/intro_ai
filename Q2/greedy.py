world = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]

start = [0,0]
end = [4,5]
moves = [[-1,0], [0,-1], [0,1], [1,0]]
found = False
r= start[0]
ste = 0
c= start[1]
open_paths = [[r,c]]
close_paths = []
step = 0
while not found:
    temp_open_paths = []
    for p in range(len(open_paths)):
        r = open_paths[p][0]
        c = open_paths[p][1]
        current_pos = open_paths[p]
        close_paths.append(current_pos)
        for i in range(len(moves)):
            newR = r+moves[i][0]# amount to move a row
            newC = c + moves[i][1] # amount to move colom
            if newR >= 0 and newR <= len(world)-1:
                if newC >= 0 and newC <= len(world[0])-1:
                    if world[newR][newC] == 0 :
                        if [newR, newC] not in close_paths: 
                            if[newR, newC] not in temp_open_paths:
                                temp_open_paths.append([newR, newC])
                                ##print(temp_open_paths)
    open_paths = temp_open_paths.copy()
    if end in open_paths:
        found = True
    step +=1
    print(open_paths)


    

#print(start)
#print(end)