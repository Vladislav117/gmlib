import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distanceToPoint(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def distanceTo(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def distanceFromCenter(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Size:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def w(self):
        return self.width

    def h(self):
        return self.height

    def square(self):
        return self.width * self.height


def emptyMapFillerFormula(point):
    return None


class Map:
    def __init__(self, size: Size, formula=emptyMapFillerFormula, outOfScopeObject=None):
        self.size = size
        self.outOfScopeObject = outOfScopeObject
        self._map = list()
        for y in range(self.size.height):
            self._map.append(list())
            for x in range(self.size.width):
                self._map[-1].append(formula(Point(x=x, y=y)))

    def fill(self, formula):
        for y in range(self.size.height):
            for x in range(self.size.width):
                self._map[y][x] = formula(x, y)

    def get(self, x, y):
        if 0 <= x < self.size.width and 0 <= y < self.size.height:
            return self._map[y][x]
        else:
            return self.outOfScopeObject
