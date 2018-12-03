from math import sqrt
from random import uniform

class vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, a):
        return vec(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return vec(self.x - a.x, self.y - a.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __mul__(self, a):
        if isinstance(a, float):
            return vec(self.x * a, self.y * a)
        if isinstance(a, vec):
            return self.x * a.x + self.y * a.y

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def unit(self):
        m = self.norm()
        if m != 0.0:
            return self * (1.0 / m)
        else:
            return vec(0, 0)

    def rand(self, limit):
        return vec(uniform(-limit, limit), uniform(-limit, limit))