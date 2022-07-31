from entities.dinosaurs import BaseDino
import pyxel


class BaseMovingDino(BaseDino.BaseDino):
    def __init__(self, x, y, w, h, enemies):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_alive = True
        self.created_at = pyxel.frame_count
        enemies.append(self)

    def get_speed(self):
        return 0

    def update(self):
        self.x = self.x - self.get_speed()
        if(self.x < -self.w):
            self.is_alive = False

    def draw(self):
        pass
