from PlayerMissile import *
from Collision import Collision
import random
import RunningValues


def create_explosion(canvas, x, y):
    for i in range(1, 10):
        RunningValues.render_list.append(Explosion(canvas, x, y))


class Explosion(Collision):
    ticker = 0
    explosion_x = -1
    explosion_y = 1

    def __init__(self, canvas: Canvas, x, y):

        self.height = 10
        self.width = 10
        self.canvas = canvas

        self.x = -100
        self.y = -100
        self.realx = x
        self.realy = y
        self.addx = Explosion.explosion_x * random.randrange(1, 3)
        self.addy = Explosion.explosion_y * random.randrange(1, 3)
        Explosion.explosion_x = Explosion.explosion_x * -1
        Explosion.explosion_y = Explosion.explosion_y * -1

        colours = ['red', 'orange', 'green']

        self.shape = canvas.create_rectangle(x, y, x + self.width, y + self.height,
                                             fill=colours[random.randrange(0, 3)])

    def render(self):
        self.canvas.move(self.shape, self.addx, self.addy)
        self.ticker = self.ticker + 1
        if self.ticker > 75:
            if self in RunningValues.render_list:
                RunningValues.render_list.remove(self)
            self.canvas.delete(self.shape)
        return

    def hit(self, other):
        return
