myFile=open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
count= 0
mostCount = [0,0,0]
for i in range(len(lines)):
    if lines[i] != '\n':
        count+= int(lines[i])
    elif lines[i] == '\n':
        if count > mostCount[0]:
            mostCount[0] = count
            mostCount.sort()
        count = 0
print(mostCount)
topThree =0
for i in mostCount:
    topThree+=i
print(topThree)
        
  
  

