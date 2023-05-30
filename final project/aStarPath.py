start = [0,0]
goal = [4,4]
map = [[0,0,0,0,0,0,0,0],
       [0,1,1,0,0,0,0,0],
       [0,1,0,1,0,0,0,0],
       [0,1,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0]
       ]
openList = []

for i in range(len(map)):
    for j in range(len(map[i])):
        openList.append([i,j])



posible_moves = ([-1,0], [1,0], [0,-1], [0,1])

def takeSecond(elem):
    return elem[1]

class Node:
    def __init__(self,pose):
        self.x = pose[0]
        self.y = pose[1]
        self.g = 0
        self.h = None
        self.f = None

    def update(self, goal):
        self.g +=1
        self.h = abs(self.x-goal[0])+ abs(self.y-goal[1])
        self.f = self.g+self.h
    
    def get_pose(self):
        return [self.x,self.y]

    def get_f(self):
        return self.f

    def __repr__(self):
        return f'--x: {self.x} y: {self.y} g: {self.g} h: {self.h} f: {self.f}--'

def find_lowest_f(list):
    lowest = 100
    index = 0
    for i in range(len(list)):
        n = list[i].get_f()
        if n <= lowest:
            lowest =n
            index = i
    return list[index]


closedList = []

nodeList = []
k = 0
flag = True
while flag:
    #print(k)
    
    pose = Node(openList[k])
    pose.update(goal)
    nodeList.append(pose)
    q = find_lowest_f(nodeList)
    openList.remove(q.get_pose())

    
    expansion = []
    for i in range(len(posible_moves)):
        x = q.get_pose()[0]+posible_moves[i][0]
        y = q.get_pose()[1]+posible_moves[i][1]
        try:
            if x>= 0 and x<= len(map[1]) and y>= 0 and y<= len(map) and map[x][y] == 0:
                expansion.append([x,y])
        except: nodeList.remove(pose)
    if expansion == []:
        nodeList.remove(pose)
        continue
    for i in expansion:
        o = Node(i)
        o.update(goal)
        nodeList.append(o)
        if i == goal:
            print("done!")
            flag = False
            break
    k+=1
for i in range(len(nodeList)):
    print(nodeList[i])
    
print(len(nodeList))




