import string

Uppers = string.ascii_uppercase
myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
file = myFile.readlines()
map = []
directions = []
numAsStrings = ['0','1','2','3', '4','5', '6','7','8','9']
translation = []
move = []
for i in range(9):
    map.append(file[i])
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] in Uppers:
            translation.append([int(map[len(map)-1][j]), j])
translation  = [translation[i] for i in range(len(translation)) if i == translation.index(translation[i])]
for i in range(10, len(file)):
    directions.append(file[i])
def show(map):
    for i in range(len(map)):
        print(map[i])
def interperate_direction(direction):
    temp_d = []
    for i in range(len(direction)):
        if direction[i] in numAsStrings:
            temp_d.append(int(direction[i]))
    return temp_d
def movement(map, direction):
    temp_map = []
    for row in range(len(map)-1):
        temp_map.append([])
        for colom in range(len(map[row])):
            if map[row][colom] in Uppers:
                temp_map[row].append([map[row][colom], map[len(map)-1][colom]])
    return map
for i in range(len(directions)):
    move.append(interperate_direction(directions[i]))
show(map)
map =movement(map, directions[0])
#print(move)
show(map)