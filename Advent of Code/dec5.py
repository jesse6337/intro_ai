myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
file = myFile.readlines()
map = []
directions = []
numAsStrings = ['0','1','2','3', '4','5', '6','7','8','9']
for i in range(9):
    map.append(file[i])
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
    object = []
    for row in range(len(map)-1):
        temp_map.append([])
        for colom in range(len(map[row])):
            if map[row][colom] != " ":
                temp_map[row].append(map[row][colom])
            elif map[row][colom] == " " or map[row][colom]== "[" or map[row][colom]== "]":
                temp_map[row].append(None)
    map = temp_map.copy()
    return map
show(map)
map =movement(map, directions[0])
print(directions[0])
print(interperate_direction(directions[0]))
show(map)