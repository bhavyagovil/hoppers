class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (2 * GRID_TILE_SIZE, 2 * GRID_TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) 
        
trees = [
    Tree(0, 0, 'tree_nobg.png', all_sprites),
    Tree(0, 0, 'tree_nobg.png', all_sprites),
    Tree(0, 0, 'tree_nobg.png', all_sprites),
    Tree(0, 0, 'tree_nobg.png', all_sprites),
    Tree(0, 0, 'tree_nobg.png', all_sprites)
]

for tree in trees:
    all_sprites.add(tree)