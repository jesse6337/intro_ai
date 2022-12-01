world = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]

start = world[0][0]
end = world[4][5]
up, down = (0,-1),(0,1)
left, right = (-1,0),(1,0)
direction = [up, down, left, right]
count = 0
for row in range(len(world)):
    for colom in range(len(world[row])):
        for i in range(len(direction)):
            if row+direction[i][1] <= len(world)-1 and row+direction[i][1]>0:
                row += direction[i][1]
            if colom+direction[i][0] <= len(world[0])-1:
                colom += direction[i][0] 
            print(len(world[0]))
            print(world[row][colom], end= " ")
            if row-direction[i][1]>0:
                row -= direction[i][0]
            if colom-direction[i][0]>0:
                colom -= direction[i][1]
        print(row, " ", colom)
        count +=1
        print("check")
print(count)