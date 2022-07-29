from entities.dinosaurs.MovingDino import BaseMovingDino
import pyxel


class BigRexDinosaur(BaseMovingDino.BaseMovingDino):
    def __init__(self, x, y, cur_game_speed, enemies):
        super().__init__(x, y, 32, 16, cur_game_speed * 1.5 - 0.2, enemies)

    def update(self):
        super().update()

    def draw(self):
        time_count = pyxel.frame_count - self.created_at
        if(time_count % 14 < 6):
            pyxel.blt(self.x, self.y, 0, 16, 16, self.w, self.h)
        elif(time_count % 14 > 10):
            pyxel.blt(self.x, self.y, 0, 16, 32, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 16, 48, self.w, self.h)
