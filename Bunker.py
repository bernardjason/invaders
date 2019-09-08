from PlayerMissile import *
from Collision import Collision


def setup(canvas):
    between_bunkers = int(RunningValues.canvas_width / 6)
    for xx in range(int(between_bunkers / 2), int(RunningValues.canvas_width - between_bunkers / 1.5),
                    between_bunkers):
        for yy in range(RunningValues.canvas_height - 200, RunningValues.canvas_height - 150, Bunker.size + 1):
            for xxx in range(xx, int(xx + between_bunkers / 2), Bunker.size + 1):
                RunningValues.render_list.append(Bunker(canvas, xxx, yy))


class Bunker(Collision):
    missile = 0
    size = 30

    def __init__(self, canvas: Canvas, x, y):

        self.height = Bunker.size
        self.width = Bunker.size
        self.canvas = canvas

        self.x = x
        self.y = y
        self.shape = canvas.create_rectangle(self.x, self.y - 4, self.x + self.width + 1, self.y + self.height + 4,
                                             fill="brown")

    def render(self):
        return
