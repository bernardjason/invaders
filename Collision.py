import RunningValues


class Collision:
    x = 0
    y = 0
    height = 20
    width = 20

    def collide(self, other):
        if other.x > self.x + self.width or \
                self.x > other.x + other.width or \
                other.y > self.y + self.height or \
                self.y > other.y + other.height:
            return False
        return True

    def hit(self, other):
        RunningValues.delete_list.append(self)
        if self in RunningValues.render_list:
            RunningValues.render_list.remove(self)
        if hasattr(self, 'shape'):
            self.canvas.delete(self.shape)
