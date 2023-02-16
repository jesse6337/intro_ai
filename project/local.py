class localize:
    def __init__(self, map):
        self.map = map
        self.belief = [[1/(len(map)*len(map[0])) for j in range(len(map[i]))]for i in range(len(map))]
    def sense(self, reading):
        for i in range(len(self.belief)):
            for j in range(len(self.belief[i])):
                if reading == self.map[i][j]:
                    self.belief[i][j] *= 0.988
                else: self.belief[i][j] *= 0.012
        normilizer = 0
        for i in range(len(self.belief)):
            for j in range(len(self.belief[i])):
                normilizer += self.belief[i][j]
        for i in range(len(self.belief)):
            for j in range(len(self.belief[i])):
                self.belief[i][j] /= normilizer
        return self.belief
    @staticmethod
    def average(belief1, belief2):
        belief = []
        for i in range(len(belief1)):
            belief.append([])
            for j in range(len(belief1[i])):
                belief[i].append(0)
        for i in range(len(belief)):
            for j in range(len(belief[i])):
                belief[i][j] = (belief1[i][j]+belief2[i][j])/2
        return belief
    def move(self, move_amount):
        moveBelief = []
        for i in range(len(self.map)):
            moveBelief.append([])
            for j in range(len(self.map[i])):
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
                unShootIx = int(move_amount[0]+j - directionx) % len(self.map) 
                acShootIx = (move_amount[0]+j) % len(self.map) 
                ovShootIx = int(move_amount[0]+j + directionx) % len(self.map)
                moveBelief[i][unShootIx] += (self.belief[i][j] * 0.01)
                moveBelief[i][acShootIx] +=( self.belief[i][j] * 0.98)
                moveBelief[i][ovShootIx] += (self.belief[i][j] * 0.01)
        moveBelief2 = []
        for i in range(len(self.map)):
            moveBelief2.append([])
            for j in range(len(self.map[i])):
                moveBelief2[i].append(0)
            # move in y direction
        for i in range(len(self.belief[0])):
            for j in range(len(self.belief)):
                #un index is currentsly an issue
                unShootIy = int(move_amount[1]+i - directiony) % len(self.map) 
                acShootIy = (move_amount[1]+i) % len(self.map) 
                ovShootIy = int((move_amount[1]+i) + directiony) % len(self.map)
                #print(unShootIy)
                #print(acShootIy)
                #print(ovShootIy)
                moveBelief2[unShootIy][j] += (self.belief[i][j] * 0.005)
                moveBelief2[acShootIy][j] += (self.belief[i][j] * 0.99)
                moveBelief2[ovShootIy][j] += (self.belief[i][j] * 0.005)
        return localize.average(moveBelief, moveBelief2)
        