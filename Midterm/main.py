import visual
import pygame as py
import localization


def main_localize():
    vis = visual.visualizer(900,900, [3,3])
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
    #readings = ["r","r", "g", "r","r","g","g",'g']
    #moves = [[1,0],[1,0],[-1,0],[0,1],[1,0],[2,2],[1,0],]
    readings = ['g','r','g','g','r','g',"g",'r','g','r',]
    moves = [[1,0],[1,0],[1,0], [1,0],[1,0],[1,0],[0,1], [1,0],[0,-1]]
    time = 500
    while flag:
        #clock.tick(2)
        for event in py.event.get():
            if event.type == py.QUIT:
                flag = False
        if count <= len(readings)-1:
            vis.blank_grid()
            belief = local.prob_belief(world=map, belief= belief, reading= readings[count])
            vis.localize_grid(belief)
            py.time.delay(time)
            if count < len(readings)-1:
                belief = local.move(belief=belief, world = map, move_amount= moves[count])
                py.time.delay(time)
                vis.localize_grid(belief)
        count += 1
#main_localize()

    