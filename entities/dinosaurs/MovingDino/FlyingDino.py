import pyxel
from entities.dinosaurs.MovingDino.BaseMovingDino import BaseMovingDino
from utils.utils import get_cur_game_speed


class NormalFlyingDinosaur(BaseMovingDino):
    def __init__(self, x, y, enemies):
        super().__init__(x, y, 8, 8, enemies)
        self.acc = 0.1
        self.is_comming = True

    def animation(self):
        if(self.is_comming):
            if(pyxel.frame_count % 20 > 7):
                pyxel.blt(self.x, self.y, 0, 8, 16, self.w, self.h)
            else:
                pyxel.blt(self.x, self.y, 0, 8, 24, self.w, self.h)
        else:
            if(pyxel.frame_count % 20 > 7):
                pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h)
            else:
                pyxel.blt(self.x, self.y, 0, 16, 8, self.w, self.h)

    def update(self):
        if(self.x < -self.w):
            self.is_alive = False
        if(self.is_comming):
            if(pyxel.frame_count - self.created_at == 60 * 2):
                self.is_comming = False
                self.w = 24
        else:
            self.acc += .5
            self.x -= get_cur_game_speed() * (self.acc)

    def draw(self):
        self.animation()
