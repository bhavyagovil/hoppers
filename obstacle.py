import pygame

Class Obstacle:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self):
        self.x += self.speed

        if self.x > SCREEN_WIDTH:
            self.x = -self.width

    def draw(self, screen):
       pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

