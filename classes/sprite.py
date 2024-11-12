from random import randint, choice
from constants import LANES
from classes.game_object import GameObject


class Sprite(GameObject):
    def __init__(self, type):
        super().__init__(0, 0, f'assets/{type}.png')
        self.coord_values = self.generate_coords()
        self.reset()  # call reset here!

    def generate_coords(self):
        def get_random():
            return (randint(0, 200) / 100) + 1

        coord_options = {
            "horizontal": [get_random(), 0, -64, choice(LANES)],
            "vertical": [0, get_random(), choice(LANES), -64]
        }

        return coord_options[choice(['vertical', 'horizontal'])]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500 or self.x > 500:
            self.reset()

    # add a new method
    def reset(self):
        self.coord_values = self.generate_coords()
        self.dx = self.coord_values[0]
        self.dy = self.coord_values[1]
        self.x = self.coord_values[2]
        self.y = self.coord_values[3]
