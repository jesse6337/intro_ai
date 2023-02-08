import visual
import pygame as py
import time
import math
pyg = visual.visualizer(500,500, (3,3))
flag = True
start = time.time()
pace = 9
while flag:
    for event in py.event.get():
            if event.type == py.QUIT:
                flag = False
    current_time = time.time()- start
    questions = math.floor(current_time/pace)+1
    if current_time%pace < 3:
        pyg.screen.fill((0,150,0))
    else:pyg.screen.fill((0,0,0))

    pyg.make_font(str(questions), 200,100)
    pyg.make_font(str(current_time%pace), 200,200)
    pyg.make_font(str(current_time), 200,400)
    #print(current_time)
    py.time.delay(50)