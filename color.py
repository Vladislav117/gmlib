def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


class Color:
    def __init__(self, r=None, g=None, b=None):
        if isinstance(r, (float, int)):
            self.r = int(r)
            self.g = int(g)
            self.b = int(b)
        elif isinstance(r, Color):
            self.r = r.r
            self.g = r.g
            self.b = r.b
        elif isinstance(r, str):
            tmp_color = hex_to_rgb(r)
            self.r = tmp_color[0]
            self.g = tmp_color[1]
            self.b = tmp_color[2]
        else:
            self.r = int(r[0])
            self.g = int(r[1])
            self.b = int(r[2])
        self.check()

    def list(self):
        return [self.r, self.g, self.b]

    def tuple(self):
        return self.r, self.g, self.b

    def dict(self):
        return {
            'r': self.r,
            'g': self.g,
            'b': self.b
        }

    def __repr__(self):
        return f'[R:{self.r} G:{self.g} B:{self.b}]'

    def check(self):
        if self.r > 255:
            self.r = 255
        elif self.r < 0:
            self.r = 0
        if self.g > 255:
            self.g = 255
        elif self.g < 0:
            self.g = 0
        if self.b > 255:
            self.b = 255
        elif self.b < 0:
            self.b = 0
        return self

    def pick(self):
        return Color(self)

    def copy(self):
        return Color(self.r, self.g, self.b)

    def mix(self, color):
        tmp_color = Color(color)
        self.r = int((self.r + tmp_color.r) / 2)
        self.g = int((self.g + tmp_color.g) / 2)
        self.b = int((self.b + tmp_color.b) / 2)
        self.check()
        return self

    def edit(self, delta=30):
        self.r += delta
        self.g += delta
        self.b += delta
        return self

    def __add__(self, other):
        return self.copy().mix(Color(other))

    def setR(self, r):
        self.r = r
        self.check()
        return self

    def setG(self, g):
        self.g = g
        self.check()
        return self

    def setB(self, b):
        self.b = b
        self.check()
        return self

    def set(self, r=None, g=None, b=None):
        if isinstance(r, (float, int)):
            self.r = int(r)
            self.g = int(g)
            self.b = int(b)
        elif isinstance(r, Color):
            self.r = r.r
            self.g = r.g
            self.b = r.b
        elif isinstance(r, str):
            tmp_color = hex_to_rgb(r)
            self.r = tmp_color[0]
            self.g = tmp_color[1]
            self.b = tmp_color[2]
        else:
            self.r = int(r[0])
            self.g = int(r[1])
            self.b = int(r[2])
        self.check()
        return self

    def __getitem__(self, item):
        if item == 0 or item == "r":
            return self.r
        elif item == 1 or item == "g":
            return self.g
        elif item == 2 or item == "b":
            return self.b
        else:
            return -1
