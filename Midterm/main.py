import visual
import pygame as py
gui = visual.visualizer(900,900, [5,5])
bellef = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,5,5]]

flag = True
while flag:
    for event in py.event.get():
        if event.type == py.QUIT:
            flag = False
    gui.blank_grid()
    gui.localize_grid(bellef)

    py.display.flip()