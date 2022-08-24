import pygame, sys, time, math
from obstacle import Obstacle
from robot import Robot
from algorithm import *

def drawObstacles(obslist):
    for obs in obslist:
        surface.blit(obs.image,(obs.x, obs.y))

def drawGrid():
    blockSize = 20 #Set the size per grid block
    for x in range(0, 400, blockSize):
        for y in range(0, 400, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, (0,0,0), rect, 1)

    for x in range(0,80, blockSize): #Drawing starting zone
        for y in range(320,400, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, (0,255,255), rect, 1)

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption('MDP Simulator')
    surface = pygame.display.set_mode((400,400))
    surface.fill((255,255,255)) #Set background to white
    
    obs1 = Obstacle(20,200,"S") #Instantiate objects in our simulator
    obs2 = Obstacle(100,100,"S") 
    obs3 = Obstacle(260,40,"W")
    obs4 = Obstacle(240,200,"E")
    obs5 = Obstacle(320,320,"W")
    obslist = [obs1,obs2,obs3,obs4,obs5]
    drawObstacles(obslist)
    drawGrid() #Instantiate grid lines for visual aid

    robo = Robot() #Instantiate robot
    surface.blit(robo.image, robo.imageposition)

    pygame.display.flip()

    #Algorithm WIP
    exhaustiveSearch(obslist)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


