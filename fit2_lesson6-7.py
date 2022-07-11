import pyxel
import math
import random

'''
class Ball:
    speed = 2
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)

ball1 = Ball()
balls = [Ball()]
padx = 100
def update():
    global padx, ballx, bally, vx, vy, speed, score, display, statement, misses, marker, ball1, balls
    if statement:
        padx = pyxel.mouse_x
        for b in balls:
            if b.bally >= 200:
                pyxel.play(0, 1)
                Ball.speed += 0.5
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                angle = pyxel.rndi(30, 150)
                b.vx = pyxel.cos(angle)
                b.vy = pyxel.sin(angle)
                misses += 1
                if misses == 5:
                    statement = False
            if b.bally >= 195 and padx+20 >= b.ballx >= padx-20:
                pyxel.play(0, 0)
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                Ball.speed += 0.2
                score += 1
                marker += 1
                if marker == 10:
                    marker = 0
                    balls.append(ball1)
            if b.ballx < 0 or b.ballx >= 200:
                b.vx *= -1
            b.ballx += b.vx * Ball.speed
            b.bally += b.vy * Ball.speed
            display = 'Score: ' + str(score)
    else:
        return

def draw():
    global padx, ballx, bally, vx, vy, score, display, statement
    pyxel.cls(7)
    if statement: 
        for b in balls:
            pyxel.circ(b.ballx, b.bally, 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
    else:
        pyxel.text(80, 100, "Game Over", 0)
    pyxel.text(5, 5, display, 0)

pyxel.run(update, draw)
''' 
'''
class Ball:
    speed = 2
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
class Pad:
    def __init__(self):
        self.x = 100
ball1 = Ball()
balls = [Ball()]
pad = Pad()

def update():
    global ballx, bally, vx, vy, speed, score, display, statement, misses, marker, ball1, balls
    pad.x = pyxel.mouse_x
    if statement:
        for b in balls:
            if b.bally >= 200:
                pyxel.play(0, 1)
                Ball.speed += 0.5
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                angle = pyxel.rndi(30, 150)
                b.vx = pyxel.cos(angle)
                b.vy = pyxel.sin(angle)
                misses += 1
                if misses == 5:
                    statement = False
            if b.bally >= 195 and pad.x+20 >= b.ballx >= pad.x-20:
                pyxel.play(0, 0)
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                Ball.speed += 0.2
                score += 1
                marker += 1
                if marker == 10:
                    marker = 0
                    balls.append(ball1)
            if b.ballx < 0 or b.ballx >= 200:
                b.vx *= -1
            b.ballx += b.vx * Ball.speed
            b.bally += b.vy * Ball.speed
            display = 'Score: ' + str(score)
    else:
        return

def draw():
    global ballx, bally, vx, vy, score, display, statement
    pyxel.cls(7)
    if statement:
        for b in balls:
            pyxel.circ(b.ballx, b.bally, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    else:
        pyxel.text(80, 100, "Game Over", 0)
    pyxel.text(5, 5, display, 0)

pyxel.run(update, draw)
'''
'''
class Ball:
    speed = 2
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
    def move(self):
        global score, misses, marker
        self.ballx += self.vx * self.speed
        self.bally += self.vy * self.speed
        if self.ballx < 0 or self.ballx >= 200:
            self.vx *= -1
class Pad:
    def __init__(self):
        self.x = 100
ball1 = Ball()
balls = [Ball()]
pad = Pad()
def update():
    global ballx, bally, vx, vy, speed, score, display, statement, misses, marker, ball1, balls
    pad.x = pyxel.mouse_x
    if statement:
        for b in balls:
            if b.bally >= 200:
                pyxel.play(0, 1)
                Ball.speed += 0.5
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                angle = pyxel.rndi(30, 150)
                b.vx = pyxel.cos(angle)
                b.vy = pyxel.sin(angle)
                misses += 1
                if misses == 5:
                    statement = False
            if b.bally >= 195 and pad.x+20 >= b.ballx >= pad.x-20:
                pyxel.play(0, 0)
                b.ballx = pyxel.rndi(0, 199)
                b.bally = 0
                Ball.speed += 0.2
                score += 1
                marker += 1
                if marker == 10:
                    marker = 0
                    balls.append(ball1)
            display = 'Score: ' + str(score)
            Ball.move(b)

def draw():
    global ballx, bally, vx, vy, score, display, statement
    pyxel.cls(7)
    if statement:
        for b in balls:
            pyxel.circ(b.ballx, b.bally, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    else:
        pyxel.text(80, 100, "Game Over", 0)
    pyxel.text(5, 5, display, 0)

pyxel.run(update, draw)
'''
'''
class Ball:
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        self.speed = 2
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
    def move(self):
        global score, misses, marker
        if self.bally >= 200:
            return 1
        if self.bally >= 195 and pad.x+20 >= self.ballx >= pad.x-20:
            return 0
        if self.ballx < 0 or self.ballx >= 200:
            self.vx *= -1
        self.ballx += self.vx * self.speed
        self.bally += self.vy * self.speed
    def running(self):
        self.ballx = pyxel.rndi(0, 199)
        self.bally = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
class Pad:
    def __init__(self):
        self.x = 100
ball1 = Ball()
balls = [Ball()]
pad = Pad()

def update():
    global ballx, bally, vx, vy, speed, score, display, statement, misses, marker, ball1, balls
    pad.x = pyxel.mouse_x
    if statement:
        for b in balls:
            play = Ball.move(b)
            if play == 0:
                pyxel.play(0, 0)
                b.speed += 0.2
                score += 1
                marker += 1
                if marker == 10:
                    marker = 0
                    balls.append(ball1)
                b.running()
            if play == 1:
                pyxel.play(0, 1)
                b.speed += 0.5
                misses += 1
                if misses == 5:
                    statement = False
                b.running()
        display = 'Score: ' + str(score)
    else:
        return() 

def draw():
    global ballx, bally, vx, vy, score, display, statement
    pyxel.cls(7)
    if statement:
        for b in balls:
            pyxel.circ(b.ballx, b.bally, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    else:
        pyxel.text(80, 100, "Game Over", 0)
    pyxel.text(5, 5, display, 0)

pyxel.run(update, draw)
'''
'''
class Ball:
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        self.speed = 2
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
    def move(self):
        global score, misses, marker
        if self.bally >= 200:
            return True
        if self.ballx < 0 or self.ballx >= 200:
            self.vx *= -1
        self.ballx += self.vx * self.speed
        self.bally += self.vy * self.speed
    def running(self):
        self.ballx = pyxel.rndi(0, 199)
        self.bally = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
class Pad:
    def __init__(self):
        self.x = 100
    def catch(self, ball):
        if ball.bally >= 195 and self.x + 20 >= ball.ballx >= self.x-20:
            pyxel.play(0, 0)
            ball.speed += 0.2
            return True
        return False
ball1 = Ball()
balls = [Ball()]
pad = Pad()
def update():
    global ballx, bally, vx, vy, speed, score, display, statement, misses, marker, ball1, balls
    pad.x = pyxel.mouse_x
    if statement:
        for b in balls:
            if pad.catch(b):
                pyxel.play(0, 0)
                b.speed += 0.2
                score += 1
                marker += 1
                if marker == 10:
                    marker = 0
                    balls.append(ball1)
                b.running()
            elif b.move():
                pyxel.play(0, 1)
                b.speed += 0.5
                misses += 1
                if misses == 5:
                    statement = False
                b.running()
        display = 'Score: ' + str(score)
    else:
        return() 

def draw():
    global ballx, bally, vx, vy, score, display, statement
    pyxel.cls(7)
    if statement:
        for b in balls:
            pyxel.circ(b.ballx, b.bally, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    else:
        pyxel.text(80, 100, "Game Over", 0)
    pyxel.text(5, 5, display, 0)

pyxel.run(update, draw)
'''
class Ball:
    def __init__(self):
        self.ballx = pyxel.rndi(0, 100)
        self.bally = 0
        self.speed = 2
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
    def move(self):
        if self.bally >= 200:
            pyxel.play(0, 1)
            self.speed += 0.5
            return True
        if self.ballx < 0 or self.ballx >= 200:
            self.vx *= -1
        self.ballx += self.vx * self.speed
        self.bally += self.vy * self.speed
    def running(self):
        self.ballx = pyxel.rndi(0, 199)
        self.bally = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
class Pad:
    def __init__(self):
        self.x = 100
    def catch(self, ball):
        if ball.bally >= 195 and self.x + 20 >= ball.ballx >= self.x-20:
            pyxel.play(0, 0)
            ball.speed += 0.2
            return True
        return False
class App:
    
    def __init__(self):
        pyxel.init(200,200)
        self.score = 0
        self.misses = 0
        self.marker = 0
        self.statement = True
        self.display = 'Score: 0'
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(notes='A2C2', tones='TT', volumes='33', effects='NN', speed=10)
        self.ball1 = Ball()
        self.balls = [Ball()]
        self.pad = Pad()
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.pad.x = pyxel.mouse_x
        if self.statement:
            for b in self.balls:
                if self.pad.catch(b):
                    self.score += 1
                    self.marker += 1
                    if self.marker == 10:
                        self.marker = 0
                        self.balls.append(self.ball1)
                    b.running()
                elif b.move():
                    self.misses += 1
                    if self.misses == 5:
                        self.statement = False
                    b.running()
            self.display = 'Score: ' + str(self.score)
        else:
            return() 

    def draw(self):
        pyxel.cls(7)
        if self.statement:
            for b in self.balls:
                pyxel.circ(b.ballx, b.bally, 10, 6)
            pyxel.rect(self.pad.x-20, 195, 40, 5, 14)
        else:
            pyxel.text(80, 100, "Game Over", 0)
        pyxel.text(5, 5, self.display, 0)
App()

