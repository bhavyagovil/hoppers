import pygame

Class Obstacle:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self,screen_width):
        self.x += self.speed

        if self.x > screen_width:
            self.x = -self.width

    def draw(self, screen):
       pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Foxes(Obstacle):
    def __init__(self, x, y, speed, image_path):
        self.image = pygame.image.load(image_path)  
        self.image = pygame.transform.scale(self.image, (80, 40)) 
        width, height = self.image.get_size()
        super().__init__(x, y, width, height, speed, None)
    
    
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))