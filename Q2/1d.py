def sense(map_of_world, prob_belief, sensor_reading):
    prob_sensor_success = 0.95
    prob_sensor_fail = 1 - prob_sensor_success

    for i in range(len(map_of_world)):
        if map_of_world[i] == sensor_reading:
            prob_belief[i] *= prob_sensor_success
        else:
            prob_belief[i] *= prob_sensor_fail

    norm = sum(prob_belief)
    for i in range(len(prob_belief)):
        prob_belief[i] = round(prob_belief[i] / norm, 3)

    return prob_belief


def move(map_of_world, prob_belief, move_amount):
    prob_ov = .02
    prob_ac = .96
    prob_un = .02

    temp_belief = [0 for i in range(len(prob_belief))]

    direction = int(move_amount / abs(move_amount))

    for i in range(len(map_of_world)):

        ov_index = (i + move_amount + direction) % len(map_of_world)

        ac_index = (i + move_amount) % len(map_of_world)

        un_index = (i + move_amount - direction) % len(map_of_world)

        temp_belief[ov_index] += prob_belief[i] * prob_ov

        temp_belief[ac_index] += prob_belief[i] * prob_ac

        temp_belief[un_index] += prob_belief[i] * prob_un

    temp_belief = [round(i, 3) for i in temp_belief]

    return temp_belief


# map of robot's environment when False is stop sign and True is open road
world = [False, True, True, False, True]
# initial belief
belief = [round(1 / len(world),3) for i in range(len(world))]
senseUpdates = [False, False, True,True]
motionUpdate =[-2, 3,1,4]
flag = True
i = 0
while flag == True:
    s = senseUpdates[i]
    belief = sense(world, belief, s)
    m = motionUpdate[i]
    belief = move(world, belief, m)
    i += 1
    if max(belief) >= 0.9:
        flag = False
    
highestI = 0
for i in range(len(belief)):
    if belief[i] > belief[highestI]: highestI= i
startPoint = (highestI -sum(motionUpdate)) % len(world)
print(startPoint)
#print(highestI)