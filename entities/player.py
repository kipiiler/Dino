import pyxel
from utils.utils import readJsonFile

configs = readJsonFile("../data/config.json")
# print(configs)


class Player:
    # Class present the player
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.booster = 100
        self.is_alive = True

    def speedingAnimation(self):
        # Load Animation when standing by
        if(pyxel.frame_count % 14 < 6):
            pyxel.blt(self.x, self.y, 0, 64, 32, self.w, self.h)
        elif(pyxel.frame_count % 14 > 10):
            pyxel.blt(self.x, self.y, 0, 64, 16, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 64, 48, self.w, self.h)

    def runningAnimation(self):
        if(pyxel.frame_count % 14 < 6):
            pyxel.blt(self.x, self.y, 0, 48, 32, self.w, self.h)
        elif(pyxel.frame_count % 14 > 10):
            pyxel.blt(self.x, self.y, 0, 48, 16, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 48, 48, self.w, self.h)

    def update(self, current_game_speed):
        # Moving player around with w a s d key
        if not self.is_alive:
            return
        if(self.x > configs["PLAYER_X_START"]):
            if(not (pyxel.btn(pyxel.KEY_D) and self.booster > 0)):
                self.x -= current_game_speed
        if(not pyxel.btn(pyxel.KEY_D) and self.booster <= 100):
            self.booster += 0.7
        if(pyxel.btn(pyxel.KEY_D) and self.booster > 0):
            self.booster = self.booster - 1.5
            if(self.x < configs["SCREEN_WIDTH"] - self.h):
                self.x = self.x + ((configs["SCREEN_WIDTH"]/3) / (100/1.5))
        if(pyxel.btn(pyxel.KEY_W)):
            if(self.y > 0):
                self.y = self.y - current_game_speed
        if(pyxel.btn(pyxel.KEY_S)):
            if(self.y < configs["SCREEN_HEIGHT"] - self.h):
                self.y = self.y + current_game_speed

    def draw_booster(self):
        pyxel.rect(self.x, self.y - 3, 14, 1, 6)
        pyxel.rect(self.x, self.y - 3, 14 * (self.booster/100), 1, 12)

    def draw(self):
        # Draw with animations
        if(pyxel.btn(pyxel.KEY_D) and self.booster > 0):
            self.speedingAnimation()
        else:
            self.runningAnimation()
        self.draw_booster()
