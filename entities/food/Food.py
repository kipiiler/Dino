import pyxel


class Food:
    def __init__(self, x, y, cur_game_speed, food, type=0):
        self.x = x
        self.y = y
        self.type = type
        self.w = 8
        self.h = 8
        self.speed = cur_game_speed
        self.is_alive = True
        food.append(self)

    def update(self):
        self.x = self.x - self.speed + 0.3
        if(self.x < -10):
            self.is_alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, self.type*8, self.w, self.h)
