import pygame
import math

class Obstacle:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        if self.direction == "N":
            self.image = pygame.image.load("resources/obstaclenorth.png").convert()
            self.goalx = x
            self.goaly = y-80
            self.goaldirection = -math.pi/2
        elif self.direction == "E":
            self.image = pygame.image.load("resources/obstacleeast.png").convert()
            self.goalx = x+80
            self.goaly = y
            self.goaldirection = math.pi
        elif self.direction == "S":
            self.image = pygame.image.load("resources/obstaclesouth.png").convert()
            self.goalx = x
            self.goaly = y+80
            self.goaldirection = math.pi/2
        elif self.direction == "W":
            self.image = pygame.image.load("resources/obstaclewest.png").convert()
            self.goalx = x-80
            self.goaly = y
            self.goaldirection = 0

    def scanned(self):
        self.image = pygame.image.load("resources/obstacledone.png").convert()
