# Recommended imports for all problems
# Some problems may require more
i = int(input())
nums = input()
num = nums.split(":")
for i in range(i):
    v = float(num[i])
    x = float(num[i+1])
    if x/v <= 1:
        print("SWERVE")
    elif x/v <= 5:
        print("BRAKE")
    else:
        print("SAFE")