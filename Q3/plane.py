import  random

def show_grid(world_map):
    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            print(world_map[i][j], end = '')
        print()


class Plane:
    worldLen = 150
   
    def __init__(self, x_pos, y_pos, map):
        self.x = x_pos
        self.y = y_pos
        self.symbol = '*'
        self.map = map
        self.worldHeight = len(map)

    def find_hog(self):
        # empty space + ground
        #if self.map[len(self.map)-1][self.x] != '_' :
         #   return len(self.map) - self.y
        plane_row = self.y
        plane_col = self.x

        for row_num in range(plane_row, len(self.map)):
            if self.map[row_num][plane_col] == '^':
                return row_num - plane_row
            elif self.map[row_num][plane_col] == '_':
                return row_num - plane_row + 1

    def weights(self, planeACT):
        p =self.find_hog()
        pA = planeACT.find_hog()
        diff = abs(p-pA)
        if diff == 0:
            return 10
        elif diff == 1:
            return 3
        elif diff == 2:
            return 1
        elif diff > 2:
            pass
        elif diff <0:
            print("negative")
        else: print("ERROR")       

    def move( self, move_amount):
        self.x =  (self.x+move_amount)% self.worldLen

    def fuzz(self):
        pass

    def __repr__(self):
        return f'plane({self.x}, {self.y})'


map1 = ['                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '          ^^  ^^                      ^^                                                 ^^^                   ^^^^^               ^^^                ',
        '    ^^  ^^^^^^^^^^       ^^   ^^     ^^^^                                           ^^  ^^^^^     ^^          ^^^^^^^^           ^^^^^^^    ^^^       ',
        '  ^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^   ^^^^^^  ^^  ^^                                 ^^^^^^^^^^^   ^^^^^  ^^  ^^^^^^^^^^^^  ^^  ^^^^^^^^^^^^^^^^^^^^    ',
        '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ',
        '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^_________________________^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^']

p1 = Plane(7,1, map1)
p2 = Plane(5,1, map1)
p3 = Plane(2,1, map1)
pActual = Plane(10,1,map1)
#print(p1.weights(pActual))
h1 = p2.find_hog()




#create initial ditrabution of particals
num_of_particles = 100
distribution = [Plane(random.randrange(0, len(map1[0])-1), 1, map1) for i in range(num_of_particles)]

for i in range(len(distribution)):
    weight = distribution[i].weights(pActual)
    print(weight)


