import pyxel


class Background:
    # Endless moving background screen ( achieve by drawing two background continuously)

    def __init__(self):
      # init with two background(x1, y1) & (x2, y2)
        self.x1 = 0
        self.y1 = 0
        self.y2 = 0
        self.x2 = 256

    def update(self, current_game_speed):
      # Seemlessly make twobackground replace and moving toward left side to make endless effect
        self.x1 -= current_game_speed
        self.x2 -= current_game_speed
        if(self.x2 < 0):
            self.x1 = self.x2 + 256
        if(self.x1 < 0):
            self.x2 = self.x1 + 256

    def draw(self):
      # draw background
        pyxel.blt(self.x1, self.y1, 1, 0, 0, 256, 96)
        pyxel.blt(self.x2, self.y2, 1, 0, 0, 256, 96)
        pyxel.blt(self.x1 - 20, self.y1 + (150 - 60), 1, 0, 0, 256, 96)
        pyxel.blt(self.x2 - 20, self.y2 + (150 - 60), 1, 0, 0, 256, 96)
