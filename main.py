from pickle import FALSE
from matplotlib import animation
import pyxel
import random

# Blast configuration
BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

# Screen configuration
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 96

# List of blasts & enemies & obstacle
blasts = []
enemy = []
# TODO: implement obstacle class
obstacle = []


def update_list(list):
  # Update el in a list
    for elem in list:
        elem.update()


def draw_list(list):
  # Draw element in a list
    for elem in list:
        elem.draw()


def cleanup_list(list):
  # Remove any el in list that is not alive
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1


class Background:
  # Endless moving background screen ( achieve by drawing two background continuously)

    def __init__(self):
      # init with two background(x1, y1) & (x2, y2)
        self.x1 = 0
        self.y1 = 0
        self.y2 = 0
        self.x2 = 256
        self.v = 0.5

    def update(self):
      # Seemlessly make twobackground replace and moving toward left side to make endless effect
        self.x1 -= self.v
        self.x2 -= self.v
        self.v += 0.00001
        if(self.x2 < 0):
            self.x1 = self.x2 + 256
        if(self.x1 < 0):
            self.x2 = self.x1 + 256

    def draw(self):
      # draw background
        pyxel.blt(self.x1, self.y1, 1, 0, 0, 256, 96)
        pyxel.blt(self.x2, self.y2, 1, 0, 0, 256, 96)


class Blast:
    # Blast class represent the explosion when player contact with a dinosaur

    def __init__(self, x, y):
        # init
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.is_alive = True

    def update(self):
        # Explode till END_RADIUS then disappear
        self.radius += 0.7
        if self.radius > BLAST_END_RADIUS:
            self.is_alive = False

    def draw(self):
        if self.radius < BLAST_END_RADIUS:
            pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
            pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)


class Dinosaur:
    # Class dinosaur represent an enemy dinosaur
    def __init__(self, x: int, y):
      # init
        self.x = x
        self.y = y
        self.h = 8
        self.w = 8
        self.is_alive = True
        enemy.append(self)

    def update(self):
        # Move to leftside
        self.x = self.x - 1
        if(self.x < -10):
            self.is_alive = False

    def draw(self):
        # draw dinosaur
        pyxel.rect(self.x, self.y, self.w, self.h, 3)


class Player:
  # Class present the player
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.booster = 100
        self.is_alive = True

    def standByAnimation(self):
      # Load Animation when standing by
        if(pyxel.frame_count % 20 > 7):
            pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h)

    def xMovingAnimation(self):
      # Load Animation when moving in x direction
        # animation_frame = pyxel.frame_count % 20
        # if(animation_frame < 2):
        #     pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h)
        # elif(animation_frame < 4 and animation_frame > 1):
        #     pyxel.blt(self.x, self.y, 0, 48, 16, self.w, self.h)
        # elif(animation_frame < 5 and animation_frame > 3):
        #     pyxel.blt(self.x, self.y, 0, 48, 32, self.w, self.h)
        # elif(animation_frame < 7 and animation_frame > 5):
        #     pyxel.blt(self.x, self.y, 0, 48, 48, self.w, self.h)
        # else:
        #     pyxel.blt(self.x, self.y, 0, 48, 64, self.w, self.h)
        if(pyxel.frame_count % 14 < 6):
            pyxel.blt(self.x, self.y, 0, 48, 32, self.w, self.h)
        elif(pyxel.frame_count % 14 > 10):
            pyxel.blt(self.x, self.y, 0, 48, 16, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 48, 48, self.w, self.h)

    def yMovingAnimation(self):
      # Load Animation when moving in y direction
        if(pyxel.frame_count % 10 > 4):
            pyxel.blt(self.x, self.y, 0, 0, 16, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 8, 16, self.w, self.h)

    def update(self):
        # Moving player around with w a s d key
        if not self.is_alive:
            return
        if(pyxel.btn(pyxel.KEY_D)):
            if(self.x < SCREEN_WIDTH - self.h):
                self.x = self.x + 1
        if(pyxel.btn(pyxel.KEY_A)):
            if(self.x > 0):
                self.x = self.x - 1
        if(pyxel.btn(pyxel.KEY_W)):
            if(self.y > 0):
                self.y = self.y - 1
        if(pyxel.btn(pyxel.KEY_S)):
            if(self.y < SCREEN_HEIGHT - self.h):
                self.y = self.y + 1

    def checkBorder(x, y):
      # Check whether player is in side the screen or not
        return(x >= 0 and y >= 0 and y <= SCREEN_HEIGHT and x <= SCREEN_WIDTH)

    def draw(self):
      # Draw with animations
        if(pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_A)):
            self.xMovingAnimation()
        elif(pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_S)):
            self.yMovingAnimation()
        else:
            self.standByAnimation()


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/resources.pyxres", image=True)
        self.x = 0
        self.player = Player(0, 0)
        self.background = Background()
        pyxel.run(self.update, self.draw)

    def update(self):
      # spawn dinosaurs
        if(pyxel.frame_count % 60 == 0 and len(enemy) < 20):
            new_y = random.randint(0, SCREEN_HEIGHT - 8)
            Dinosaur(SCREEN_WIDTH - 8, new_y)
      # Detech collision with dinosaur
        for dino in enemy:
            if (
                self.player.x + self.player.w > dino.x
                and dino.x + dino.w > self.player.x
                and self.player.y + self.player.h > dino.y
                and dino.y + dino.h > self.player.y
            ):
                # Game over, append a blast on contact
                dino.is_alive = False
                self.player.is_alive = False
                blasts.append(
                    Blast(
                        self.player.x + 4,
                        self.player.y + 4,
                    )
                )
                pyxel.play(1, 1)
        update_list(enemy)
        update_list(blasts)
        cleanup_list(blasts)
        cleanup_list(enemy)
        self.player.update()
        self.background.update()

    def draw(self):
        pyxel.cls(0)
        self.background.draw()
        draw_list(enemy)
        self.player.draw()
        draw_list(blasts)


App()
