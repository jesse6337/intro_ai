import string
myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
common = []
flag = False
Lalph = list(string.ascii_lowercase)
Ualph = list(string.ascii_uppercase)
for i in range(0,len(lines),3):
    check0 = lines[i]
    check1 = lines[i+1]
    check2 = lines[i+2]
    #print(check0, check1, check2)
    # add extra for loop
    for j in range(len(check0)):
        if flag:break
        for k in range(len(check1)):
            if flag :break
            for l in range(len(check2)):
                if check0[j] == check1[k] == check2[l]!= '\n':
                    common.append(check1[k])
                    flag = True
                    break
    flag = False
pointsL = 0
pointsU = 0
print(len(common))
print(common)
for i in range(len(Lalph)):
    pointsL += common.count(Lalph[i])* (i+1)  
for i in range(len(Ualph)):
    pointsU += common.count(Ualph[i])*(27+i)
print(pointsL+pointsU)