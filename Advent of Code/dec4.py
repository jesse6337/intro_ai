myFile = open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
checklist = []
crossover = []
count = 0
for i in range(len(lines)):
    check = lines[i].split(',')
    #print(check,i)
    for j in range(len(check)):
        checklist.append(check[j].split('-'))
for i in range(len(checklist)):
     for j in range(len(checklist[0])):
            checklist[i][j] = int(checklist[i][j])
for i in range(1,len(checklist),2):
    num1 = checklist[i-1]
    num2 = checklist[i]
    if num1[0] in range(num2[0],num2[1]-1) or num2[0] in range(num1[0], num1[1]-1):
        # this contains that
        crossover.append([num1,num2])
    elif num1[1] in range(num2[0],num2[1]-1)or num2[1] in range(num1[0], num1[1]-1):
        # this contains that
        crossover.append([num2, num1])
#print(len(crossover))
#print(len(checklist))

print(len(crossover))
