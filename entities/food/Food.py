import pyxel

from utils.utils import get_cur_game_speed


class Food:
    def __init__(self, x, y, food, type=0):
        self.x = x
        self.y = y
        self.type = type
        self.w = 8
        self.h = 8
        self.is_alive = True
        food.append(self)

    def update(self):
        cur_game_speed = get_cur_game_speed()
        self.x = self.x - cur_game_speed + 0.3
        if(self.x < -10):
            self.is_alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, self.type*8, self.w, self.h)
