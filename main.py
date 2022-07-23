import pyxel
import random

# Screen Configuration


class Game_State:
    SCREEN_MENU = "menu"
    SCREEN_PLAY = "play"
    SCREEN_GAMEOVER = "over"


# Screen configuration
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 150

# Game configuration
PLAYER_X_START = 10
PLAYER_Y_START = SCREEN_HEIGHT/2 - 8
high_score = 0
GAME_SPEED_NORMAL = 0.5
GAME_ACCELERATE_NORMAL = 0.001
current_game_speed = GAME_SPEED_NORMAL
current_game_acc = GAME_ACCELERATE_NORMAL

# Blast configuration
BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

# List of blasts & enemies & obstacle
blasts = []
enemy = []
food = []
# TODO: implement obstacle class
obstacle = []


def reset_game_setting():
    global blasts
    global enemy
    global food
    global obstacle
    global current_game_speed
    current_game_speed = GAME_SPEED_NORMAL
    blasts = []
    enemy = []
    food = []
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

    def update(self):
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


class Food:
    def __init__(self, x, y, type=0):
        self.x = x
        self.y = y
        self.type = type
        self.w = 8
        self.h = 8
        self.is_alive = True
        food.append(self)

    def update(self):
        self.x = self.x - current_game_speed + 0.3
        if(self.x < -10):
            self.is_alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, self.type*8, self.w, self.h)


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


class SmallRexDinosaur:
    # Class dinosaur represent an enemy dinosaur
    def __init__(self, x: int, y):
        # init
        self.x = x
        self.y = y
        self.h = 8
        self.w = 8
        self.is_alive = True
        enemy.append(self)

    def animation(self):
        if(pyxel.frame_count % 20 > 7):
            pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 8, 8, self.w, self.h)

    def update(self):
        # Move to leftside
        self.x = self.x - current_game_speed*1.5 - 1
        if(self.x < -self.w):
            self.is_alive = False

    def draw(self):
        # draw dinosaur
        self.animation()


class NormalFlyingDinosaur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 8
        self.w = 8
        self.acc = 0.1
        self.create_at = pyxel.frame_count
        self.is_comming = True
        self.is_alive = True
        enemy.append(self)

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
            if(pyxel.frame_count - self.create_at == 60 * 3):
                self.is_comming = False
                self.w = 24
        else:
            self.acc += 0.2
            self.x -= current_game_speed * (self.acc)

    def draw(self):
        self.animation()


class BigRexDinosaur:
    # Class dinosaur represent an enemy dinosaur
    def __init__(self, x, y):
        # init
        self.x = x
        self.y = y
        self.h = 16
        self.w = 32
        self.is_alive = True
        enemy.append(self)

    def animation(self):
        if(pyxel.frame_count % 14 < 6):
            pyxel.blt(self.x, self.y, 0, 16, 16, self.w, self.h)
        elif(pyxel.frame_count % 14 > 10):
            pyxel.blt(self.x, self.y, 0, 16, 32, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 16, 48, self.w, self.h)

    def update(self):
        # Move to leftside
        self.x = self.x - current_game_speed + 0.2
        if(self.x < -self.w):
            self.is_alive = False

    def draw(self):
        # draw dinosaur
        self.animation()


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

    def update(self):
        # Moving player around with w a s d key
        if not self.is_alive:
            return
        if(self.x > PLAYER_X_START):
            if(not (pyxel.btn(pyxel.KEY_D) and self.booster > 0)):
                self.x -= current_game_speed
        if(not pyxel.btn(pyxel.KEY_D) and self.booster <= 100):
            self.booster += 0.7
        if(pyxel.btn(pyxel.KEY_D) and self.booster > 0):
            self.booster = self.booster - 1.5
            if(self.x < SCREEN_WIDTH - self.h):
                self.x = self.x + ((SCREEN_WIDTH/3) / (100/1.5))
        if(pyxel.btn(pyxel.KEY_W)):
            if(self.y > 0):
                self.y = self.y - current_game_speed
        if(pyxel.btn(pyxel.KEY_S)):
            if(self.y < SCREEN_HEIGHT - self.h):
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


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/resources.pyxres", image=True)
        sound_set_up()
        self.game_state = Game_State.SCREEN_MENU
        self.background = Background()
        self.last_score = 0
        self.music = True
        if(self.music):
            pyxel.playm(0, loop=True)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        reset_game_setting()
        self.player = Player(PLAYER_X_START, PLAYER_Y_START)
        self.player.is_alive = True
        self.current_score = 0

    def update(self):
        global current_game_speed
        current_game_speed += current_game_acc
        self.background.update()
        match self.game_state:
            case Game_State.SCREEN_MENU:
                self.update_screen_menu()
            case Game_State.SCREEN_PLAY:
                self.update_screen_play()
            case Game_State.SCREEN_GAMEOVER:
                self.update_screen_over()
            case _:
                return

    def update_screen_menu(self):
        if(pyxel.btn(pyxel.KEY_SPACE)):
            self.reset()
            self.game_state = Game_State.SCREEN_PLAY
        if(pyxel.btnr(pyxel.KEY_M) and self.music):
            self.music = False
            pyxel.stop()
        elif(pyxel.btnr(pyxel.KEY_M) and not self.music):
            self.music = True
            pyxel.playm(0, loop=True)

    def update_screen_play(self):
        global high_score
        global current_game_speed
        if(int(pyxel.frame_count / current_game_speed) % 60 == 0 or pyxel.frame_count % 60 == 0):
            self.current_score += 1

        # spawn dinosaurs & food
        r = random.randint(0, 3)
        if(pyxel.frame_count % 25 == 0 and len(enemy) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 8)
            SmallRexDinosaur(SCREEN_WIDTH - 8, new_y)
        if(pyxel.frame_count % 30 == 0 and len(food) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 8)
            Food(SCREEN_WIDTH - 8, new_y, r)
        if(pyxel.frame_count % 80 == 0 and len(enemy) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 32)
            BigRexDinosaur(SCREEN_WIDTH - 8, new_y)
        if(pyxel.frame_count % 120 == r and len(enemy) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 32)
            NormalFlyingDinosaur(SCREEN_WIDTH - 8, new_y)

        for item in food:
            if (
                self.player.x + self.player.w > item.x
                and item.x + item.w > self.player.x
                and self.player.y + self.player.h > item.y
                and item.y + item.h > self.player.y
            ):
                if(item.is_alive):
                    self.current_score += 10
                    pyxel.play(0, 0)
                item.is_alive = False

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
                        self.player.x + 8,
                        self.player.y + 8,
                    )
                )
                pyxel.play(0, 1)
                if(self.current_score > high_score):
                    high_score = self.current_score
                self.last_score = self.current_score
        update_list(food)
        update_list(enemy)
        update_list(blasts)
        cleanup_list(blasts)
        cleanup_list(enemy)
        cleanup_list(food)
        if(len(blasts) == 0 and not self.player.is_alive):
            self.game_state = Game_State.SCREEN_GAMEOVER

        self.player.update()

    def update_screen_over(self):
        self.reset()
        if(pyxel.btn(pyxel.KEY_H)):
            if(self.music):
                pyxel.playm(0, loop=True)
            self.game_state = Game_State.SCREEN_MENU
        if(pyxel.btn(pyxel.KEY_R)):
            if(self.music):
                pyxel.playm(0, loop=True)
            self.game_state = Game_State.SCREEN_PLAY

    def draw(self):
        pyxel.cls(0)
        self.background.draw()
        match self.game_state:
            case Game_State.SCREEN_MENU:
                self.draw_screen_menu()
            case Game_State.SCREEN_PLAY:
                self.draw_screen_game()
            case Game_State.SCREEN_GAMEOVER:
                self.draw_screen_over()
            case _:
                return

    def draw_screen_game(self):
        self.player.draw()
        draw_list(enemy)
        draw_list(blasts)
        draw_list(food)
        score = f"{self.current_score:>03}"
        debug = f"{len(enemy)}"
        speed = f"{current_game_speed}"
        # pyxel.text(SCREEN_WIDTH - 15, 12, debug, 1)
        # pyxel.text(SCREEN_WIDTH - 15, 19, speed, 1)
        pyxel.text(SCREEN_WIDTH - 15, 5, score, 1)
        pyxel.text(SCREEN_WIDTH - 16, 5, score, 7)

    def draw_screen_over(self):
        score = f"{self.last_score:>02}"
        pyxel.text(SCREEN_WIDTH/100*45, SCREEN_HEIGHT /
                   100*30, "GAME_OVER", pyxel.frame_count % 12)
        pyxel.text(SCREEN_WIDTH/100*51, SCREEN_HEIGHT /
                   100*40, score, 1)
        pyxel.text(SCREEN_WIDTH/100*51 - 1, SCREEN_HEIGHT /
                   100*40, score, 7)
        pyxel.text(SCREEN_WIDTH/100*42, SCREEN_HEIGHT /
                   100*70, " (R) REPLAY ", 1)
        pyxel.text(SCREEN_WIDTH/100*42 - 1, SCREEN_HEIGHT /
                   100*70, " (R) REPLAY ", 7)
        pyxel.text(SCREEN_WIDTH/100*43, SCREEN_HEIGHT /
                   100*80, " (H) HOME ", 1)
        pyxel.text(SCREEN_WIDTH/100*42, SCREEN_HEIGHT /
                   100*90, "HIGH SCORE: " + str(high_score), 1)
        pyxel.text(SCREEN_WIDTH/100*43 - 1, SCREEN_HEIGHT /
                   100*80, " (H) HOME ", 7)
        pyxel.text(SCREEN_WIDTH/100*42 - 1, SCREEN_HEIGHT /
                   100*90, "HIGH SCORE: " + str(high_score), 7)

    def draw_screen_menu(self):
        pyxel.text(SCREEN_WIDTH/100*40, SCREEN_HEIGHT /
                   100*30, "Dinosaur Tactic", pyxel.frame_count % 16)
        pyxel.text(SCREEN_WIDTH/100*40, SCREEN_HEIGHT /
                   100*70, "- PRESS SPACE -", 1)
        pyxel.text(SCREEN_WIDTH/100*42, SCREEN_HEIGHT /
                   100*80, "HIGH SCORE: " + str(high_score), 1)
        pyxel.text(SCREEN_WIDTH/100*40 - 1, SCREEN_HEIGHT /
                   100*70, "- PRESS SPACE -", 7)
        pyxel.text(SCREEN_WIDTH/100*42 - 1, SCREEN_HEIGHT /
                   100*80, "HIGH SCORE: " + str(high_score), 7)
        if(self.music):
            pyxel.blt(SCREEN_WIDTH - 16, SCREEN_HEIGHT - 18, 0, 0, 32, 16, 16)
        else:
            pyxel.blt(SCREEN_WIDTH - 16, SCREEN_HEIGHT - 18, 0, 0, 48, 16, 16)


def sound_set_up():
    pyxel.sound(0).set(notes='A2C3', tones='TT',
                       volumes='33', effects='NN', speed=10)
    pyxel.sound(1).set(notes='A2C2', tones='TT',
                       volumes='33', effects='NN', speed=10)
    pyxel.sound(3).set(notes=("f0 r a4 r  f0 f0 a4 r" "f0 r a4 r   f0 f0 a4 f0"),
                       tones="n", volumes="1", effects="f", speed=25)
    pyxel.music(0).set([], [], [3], [])


App()
