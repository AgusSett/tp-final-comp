from math import sqrt, sin, cos, radians
from random import uniform

class vec:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        return vec(self.x + a.x, self.y + a.y, self.z + a.z)

    def __sub__(self, a):
        return vec(self.x - a.x, self.y - a.y, self.z - a.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __mul__(self, a):
        if isinstance(a, float):
            return vec(self.x * a, self.y * a, self.z * a)
        if isinstance(a, vec):
            return self.x * a.x + self.y * a.y + self.z * a.z

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def unit(self):
        return self * (1.0 / self.norm())

    def rot_y(self, angle):
        angle = radians(angle)
        return vec(self.x * cos(angle) + self.z * sin(angle), self.y, self.z * cos(angle) - self.x * sin(angle))

    def rot_x(self, angle):
        angle = radians(angle)
        return vec(self.x, self.y * cos(angle) - self.z * sin(angle), self.y * sin(angle) + self.z * cos(angle))

    def rand(self, limit):
        return vec(uniform(-limit, limit), uniform(-limit, limit), uniform(-limit, limit))