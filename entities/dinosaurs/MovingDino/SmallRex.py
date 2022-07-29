from entities.dinosaurs.MovingDino import BaseMovingDino
import pyxel


class SmallRexDinosaur(BaseMovingDino.BaseMovingDino):
    def __init__(self, x, y, cur_game_speed, enemies):
        super().__init__(x, y, 8, 8, cur_game_speed * 1.5 + 1, enemies)

    def update(self):
        super().update()

    def draw(self):
        if((pyxel.frame_count - self.created_at) % 20 > 7):
            pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 8, 8, self.w, self.h)
