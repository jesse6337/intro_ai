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
        self.block_sizeX = math.floor(self.WIDTH/self.grid_size[0]) 
        self.block_sizeY = math.floor(self.HEIGHT/self.grid_size[1]) 
        rectlist = []
        xylist = []
        for x in range(0,self.WIDTH,self.block_sizeX ):
            for y in range(0, self.HEIGHT, self.block_sizeY):
                rect = py.Rect(x, y, self.block_sizeX,self.block_sizeY)
                rectlist.append(rect)
                xylist.append((x,y))
        self.rectlist = rectlist
        self.xylist = xylist
    # not working
    def blank_grid(self):
        for i in range(len(self.rectlist)) :
                py.draw.rect(self.screen, [0,0,0] ,self.rectlist[i])
                py.draw.line(self.screen, (225,225,225),(self.xylist[i][0],0), (self.xylist[i][0],self.HEIGHT))
                py.draw.line(self.screen, (225,225,225),(0,self.xylist[i][1]), (self.WIDTH,self.xylist[i][1]))
                py.display.flip()
<<<<<<< HEAD
    def make_font(self, input, midX,midY):
        num = self.myFont.render(str(input), (255,255,255),(255,255,255))
        self.screen.blit(num, (midX, midY))
        py.display.flip()
=======
>>>>>>> 25d7757bd88f6b60b6bd294bbf1cc8a872ca43fa
    def localize_grid(self, belief):
        for x in range(0,self.WIDTH+ self.block_sizeX,self.block_sizeX ):
            for y in range(0, self.HEIGHT+self.block_sizeY, self.block_sizeY):
                midX = x - math.floor(self.block_sizeX/2)
                midY =y - math.floor(self.block_sizeY/2)
                currentB = belief[round(y/self.block_sizeY)-1][round(x/self.block_sizeX)-1]
                brightness = 200* currentB
                py.draw.rect(self.screen, [0,int(brightness),0] ,py.Rect(x-self.block_sizeX, y-self.block_sizeY, self.block_sizeX,self.block_sizeY))
                f = str(currentB)
<<<<<<< HEAD
                self.make_font(f,midX,midY)
=======
                num = self.myFont.render(f, (255,255,255),(255,255,255))
                self.screen.blit(num, (midX, midY))
>>>>>>> 25d7757bd88f6b60b6bd294bbf1cc8a872ca43fa
                py.display.flip()
    def path_grid(self, belief):
        for x in range(0,self.WIDTH+ self.block_sizeX,self.block_sizeX ):
            for y in range(0, self.HEIGHT+self.block_sizeY, self.block_sizeY):
                midX = x - math.floor(self.block_sizeX/2)
                midY =y - math.floor(self.block_sizeY/2)
                currentB = belief[round(y/self.block_sizeY)-1][round(x/self.block_sizeX)-1]
                brightness = 200* currentB
                py.draw.rect(self.screen, [0,int(brightness),0] ,py.Rect(x-self.block_sizeX, y-self.block_sizeY, self.block_sizeX,self.block_sizeY))
                f = str(currentB)
<<<<<<< HEAD
                self.make_font(f, midX,midY)
=======
                num = self.myFont.render(f, (255,255,255),(255,255,255))
                self.screen.blit(num, (midX, midY))
>>>>>>> 25d7757bd88f6b60b6bd294bbf1cc8a872ca43fa
                py.display.flip()
        
    