from tkinter import *
from PlayerMissile import *
from RunningValues import render_list
from Collision import Collision

class Player(Collision):
    missile = 0

    def __init__(self, canvas: Canvas, width, height):

        self.height = 50
        self.width = 100
        self.canvas = canvas

        self.x = width / 2
        self.y = height - self.height
        self.shape=canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="yellow")

    def move(self, bx: int):
        bx = bx * 5
        self.x = self.x + bx
        self.canvas.move(self.shape, bx, 0)

    def render(self):
        return

    def hit(self,other):
        if str(type(other)).__contains__("Invader") :
            lives = RunningValues.lives_variable.get()
            lives = lives-1
            RunningValues.lives_variable.set(lives)

