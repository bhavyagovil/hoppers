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
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

DEATH_SOUND = pygame.mixer.Sound("impact.wav")
LOSE_SOUND = pygame.mixer.Sound("loosing_sound.wav")
MUSIC = pygame.mixer.Sound("music_loop.wav")

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
        DEATH_SOUND.play()

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

    def update(self, dt) -> None:
        self.rect.x += self.spd * dt

class Adalovelace(pygame.sprite.Sprite):
    def __init__(self, spd, x, y, end_x, end_y, direction):
        super().__init__(all_sprites, obstacles)
        self.width = GRID_TILE_SIZE
        self.height = GRID_TILE_SIZE
        self.spd = spd
        self.dir = direction

        self.start_pos = (x, y)
        self.end_pos = (end_x, end_y)

        self.ada = 'ada.png'
        self.image = pygame.image.load(self.ada).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, dt) -> None:
        if self.dir == EAST:
            self.rect.x += GRID_TILE_SIZE * self.spd * dt
        elif self.dir == WEST:
            self.rect.x -= GRID_TILE_SIZE * self.spd * dt

        # if self.dir == EAST:
        #     if self.rect.left > self.end_pos[0]:
        #         self.rect.topleft = self.start_pos
        # elif self.dir == WEST:
        #     if self.rect.right < self.end_pos[0]:
        #         self.rect.topleft = self.start_pos

        if self.rect.left > WINDOW_WIDTH and self.dir == EAST:
            self.rect.x = self.start_pos[0]
        elif self.rect.right < 0 and self.dir == WEST:
            self.rect.x = self.start_pos[0]

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.image.load("background.jpg")
        self.rect = self.image.get_rect()

        self.start_rect = pygame.Rect(0, WINDOW_HEIGHT - GRID_TILE_SIZE, WINDOW_WIDTH, 2 * GRID_TILE_SIZE)
        self.road1_rect = pygame.Rect(0, WINDOW_HEIGHT - 7 * GRID_TILE_SIZE, WINDOW_WIDTH, 5 * GRID_TILE_SIZE)
        self.central_rect = pygame.Rect(0, WINDOW_HEIGHT - 8 * GRID_TILE_SIZE, WINDOW_WIDTH, GRID_TILE_SIZE)
        self.road2_rect = pygame.Rect(0, 2 * GRID_TILE_SIZE, WINDOW_WIDTH, 5 * GRID_TILE_SIZE)
        self.finish_rect = pygame.Rect(0, 0, WINDOW_WIDTH, 2 * GRID_TILE_SIZE)

    def create_obstacles(self, level):
        for obs in obstacles:
            obs.kill()
        obstacles.empty()

        for i in range(5): # road 1, 5 lanes
            direction = EAST if i % 2 == 0 else WEST
            lane_layout = levels[level][i]
            speed = random.randint(1, 5)
            for j in range(15):
                if lane_layout[j] == 1:
                    if direction == EAST:
                        x = 0 - (j * GRID_TILE_SIZE)
                        y = self.road1_rect.top + i * GRID_TILE_SIZE

                        if direction == EAST:
                            end_x = WINDOW_WIDTH + abs(x)
                        else:
                            end_x = 0 - abs(x)

                        end_y = y
                        ada = Adalovelace(speed, x, y, end_x, end_y, direction)

                    else: # direction == WEST
                        x = WINDOW_WIDTH + j * GRID_TILE_SIZE
                        y = self.road1_rect.top + i * GRID_TILE_SIZE

                        if direction == EAST:
                            end_x = WINDOW_WIDTH + abs(x)
                        else:
                            end_x = 0 - abs(x)

                        end_y = y
                        ada = Adalovelace(speed, x, y, end_x, end_y, direction)

        for i in range(5): # road 2, 5 lanes
            direction = EAST if i % 2 == 0 else WEST
            lane_layout = levels[level][i]
            speed = random.randint(1, 3) + 0.2 * level
            for j in range(15):
                if lane_layout[j] == 1:
                    if direction == EAST:
                        x = 0 - (j * GRID_TILE_SIZE)
                        y = self.road2_rect.top + i * GRID_TILE_SIZE

                        if direction == EAST:
                            end_x = WINDOW_WIDTH + abs(x)
                        else:
                            end_x = 0 - abs(x)

                        end_y = y
                        ada = Adalovelace(speed, x, y, end_x, end_y, direction)

                    else: # direction == WEST
                        x = WINDOW_WIDTH + j * GRID_TILE_SIZE
                        y = self.road2_rect.top + i * GRID_TILE_SIZE

                        if direction == EAST:
                            end_x = WINDOW_WIDTH + abs(x)
                        else:
                            end_x = 0 - abs(x)

                        end_y = y
                        ada = Adalovelace(speed, x, y, end_x, end_y, direction)

levels = [[[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
           [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
           [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

          [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
           [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]]]

class Carrot(pygame.sprite.Sprite):
    def __init__(self, i, blink_interval):
        super().__init__(all_sprites, carrots)
        self.carrot = 'carrot.png'
        self.loaded_image = pygame.image.load(self.carrot).convert_alpha()
        self.loaded_image = pygame.transform.scale(self.loaded_image, (2*GRID_TILE_SIZE, 2*GRID_TILE_SIZE))
        self.invisible_image = pygame.Surface((2 * GRID_TILE_SIZE, 2 * GRID_TILE_SIZE), pygame.SRCALPHA)
        self.invisible_image.fill((0, 0, 0, 0))
        self.rect = self.loaded_image.get_rect()
        self.rect.topleft = (GRID_TILE_SIZE * 3 * i + GRID_TILE_SIZE // 2, 0)

        self.blink_interval = blink_interval
        self.last_blink_time = pygame.time.get_ticks()
        self.visible = True

    def update(self, dt):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_blink_time >= self.blink_interval:
            self.visible = not self.visible
            self.last_blink_time = current_time

        if self.visible:
            self.image = self.loaded_image
        else:
            self.image = self.invisible_image

def draw_text_bottomleft(text, bottomleft, colour, size):
    font = pygame.font.Font("freesansbold.ttf", size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(bottomleft=bottomleft)
    window.blit(text_surface, text_rect)

def draw_text_center(text, center, colour, size):
    font = pygame.font.Font("freesansbold.ttf", size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

all_sprites = pygame.sprite.Group() # every object here for rendering please
obstacles = pygame.sprite.Group() # only obstacles so easy to detect if bunny is dead
carrots = pygame.sprite.Group() # only things that indicate a win

bunny = Bunny(7 * GRID_TILE_SIZE, WINDOW_HEIGHT - GRID_TILE_SIZE)

def main() -> None:
    level = 0
    clock = pygame.time.Clock()

    MUSIC.play(loops=-1)

    background = Background()

    background.create_obstacles(level)

    for i in range(5):
        carrots.add(Carrot(i, 800))

    all_sprites.add(bunny)

    running = True
    game_over = False

    while running:
        dt = clock.tick(60) / 1000

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

        if not game_over:
            carrots_hit = pygame.sprite.spritecollide(bunny, carrots, False)
            for carrot in carrots_hit:
                carrot.kill()
                bunny.rect.topleft = bunny.start_pos

            # check if bunny dead :(
            if pygame.sprite.spritecollideany(bunny, obstacles):
                bunny.die()

            if bunny.lives == 0:
                LOSE_SOUND.play()
                game_over = True

            if len(carrots) == 0:
                for i in range(5):
                    carrots.add(Carrot(i, 800))
                level += 1
                background.create_obstacles(level)

            window.fill(WHITE)

            all_sprites.update(dt)
            all_sprites.draw(window)

            if game_over:
                draw_text_center("Game Over!", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), RED, 64)

            draw_text_bottomleft("Lives: %s" % bunny.lives, (5, WINDOW_HEIGHT - 5), RED, 36)

            pygame.display.flip()

if __name__ == "__main__":
    main()
