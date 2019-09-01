from tkinter import *
from RunningValues import *
from Collision import Collision
import RunningValues
from Player import Player
from PlayerMissile import PlayerMissile

class InvaderMissile(Collision):

    speed=2
    def __init__(self, canvas: Canvas, x, y):

        self.height = 20
        self.width = 10
        self.canvas = canvas

        self.x = x - self.width/2
        self.y = y - self.height/2
        self.shape=canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="red")

    def move(self, by: int):
        if ( self.y > RunningValues.canvas_height  )  :
            render_list.remove(self)
            delete_list.append(self)
        else:
            by = by * self.speed
            self.y = self.y + by
            self.canvas.move(self.shape, 0, by)


    def render(self):
        self.move(1)

    def hit(self,other):
        if str(type(other)).__contains__("Player") :
            RunningValues.delete_list.append(self)
            RunningValues.render_list.remove(self)
            self.canvas.delete(self.shape)
