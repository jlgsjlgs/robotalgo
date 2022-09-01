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
    
    #Instantiate objects in our simulator

    # Base case
    # obs1 = Obstacle(20,200,"S") 
    # obs2 = Obstacle(100,100,"S") 
    # obs3 = Obstacle(260,40,"W")
    # obs4 = Obstacle(240,200,"E")
    # obs5 = Obstacle(320,320,"W")
    # obslist = [obs1,obs2,obs3,obs4,obs5]

    # Test case 2
    # obs1 = Obstacle(20,200,"S") 
    # obs2 = Obstacle(100,100,"S") 
    # obs3 = Obstacle(260,40,"W")
    # obs4 = Obstacle(240,200,"W")
    # obs5 = Obstacle(280,200,"E")
    # obs6 = Obstacle(320,320,"W")
    # obslist = [obs1,obs2,obs3,obs4,obs5,obs6]

    # Test case 3
    # obs1 = Obstacle(20,200,"S") 
    # obs2 = Obstacle(100,100,"S") 
    # obs3 = Obstacle(260,40,"W")
    # obs4 = Obstacle(240,200,"E")
    # obs5 = Obstacle(340,160,"W")
    # obs6 = Obstacle(320,320,"W")
    # obslist = [obs1,obs2,obs3,obs4,obs5,obs6]

    # Test case 4
    # obs1 = Obstacle(20,200,"S") 
    # obs2 = Obstacle(100,100,"S") 
    # obs3 = Obstacle(260,40,"W")
    # obs4 = Obstacle(240,200,"E")
    # obs5 = Obstacle(320,320,"W")
    # obs6 = Obstacle(340,0,"S")
    # obslist = [obs1,obs2,obs3,obs4,obs5,obs6]

    # Test case 5
    # obs1 = Obstacle(20,200,"S") 
    # obs2 = Obstacle(100,100,"S") 
    # obs3 = Obstacle(260,40,"W")
    # obs4 = Obstacle(240,200,"E")
    # obs5 = Obstacle(340,0,"S")
    # obslist = [obs1,obs2,obs3,obs4,obs5]

    # Test case 6
    obs1 = Obstacle(20,200,"S") 
    obs2 = Obstacle(100,100,"S") 
    obs3 = Obstacle(260,40,"W")
    obs4 = Obstacle(240,200,"E")
    obs5 = Obstacle(320,320,"W")
    obs6 = Obstacle(100,300,"W")
    obslist = [obs1,obs2,obs3,obs4,obs5,obs6]

    drawObstacles(obslist)
    drawGrid() #Instantiate grid lines for visual aid

    robo = Robot() #Instantiate robot
    surface.blit(robo.image, robo.imageposition)

    pygame.display.flip()

    #Algorithm
    visitingorder = exhaustiveSearch(obslist)
    paths = astarsearch(obslist, visitingorder)
    nextmove = 0
    currentobs = 0

    # For debugging purposes
    # for routes in paths:
    #     print("NEW OBSTACLE")
    #     for nodes in routes:
    #         print(nodes.x, nodes.y)
    #     print("OBSTACLE FOUND")

    # These 2 variable just to check if animation is correct
    atGoal = False
    obscounter = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if nextmove <= len(paths[currentobs])-2:
                    nextmove+=1
                    if nextmove > len(paths[currentobs])-2:
                        atGoal = True
                else:
                    nextmove=0
                    currentobs+=1

                
                robo.updateposition(paths[currentobs][nextmove].x, paths[currentobs][nextmove].y)

                if atGoal == True:
                    atGoal = False
                    robo.checkDirection(obslist[int(visitingorder[currentobs])-1].goaldirection)
                    obslist[int(visitingorder[currentobs])-1].scanned()
                    obscounter+=1
            
                surface.fill((255,255,255)) #Set background to white
                drawObstacles(obslist)
                drawGrid() #Instantiate grid lines for visual aid
                surface.blit(robo.image, robo.imageposition)
                pygame.display.flip()
                print("Robot currently at ", robo.x, robo.y)
