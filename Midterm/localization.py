class locals:
    def prob_belief(x, world, belief, reading, hit = 0.9, miss = 0.1):
        for i in range(len(world)):
            for j in range(len(world[i])):
                if world[i][j] == reading: belief[i][j] *= hit
                else: belief[i][j]*= miss
        normalizer = 0
        for i in range(len(belief)):
            normalizer += sum(belief[i])
        for i in range(len(belief)):
            for j in range(len(belief[i])):
                belief[i][j] /= normalizer
        belief = [[round(belief[i][j], 7) for j in range(len(belief[i]))] for i in range(len(belief))]
        return belief
    @classmethod
    def average(self, belief1, belief2):
        belief = []
        for i in range(len(belief1)):
            belief.append([])
            for j in range(len(belief1[i])):
                belief[i].append(0)
        for i in range(len(belief)):
            for j in range(len(belief[i])):
                belief[i][j] = (belief1[i][j]+belief2[i][j])/2
        belief = [[round(belief[i][j], 7) for j in range(len(belief[i]))] for i in range(len(belief))]
        return belief

    def move(self,world, belief, move_amount):
        moveBelief = []
        for i in range(len(world)):
            moveBelief.append([])
            for j in range(len(world[i])):
                moveBelief[i].append(0)
        # move in directions
        if move_amount[0] == 0:
            directionx = 0
        else:
            directionx = move_amount[0]/abs(move_amount[0])
        if move_amount[1] == 0:
            directiony = 0
        else:
            directiony = move_amount[1]/abs(move_amount[1])
        for i in range(len(moveBelief)):
            # move in x direction 
            for j in range(len(moveBelief[i])):
                unShootIx = int(move_amount[0]+j - directionx) % len(world) 
                acShootIx = (move_amount[0]+j) % len(world) 
                ovShootIx = int(move_amount[0]+j + directionx) % len(world)
                moveBelief[i][unShootIx] += (belief[i][j] * 0.01)
                moveBelief[i][acShootIx] +=( belief[i][j] * 0.98)
                moveBelief[i][ovShootIx] += (belief[i][j] * 0.01)
        moveBelief2 = []
        for i in range(len(world)):
            moveBelief2.append([])
            for j in range(len(world[i])):
                moveBelief2[i].append(0)
            # move in y direction
        for i in range(len(belief[0])):
            for j in range(len(belief)):
                #un index is currentsly an issue
                unShootIy = int(move_amount[1]+i - directiony) % len(world) 
                acShootIy = (move_amount[1]+i) % len(world) 
                ovShootIy = int((move_amount[1]+i) + directiony) % len(world)
                moveBelief2[unShootIy][j] += (belief[i][j] * 0.005)
                moveBelief2[acShootIy][j] += (belief[i][j] * 0.99)
                moveBelief2[ovShootIy][j] += (belief[i][j] * 0.005)
        return self.average(moveBelief, moveBelief2)