import os

myFile=open(r"C:\Users\Jesse\Desktop\intro_ai\Advent of Code\input.txt")
lines = myFile.readlines()
count, mostCount =  0,0
print(lines)
for i in range(len(lines)):
    if lines[i] != '\n':
        count+= int(lines[i])
    elif lines[i] == '\n':
        if count > mostCount:
            mostCount = count
        count = 0
print(mostCount)
        
  
  

