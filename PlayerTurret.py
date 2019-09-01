from tkinter import *
from PlayerMissile import *
from RunningValues import render_list
from Collision import Collision
from InvaderMissile import InvaderMissile

class PlayerTurret(Collision):
    missile = 0

    def __init__(self, canvas: Canvas, width, height):

        self.height = 50
        self.width = 50
        self.canvas = canvas

        self.x = width/2 + self.width/2
        self.y = height - self.height*2
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="purple")

    def move(self, bx: int):
        bx = bx * 5
        self.x = self.x + bx
        self.canvas.move(self.shape, bx, 0)

    def render(self):
        return


    def fire(self):
        render_list.append(PlayerMissile(self.canvas, self.x + self.width / 2, self.y - self.height/2))

    def hit(self,other):
        if str(type(other)).__contains__("Invader") :
            lives = RunningValues.lives_variable.get()
            lives = lives-1
            RunningValues.lives_variable.set(lives)

