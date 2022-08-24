import pygame, math

class Robot:
    def __init__(self):
        self.x = 20
        self.y = 340
        self.direction = math.pi/2
        self.imageposition = (self.x-20, self.y-20)

        if self.direction == math.pi/2:
            self.image = pygame.image.load("resources/robotnorth.png").convert()
        elif self.direction == 0:
            self.image = pygame.image.load("resources/roboteast.png").convert()
        elif self.direction == -math.pi/2:
            self.image = pygame.image.load("resources/robotsouth.png").convert()
        elif self.direction == math.pi:
            self.image = pygame.image.load("resources/robotwest.png").convert()

        self.boundaries = [[self.x-20,self.y-20], [self.x,self.y-20], [self.x+20, self.y-20],
                           [self.x-20, self.y], [self.x, self.y], [self.x+20, self.y],
                           [self.x-20, self.y+20], [self.x,self.y+20], [self.x+20, self.y+20]]