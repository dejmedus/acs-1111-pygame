from random import randint, choice
from constants import LANES
from classes.game_object import GameObject


class FruitType:
    APPLE = 'apple'
    STRAWBERRY = 'strawberry'


class Fruit(GameObject):

    def __init__(self, fruit: FruitType):
        super(Fruit, self).__init__(0, 0, f'assets/{fruit}.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()  # call reset here!

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the fruit
        if self.y > 500:
            self.reset()

    # add a new method
    def reset(self):
        self.x = choice(LANES)
        self.y = -64
