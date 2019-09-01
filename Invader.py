from tkinter import *
import RunningValues
from Collision import Collision
from InvaderMissile import InvaderMissile
from PlayerMissile import PlayerMissile
import random


class Invader(Collision):
    speed=1

    def __init__(self, canvas: Canvas, x, y):

        self.width=40
        self.height=40
        self.canvas = canvas

        self.x = x - self.width/2
        self.y = y - self.height/2
        self.shape=canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="green")

    def move(self, byx: int,byy:int):
        byx = byx * self.speed
        self.x = self.x + byx
        byy = byy * self.speed *2
        self.y = self.y + byy
        self.canvas.move(self.shape, byx,byy)


    def render(self):
        if ( RunningValues.move_down > 0 ) :
            self.move(0,1)
        else:
            ran=random.randint(1,100000)
            if ran > 99958 :
                missile = InvaderMissile(self.canvas, self.x + self.width / 2, self.y + self.height)
                RunningValues.render_list.append(missile)
            if self.x <= 0 :
                RunningValues.next_direction = 1
                RunningValues.down()
            if self.x >= RunningValues.canvas_width - self.width :
                RunningValues.next_direction = -1
                RunningValues.down()

            self.move(RunningValues.direction,0)

            if ( self.y > RunningValues.landed_y ) :
                RunningValues.game_over = True

    def hit(self,other):
        if isinstance(other,PlayerMissile) :
            print(self,"been hit by",other)
            RunningValues.delete_list.append(self)
            if self in RunningValues.render_list:
                RunningValues.render_list.remove(self)
            self.canvas.delete(self.shape)
            score = RunningValues.score_variable.get()
            score = score +1
            RunningValues.score_variable.set(score)
