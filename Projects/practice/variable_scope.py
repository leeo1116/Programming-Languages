def f():
    pass


class God(object):
    a = []

    def make(self):
        self.a = [1, 2, 3]

    def see(self):
        self.a.append(6)

g = God()
g.see()
print(g.a)


