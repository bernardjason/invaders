from tkinter import *
import RunningValues
from Collision import Collision
from InvaderMissile import InvaderMissile
from PlayerMissile import PlayerMissile
import Explosion
import random


def invader_group_change():
    Invader.dont_move_down_clicks = Invader.dont_move_down_clicks + 1

    if Invader.next_direction != 0:
        Invader.direction = Invader.next_direction
    if Invader.next_down != 0:
        Invader.move_down = Invader.next_down
        Invader.next_down = 0
    if Invader.move_down > 0:
        Invader.move_down = Invader.move_down - 1


def setup(canvas):
    Invader.move_down = 0
    Invader.direction = -1
    Invader.next_direction = 0
    Invader.next_down = 0
    Invader.dont_move_down_clicks = 0
    Invader.speed = 1
    Invader.ticker = 0
    space_between_x = 80
    space_between_y = 50
    Invader.invader_count = 0
    Invader.alive_invader_count = 0
    for xx in range(1, 11):
        for yy in range(1, 7):
            RunningValues.render_list.append(
                Invader(canvas, RunningValues.canvas_width - xx * space_between_x, yy * space_between_y))
            Invader.invader_count = Invader.invader_count + 1
    Invader.alive_invader_count = Invader.invader_count


def all_dead():
    if Invader.alive_invader_count < 55:
        return True
    return False


def down():
    if Invader.dont_move_down_clicks >= 0:
        Invader.next_down = 8
        Invader.dont_move_down_clicks = -50


class Invader(Collision):
    speed = 1
    ticker = 0
    invader_count = 0
    alive_invader_count = 0
    move_down: int = 0
    direction: int = -1
    next_direction: int = 0
    next_down: int = 0
    dont_move_down_clicks = 0

    def __init__(self, canvas: Canvas, x, y):

        self.width = 40
        self.height = 30
        self.canvas = canvas

        self.x = x - self.width / 2
        self.y = y - self.height / 2

        self.img1 = canvas.create_image(self.x, self.y, image=RunningValues.invader_photo1)
        self.img2 = canvas.create_image(self.x, self.y, image=RunningValues.invader_photo2)

    def move(self, byx: int, byy: int):
        self.speed = Invader.invader_count / (Invader.alive_invader_count + 1) / 3
        self.speed = self.speed + 1
        byx = byx * self.speed
        self.x = self.x + byx
        byy = byy * self.speed * 2
        self.y = self.y + byy
        self.canvas.move(self.img1, byx, byy)
        self.canvas.move(self.img2, byx, byy)
        if self.ticker % 20 < 10:
            self.canvas.itemconfig(self.img1, state=HIDDEN)
            self.canvas.itemconfig(self.img2, state=NORMAL)
        else:
            self.canvas.itemconfig(self.img1, state=NORMAL)
            self.canvas.itemconfig(self.img2, state=HIDDEN)

    def render(self):
        self.ticker = self.ticker + 1
        if Invader.move_down > 0:
            self.move(0, 1)
        else:
            ran = random.randint(1, 100000)
            if ran > 99958:
                missile = InvaderMissile(self.canvas, self.x + self.width / 2, self.y + self.height)
                RunningValues.render_list.append(missile)
            if self.x <= self.width:
                Invader.next_direction = 1
                down()
            if self.x >= RunningValues.canvas_width - self.width:
                Invader.next_direction = -1
                down()

            self.move(Invader.direction, 0)

            if self.y > RunningValues.canvas_height - self.height * 3:
                RunningValues.game_over = True

    def hit(self, other):
        if isinstance(other, PlayerMissile):
            Invader.alive_invader_count = Invader.alive_invader_count - 1
            RunningValues.delete_list.append(self)
            if self in RunningValues.render_list:
                RunningValues.render_list.remove(self)
            self.canvas.delete(self.img1)
            self.canvas.delete(self.img2)
            score = RunningValues.score_variable.get()
            score = score + 1
            RunningValues.score_variable.set(score)

            Explosion.create_explosion(self.canvas, self.x + self.width / 2, self.y - self.height / 2)
