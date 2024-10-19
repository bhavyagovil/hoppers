import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Hopper"

GRID_TILE_SIZE = 40
GRID_NUM_COLS = 15
GRID_NUM_ROWS = 15

# bunny directions
NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

class Bunny(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((GRID_TILE_SIZE, GRID_TILE_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.start_pos = (x, y)
        self.lives = 4

    def die(self) -> None:
        self.lives -= 1
        self.rect.topleft = self.start_pos

    def move(self, direction: str) -> None:
        if direction == NORTH:
            self.rect.y -= GRID_TILE_SIZE
        elif direction == EAST:
            self.rect.x += GRID_TILE_SIZE
        elif direction == SOUTH:
            self.rect.y += GRID_TILE_SIZE
        elif direction == WEST:
            self.rect.x -= GRID_TILE_SIZE

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.bottom > WINDOW_HEIGHT:
            self.die()

class Fox(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Adalovelace(pygame.sprite.Sprite):
    def __init__(self):
        pass

class GameMap():
    def __init__(self):
        pass

def main() -> None:
    all_sprites = pygame.sprite.Group() # every object here for rendering please
    obstacles = pygame.sprite.Group() # only obstacles so easy to detect if bunny is dead
    finish_boxes = pygame.sprite.Group() # only things that indicate a win

    bunny = Bunny(0, 0, all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bunny.move(NORTH)
                elif event.key == pygame.K_d:
                    bunny.move(EAST)
                elif event.key == pygame.K_s:
                    bunny.move(SOUTH)
                elif event.key == pygame.K_a:
                    bunny.move(WEST)

        window.fill(BLACK)

        all_sprites.draw(window)

        pygame.display.flip()

if __name__ == "__main__":
    main()
