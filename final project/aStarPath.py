start = [0,0]
goal = [4,4]
map = [[0,0,0,0,0,0,0,0],
       [0,1,1,0,0,0,0,0],
       [0,1,0,1,0,0,0,0],
       [0,1,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0]
       ]
openNodeList = []

#print(openList)

# left, right, down, up
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

st = Node(start)
st.update(goal)
nodeList = [st]
deadNodeList = []


k = 0
def find_lowest_f(list):
    order = [[list[i].get_f(), i] for i in range(len(list))]
    order.sort(key=takeSecond)
    return order


previousPose = 0
while k < 10:
    expansion = []
    pose = find_lowest_f(nodeList)[0]
    if pose in deadNodeList:
        pass
    
    for i in posible_moves:
        x = pose[0]+ i[0]
        y = pose[1]+i[1]
        if x >=0 and y >=0 and x<= len(map) and y<= len(map)and map[pose[0]][pose[1]] ==0:
            expansion.append([x,y])
    if expansion == []:
        deadNodeList.append(pose)
        continue
    print(expansion)
    
    for i in expansion:
        n = Node(i)
        n.update(goal)
        nodeList.append(n)
    
    if goal in expansion:
        print("done")
        break
    #print(nodeList)
    previousPose = pose
    k+=1
print("")

        



