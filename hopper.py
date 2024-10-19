import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Hopper"

GRID_TILE_SIZE = 40
GRID_NUM_COLS = 15
GRID_NUM_ROWS = 15

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

class Bunny(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pass

class Fox(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Adalovelace(pygame.sprite.Sprite):
    def __init__(self):
        pass

class GameMap():
    def __init__(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
