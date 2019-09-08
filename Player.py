from tkinter import *
from Collision import Collision
import Explosion
import RunningValues
import Sound

class Player(Collision):
    missile = 0

    def __init__(self, canvas: Canvas, width, height):
        self.height = 40
        self.width = 100
        self.canvas = canvas

        self.x = width / 2
        self.y = height - self.height
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                             fill="yellow")

    def move(self, bx: int):
        bx = bx * 3
        self.x = self.x + bx
        self.canvas.move(self.shape, bx, 0)

    def render(self):
        return

    def cleanup(self):
        self.canvas.delete(self.shape)

    def hit(self, other):
        if str(type(other)).__contains__("Invader"):
            Sound.hit()
            lives = RunningValues.lives_variable.get()
            lives = lives - 1
            RunningValues.lives_variable.set(lives)
            Explosion.create_explosion(self.canvas, self.x + self.width / 2, self.y - self.height / 2)
            RunningValues.player_dead()
