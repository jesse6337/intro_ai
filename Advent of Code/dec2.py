myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
lost = 0
draw = 3
won = 6
# for xyz
wins = [['A', 'Y\n'], ['B', 'Z\n'], ['C', 'X\n']]
draws = [['A', 'X\n'], ['B', 'Y\n'], ['C', 'Z\n']]
lost = [['A', 'Z\n'], ['B', 'X\n'], ['C', 'Y\n']]
numWins, numDraws, numLosts = 0,0,0
errorCount = 0
count = 0
a,b,c= 0,0,0
x,y,z= 0,0,0
for i in range(len(lines)):
    check = lines[i].split(' ')
    count+=1
    print(check)
    if check[0] == 'A':
        a +=1
    elif check[0] == "B":
        b +=1
    elif check[0] == "C":
        c +=1
    elif check[1] == 'X':
        x +=1
    elif check[1] == "Y":
        y +=1
    elif check[1] == "Z":
        z +=1
    for j in range(len(wins)):
        if check == wins[j]:
            numWins+=1
        elif check == draws[j]:
            numDraws +=1
        elif check == lost[j]:
            numLosts+=1
        else:
            errorCount += 1
b*= 2
y *=2
c *= 3
z *= 3
winPoint = numWins * 6
tiePoint = numDraws*3
print(x)
print(winPoint+ tiePoint+x+y+z)
            
