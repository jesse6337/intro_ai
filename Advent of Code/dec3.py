import string
myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
common = []
flag = False
Lalph = list(string.ascii_lowercase)
Ualph = list(string.ascii_uppercase)
for i in range(len(lines)):
    check = lines[i]
    check11 = slice(0,len(lines[i])//2)
    check22 = slice(len(lines[i])//2, len(lines[i]))
    check1 = check[check11]
    check2 = check[check22]
    print(check1, check2)
    for j in range(len(check1)):
        if flag:break
        for k in range(len(check2)):
            if check1[j] == check2[k]!= '\n':
                common.append(check1[j])
                flag = True
                break
    flag = False
pointsL = 0
pointsU = 0
for i in range(len(Lalph)):
    pointsL += common.count(Lalph[i])* (i+1)  
for i in range(len(Ualph)):
    pointsU += common.count(Ualph[i])*(27+i)
print(pointsL+pointsU)