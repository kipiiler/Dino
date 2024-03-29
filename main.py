import pyxel
import random
from entities.dinosaurs.MovingDino.SmallRex import SmallRexDinosaur
from entities.dinosaurs.MovingDino.BigRex import BigRexDinosaur
from entities.dinosaurs.MovingDino.FlyingDino import NormalFlyingDinosaur
from entities.background.background import Background
from entities.blast.blast import Blast
from utils.utils import *
from utils.sound import *
from entities.food.Food import *
from entities.player import Player

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
        self.background.update(current_game_speed)
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
            # SmallRexDinosaur(SCREEN_WIDTH - 8, new_y)
            SmallRexDinosaur(SCREEN_WIDTH - 8, new_y, enemies=enemy)
        if(pyxel.frame_count % 30 == 0 and len(food) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 8)
            Food(SCREEN_WIDTH - 8, new_y, food, r)
        if(pyxel.frame_count % 80 == 0 and len(enemy) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 8)
            BigRexDinosaur(SCREEN_WIDTH - 8, new_y, enemies=enemy)
        if(pyxel.frame_count % 120 == r and len(enemy) < 30):
            new_y = random.randint(0, SCREEN_HEIGHT - 32)
            NormalFlyingDinosaur(SCREEN_WIDTH - 8, new_y, enemies=enemy)

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


App()
