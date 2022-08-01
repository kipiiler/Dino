import pyxel

# Blast configuration
BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10


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
