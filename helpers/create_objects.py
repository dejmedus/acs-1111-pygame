import pygame

from classes.fruit import Fruit, FruitType
from classes.player import Player
from classes.bomb import Bomb


def create_objects():

    all_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()

    apple = Fruit(FruitType.APPLE)
    apple2 = Fruit(FruitType.APPLE)
    strawberry = Fruit(FruitType.STRAWBERRY)
    strawberry2 = Fruit(FruitType.STRAWBERRY)
    player = Player()
    bomb = Bomb()

    all_sprites.add(apple)
    # all_sprites.add(apple2)
    all_sprites.add(strawberry)
    all_sprites.add(strawberry2)
    all_sprites.add(bomb)
    all_sprites.add(player)

    fruit_sprites.add(apple)
    # fruit_sprites.add(apple2)
    fruit_sprites.add(strawberry)
    fruit_sprites.add(strawberry2)

    return player, all_sprites, fruit_sprites, bomb
