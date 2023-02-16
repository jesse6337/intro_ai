def show_grid(world_map):
    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            print(world_map[i][j], end = '')
        print()


class Plane:
    worldLen = 150
    worldHeight = 9
    def __init__(self, x_pos, y_pos, map):
        self.x = x_pos
        self.y = y_pos
        self.symbol = '*'
        self.map = map

    def find_hog(self):
        # empty space + ground
        if self.map[len(self.map)-1][self.x] != '_' :
            return len(self.map) - self.y
        for y in range(self.worldHeight):
            if self.map[y][self.x] == '^':    
                return abs(y-self.y)

    def weights(self):
        pass

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

p1 = Plane(0,1, map1)
h1 = p1.find_hog()
print(h1)