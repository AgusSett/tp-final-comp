from vec3 import *

class vertex:
    def __init__(self, p = vec(), label = ""):
        self.p = p
        self.f = vec()
        self.label = label

class edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.k = 200.0

    def complete(self, n):
        for i in range(n):
            self.V.append(vertex(label = str(i)))

        for i in range(n):
            for j in range(n):
                if i < j:
                    self.E.append(edge(self.V[i], self.V[j]))

    def bipartite(self, a, b):
        for i in range(a+b):
            label = ("A" + str(i)) if (i < a) else ("B" + str(i+a))
            self.V.append(vertex(label = label))

        for i in range(a):
            for j in range(b):
                self.E.append(edge(self.V[i], self.V[a+j]))

    def fa(self, d):
        return (d*d) / self.k

    def fr(self, d):
        return (self.k*self.k) / d

    def fg(self, d):
        return d

    def iteration(self):
        for v in self.V:
            v.f = vec()

            d = vec() - v.p
            v.f = v.f + d.unit() * self.fg(d.norm())

            for u in self.V:
                if v != u:
                    d = v.p - u.p
                    v.f = v.f + d.unit() * self.fr(d.norm())

        for e in self.E:
            d = e.a.p - e.b.p
            e.a.f = e.a.f - d.unit() * self.fa(d.norm())
            e.b.f = e.b.f + d.unit() * self.fa(d.norm())

        t = 0.05
        for v in self.V:
            v.p = v.p + v.f.unit() * min(5.0, v.f.norm() * t)

    def random(self, limit):
        for v in self.V:
            v.p = vec().rand(limit)

    def load(self, file):
        with file as infile:
            n = int(infile.readline())

            for i in range(n):
                v = infile.readline()
                self.V.append(vertex(label = v.rstrip()))

            while True:
                e = infile.readline()
                
                if e == "":
                    break

                verts = e.rstrip().split(" ")

                find = lambda x : filter(lambda y : y.label == x, self.V)[0]
                a = find(verts[0])
                b = find(verts[1])

                self.E.append(edge(a, b))