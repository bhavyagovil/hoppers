import pygame, random

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
WINDOW_TITLE = "Hopper"

GRID_TILE_SIZE = 60
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
GREY = (144, 144, 144)
RED = (255, 0, 0)
ORANGE = (150, 150, 0)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

class Bunny(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_TILE_SIZE, GRID_TILE_SIZE))
        self.image.fill(RED)
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
    def __init__(self, spd, x, y, direction):
        super().__init__(all_sprites, obstacles)
        self.width = GRID_TILE_SIZE
        self.height = GRID_TILE_SIZE
        self.spd = spd if direction == EAST else -spd
        self.direction = direction

        self.image = pygame.Surface((GRID_TILE_SIZE, GRID_TILE_SIZE))
        self.image.fill((ORANGE))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self) -> None:
        self.rect.x += self.spd

class Adalovelace(pygame.sprite.Sprite):
    def __init__(self, spd, x, y, direction):
        super().__init__(all_sprites, obstacles)
        self.width = GRID_TILE_SIZE
        self.height = GRID_TILE_SIZE
        self.spd = spd
        self.dir = direction

        self.ada = 'ada.png'
        self.image = pygame.image.load(self.ada).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self) -> None:
        if self.dir == EAST:
            self.rect.x += GRID_TILE_SIZE * self.spd
        elif self.dir == WEST:
            self.rect.x -= GRID_TILE_SIZE * self.spd

        if self.rect.right < 0:
            self.rect.left = WINDOW_WIDTH + GRID_TILE_SIZE
        elif self.rect.left > WINDOW_WIDTH:
            self.rect.right = 0

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.image.load("background.jpg")
        self.rect = self.image.get_rect()

        self.start_rect = pygame.Rect(0, WINDOW_HEIGHT - GRID_TILE_SIZE, WINDOW_WIDTH, GRID_TILE_SIZE)
        self.road1_rect = pygame.Rect(0, WINDOW_HEIGHT - 6 * GRID_TILE_SIZE, WINDOW_WIDTH, 5 * GRID_TILE_SIZE)
        self.central_rect = pygame.Rect(0, WINDOW_HEIGHT - 7 * GRID_TILE_SIZE, WINDOW_WIDTH, GRID_TILE_SIZE)
        self.road2_rect = pygame.Rect(0, 2 * GRID_TILE_SIZE, WINDOW_WIDTH, 5 * GRID_TILE_SIZE)
        self.finish_rect = pygame.Rect(0, 0, WINDOW_WIDTH, 2 * GRID_TILE_SIZE)

    def create_obstacles(self, level):
        for i in range(5): # road 1
            spd = 0.05
            x, dir = ((-GRID_TILE_SIZE, EAST), (WINDOW_WIDTH, WEST))[random.randint(0, 1)]
            y = self.road1_rect.y + random.randint(1, 2) * GRID_TILE_SIZE
            ada = Adalovelace(spd, x, y, dir)
            obstacles.add(ada)

class Carrot(pygame.sprite.Sprite):
    def __init__(self, i, *groups):
        super().__init__(*groups)
        self.carrot = 'carrot.png'
        self.image = pygame.image.load(self.carrot).convert_alpha()
        self.image = pygame.transform.scale(self.image, (2*GRID_TILE_SIZE, 2*GRID_TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (GRID_TILE_SIZE * 3 * i + GRID_TILE_SIZE/2, 0)

all_sprites = pygame.sprite.Group() # every object here for rendering please
obstacles = pygame.sprite.Group() # only obstacles so easy to detect if bunny is dead
carrots = pygame.sprite.Group() # only things that indicate a win

bunny = Bunny(7 * GRID_TILE_SIZE, WINDOW_HEIGHT - GRID_TILE_SIZE)

def main() -> None:
    clock = pygame.time.Clock()

    background = Background()

    background.create_obstacles(1)

    all_sprites.add(bunny)
    
    for i in range(5):
        all_sprites.add(Carrot(i))
        carrots.add(Carrot(i))

    running = True
    while running:
        clock.tick(60)

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

        # check if bunny dead :(
        if pygame.sprite.spritecollideany(bunny, obstacles):
            print("dead")

        window.fill(WHITE)

        all_sprites.update()
        all_sprites.draw(window)

        pygame.display.flip()

if __name__ == "__main__":
    main()