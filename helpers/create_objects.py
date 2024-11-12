import pygame

from classes.player import Player
from classes.sprite import Sprite


class FruitType:
    APPLE = 'apple'
    STRAWBERRY = 'strawberry'


def create_objects():
    all_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()

    apple = Sprite(FruitType.APPLE)
    apple2 = Sprite(FruitType.APPLE)
    strawberry = Sprite(FruitType.STRAWBERRY)
    strawberry2 = Sprite(FruitType.STRAWBERRY)
    player = Player()
    bomb = Sprite("bomb")

    all_sprites.add(apple)
    all_sprites.add(apple2)
    all_sprites.add(strawberry)
    all_sprites.add(strawberry2)
    all_sprites.add(bomb)
    all_sprites.add(player)

    fruit_sprites.add(apple)
    fruit_sprites.add(apple2)
    fruit_sprites.add(strawberry)
    fruit_sprites.add(strawberry2)

    return player, all_sprites, fruit_sprites, bomb
