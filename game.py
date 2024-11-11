import pygame

from classes.fruit import Fruit, FruitType
from classes.player import Player
from classes.bomb import Bomb

pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create a new instance of Surface
surf = pygame.Surface((150, 150))
surf.fill((255, 111, 33))

all_sprites = pygame.sprite.Group()

apple = Fruit(FruitType.APPLE)
apple2 = Fruit(FruitType.APPLE)
strawberry = Fruit(FruitType.STRAWBERRY)
strawberry2 = Fruit(FruitType.STRAWBERRY)
player = Player()
bomb = Bomb()


all_sprites.add(apple)
all_sprites.add(apple2)
all_sprites.add(strawberry)
all_sprites.add(strawberry2)
all_sprites.add(bomb)
all_sprites.add(player)

# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Update the window
    pygame.display.flip()

    # tick the clock!
    clock.tick(30)
