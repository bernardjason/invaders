from RunningValues import *
from Collision import Collision
import RunningValues


class PlayerMissile(Collision):
    speed = 4

    def __init__(self, canvas: Canvas, x, y):

        RunningValues.collision_list.append(self)
        self.height = 10
        self.width = 10
        self.canvas = canvas
        self.ticker =0

        self.x = x - self.width / 2
        self.y = y - self.height / 2
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                             fill="yellow")

    def move(self, by: int):
        if self.y > -self.height:
            by = by * self.speed
            self.y = self.y + by
            self.canvas.move(self.shape, 0, by)
        else:
            RunningValues.render_list.remove(self)
            RunningValues.delete_list.append(self)

    def render(self):
        self.ticker = self.ticker +1
        if self.ticker % 8 < 3:
            return
        self.move(-1)

    def hit(self, other):
        if not isinstance(other, PlayerMissile):
            RunningValues.delete_list.append(self)
            if self in RunningValues.render_list:
                RunningValues.render_list.remove(self)
            self.canvas.delete(self.shape)
            RunningValues.collision_list.remove(self)
            RunningValues.delete_list.append(self)
