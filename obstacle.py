import pygame

class Obstacle:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        if self.direction == "N":
            self.image = pygame.image.load("resources/obstaclenorth.png").convert()
        elif self.direction == "E":
            self.image = pygame.image.load("resources/obstacleeast.png").convert()
        elif self.direction == "S":
            self.image = pygame.image.load("resources/obstaclesouth.png").convert()
        elif self.direction == "W":
            self.image = pygame.image.load("resources/obstaclewest.png").convert()

    def scanned(self):
        self.image = pygame.image.load("resources/obstacledone.png").convert()
