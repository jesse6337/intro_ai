myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
# for xyz
wins = [ ['C', 'X\n'], ['A', 'Y\n'], ['B', 'Z\n'],]
draws = [['A', 'X\n'], ['B', 'Y\n'], ['C', 'Z\n']]
lost = [ ['B', 'X\n'], ['C', 'Y\n'],['A', 'Z\n']]
numWins, numDraws, numLosts = 0,0,0
points = [0,0,0]
for i in range(len(lines)):
    check = lines[i].split(' ')
    if check[1] == 'X\n':
        for j in range(len(lost)):
            if lost[j][0] == check[0]:
                points[j] +=1
        numLosts+=1
    elif check[1] == 'Y\n':
        for j in range(len(draws)):
            if draws[j][0] == check[0]:
                points[j] +=1
        numDraws +=1
    elif check[1] == "Z\n":
        for j in range(len(wins)):
            if wins[j][0] == check[0]:
                points[j] +=1
        numWins+=1
numWins*=6
numDraws*=3
numLosts *=0
points[1]*=2
points[2]*=3 
print(numWins+ numDraws+ numLosts+sum(points))

            
