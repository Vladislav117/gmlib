import json
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

    def list(self):
        return [self.x, self.y]

    def tuple(self):
        return self.x, self.y

    def dict(self):
        return {
            'x': self.x,
            'y': self.y
        }


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

    def list(self):
        return [self.width, self.height]

    def tuple(self):
        return self.width, self.height

    def dict(self):
        return {
            'width': self.width,
            'height': self.height
        }


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


class TagData:
    def __init__(self):
        self._data = {}

    def add(self, key, item):
        if key not in self._data:
            self._data[key] = item

    def set(self, key, item):
        self._data[key] = item

    def replace(self, key, item):
        if key in self._data:
            self._data[key] = item

    def remove(self, key):
        if key in self._data:
            del self._data[key]

    def get(self, key):
        if key in self._data:
            return self._data[key]

    def compare(self, key, compareTo):
        if key in self._data:
            return self._data[key] == compareTo
        else:
            return False

    def has(self, key):
        return key in self._data


class Reader:
    @classmethod
    def json(cls, path, encoding='utf-8'):
        fp = open(path, encoding=encoding)
        data = json.load(fp)
        fp.close()
        return data

    @classmethod
    def text(cls, path, encoding='utf-8'):
        fp = open(path, encoding=encoding)
        content = fp.read()
        fp.close()
        return content
