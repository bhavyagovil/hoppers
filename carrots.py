import pygame
class Carrot(pygame.sprite.Sprite):
    def __init__(self, i, blink_interval, *groups):
        super().__init__(*groups)
        self.carrot = 'carrot.png'
        self.image = pygame.image.load(self.carrot).convert_alpha()
        self.image = pygame.transform.scale(self.image, (2*GRID_TILE_SIZE, 2*GRID_TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (GRID_TILE_SIZE * 3 * i + GRID_TILE_SIZE / 2, 0)

        
        self.blink_interval = blink_interval  
        self.last_blink_time = pygame.time.get_ticks()  
        self.visible = True 

    def update(self):
    
        current_time = pygame.time.get_ticks()

        
        if current_time - self.last_blink_time >= self.blink_interval:
            self.visible = not self.visible  
            self.last_blink_time = current_time  

        
        if self.visible:
            self.image = pygame.image.load(self.carrot).convert_alpha()
            self.image = pygame.transform.scale(self.image, (2 * GRID_TILE_SIZE, 2 * GRID_TILE_SIZE))
        else:
            self.image = pygame.Surface((2 * GRID_TILE_SIZE, 2 * GRID_TILE_SIZE), pygame.SRCALPHA)
            self.image.fill((0, 0, 0, 0))  

            
            
            