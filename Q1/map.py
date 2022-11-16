# 1 is door 0 is wall
world = [1,0,1,0,0]
belief = []
# P(Xi)
for i in range(len(world)):
    belief.append(1/len(world))
sAcc = 0.83
sWrong = 0.17
currentSensorReading = 0
normalizor = 0
# then * P(S| Xi)
for i in range(len(belief)):
    if currentSensorReading == world[i]:
        belief[i] *= sAcc
    else: belief[i] *= sWrong
#normalizer
for i in belief:
    normalizor += i
#complete equation
for i in range(len(belief)):
    belief[i] /= normalizor
for i in belief:
    print(i)