from random import randint, choice
from constants import LANES
from classes.game_object import GameObject


class Bomb(GameObject):

    def __init__(self,):
        super(Bomb, self).__init__(0, 0, f'assets/bomb.png')
        self.coord_values = choice([[0, (randint(0, 200) / 100) + 1, choice(
            LANES), -64], [(randint(0, 200) / 100) + 1, 0, -64, choice(LANES)]])
        self.dx = self.coord_values[0]
        self.dy = self.coord_values[1]
        self.reset()  # call reset here!

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500 or self.x > 500:
            self.reset()

    # add a new method
    def reset(self):
        self.x = self.coord_values[2]
        self.y = self.coord_values[3]
