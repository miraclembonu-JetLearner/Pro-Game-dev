import pgzrun
import random

HEIGHT = 500
WIDTH = 500



R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)


clr = (R,G,B)

Gravity = 2000.0

class ball():
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 25

    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius, clr)


b1 = ball(100,100)

def draw():
    b1.draw()

pgzrun.go()
