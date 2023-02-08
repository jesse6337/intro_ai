import visual
import pygame as py
import localization
import constants
#readings = ['g','r','g','g','r','g','g','r','g','r',]
#moves = [[1,0],[1,0],[1,0], [1,0],[1,0],[1,0],[0,1], [1,0],[0,-1]]

def main_localize():
    screenSize = 900
    vis = visual.visualizer(screenSize,screenSize, [3,3])
    local = localization.locals()
    map = [['r', 'r','g'],
        ['g', 'r','g'],
        ['r','g','r']]
#world = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,5,5]]
    belief = [[1/9 for j in range(len(map[i]))]for i in range(len(map))]
# print(belief)
    clock = py.time.Clock() 
    flag = True
    count = 0
    readings = ["r","r", "g", "r","r","g","g",'g']
    moves = [[1,0],[1,0],[-1,0],[0,1],[1,0],[2,2],[1,0],]
    
    time = 1000
    while flag:
        #readings = constants.readings
        #moves = constants.moves
        #clock.tick(2)
        print(readings,moves)
        for event in py.event.get():
            if event.type == py.QUIT:
                flag = False
            
        if count <= len(readings)-1 and len(readings)> 0:
            #vis.blank_grid()
            belief = local.prob_belief(world=map, belief= belief, reading= readings[count])
            vis.localize_grid(belief)
            vis.make_font(readings[count], int(screenSize/3), 10)
            py.time.delay(time)
        if count < len(readings)-1 and len(readings)> 0:
                belief = local.move(belief=belief, world = map, move_amount= moves[count])
                py.time.delay(time)
                vis.localize_grid(belief)
                vis.make_font(str(moves[count]), int(screenSize*2/3), 10)
                py.time.delay(time)
        count += 1
#main_localize()

    