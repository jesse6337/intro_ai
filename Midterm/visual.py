import pygame as py
import math
class visualizer:
    def __init__(self, WIDTH, HEIGHT, grid_size):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.grid_size = grid_size
        self.myFont = py.font.SysFont("Times New Roman", 24)
        block_sizeX = math.floor(self.WIDTH/self.grid_size[0]) 
        block_sizeY = math.floor(self.HEIGHT/self.grid_size[1]) 
        rectlist = []
        xylist = []
        for x in range(0,self.WIDTH,block_sizeX ):
            for y in range(0, self.HEIGHT, block_sizeY):
                rect = py.Rect(x, y, block_sizeX,block_sizeY)
                rectlist.append(rect)
                xylist.append((x,y))
                print(x)
        self.rectlist = rectlist
        self.xylist = xylist
    # not working
    def blank_grid(self):
        for i in range(len(self.rectlist)) :
                py.draw.rect(self.screen, [0,0,0] ,self.rectlist[i])
                py.draw.line(self.screen, (225,225,225),(self.xylist[i][0],0), (self.xylist[i][0],self.HEIGHT))
                py.draw.line(self.screen, (225,225,225),(0,self.xylist[i][1]), (self.WIDTH,self.xylist[i][1]))
    def localize_grid(self, belief):
        block_sizeX = math.floor(self.WIDTH/self.grid_size[0]) 
        block_sizeY = math.floor(self.HEIGHT/self.grid_size[1])
        largert = max(max(belief))
        count = 0
        print(count)
        for x in range(0,self.WIDTH+ block_sizeX,block_sizeX ):
            for y in range(0, self.HEIGHT+block_sizeY, block_sizeY):
                midX = x - math.floor(block_sizeX/2)
                midY =y - math.floor(block_sizeY/2)
                currentB = belief[round(x/block_sizeX)-1][round(y/block_sizeY)-1]
                if currentB == largert:
                    py.draw.rect(self.screen, [0,150,0] ,py.Rect(x-block_sizeX, y-block_sizeY, block_sizeX,block_sizeY))
                f = str(currentB)
                num = self.myFont.render(f, (255,255,255),(255,255,255))
                self.screen.blit(num, (midX, midY))
        #make percenatage base coloring system


v = visualizer(900,900, [5,5])
bellef = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,5,5]]
flag = True
while flag:
    for event in py.event.get():
        if event.type == py.QUIT:
            flag = False
    v.blank_grid()
    v.localize_grid(bellef)

    py.display.flip()
    