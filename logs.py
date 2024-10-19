class Log(pygame.sprite.Sprite):
    def __init__(self, spd, x, y, direction):
        super().__init__(all_sprites, obstacles)
        self.width = 3 * GRID_TILE_SIZE  
        self.height = GRID_TILE_SIZE
        self.spd = spd if direction == EAST else -spd
        self.direction = direction

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, dt):
        self.rect.x += self.spd * dt
        if self.rect.left > WINDOW_WIDTH and self.direction == EAST:
            self.rect.right = 0
        elif self.rect.right < 0 and self.direction == WEST:
            self.rect.left = WINDOW_WIDTH 
            
#add to bunny
    def update(self, dt):
        #Check if bunny is on a log
        log_collisions = pygame.sprite.spritecollide(self, obstacles, False)
        for log in log_collisions:
            if isinstance(log, Log):
                self.rect.x += log.spd * dt  # Move with the log


            