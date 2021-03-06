import json
import math
import os


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

    def __repr__(self):
        return f'[x = {self.x}; y = {self.y}]'


class Line:
    def __init__(self, position_from: Point, position_to: Point):
        self.position_from = position_from
        self.position_to = position_to

    def length(self):
        return math.sqrt((self.position_to.x - self.position_from.x) ** 2 +
                         (self.position_to.y - self.position_from.y) ** 2)

    def list(self):
        return [self.position_from.x, self.position_from.y, self.position_to.x, self.position_to.y]

    def tuple(self):
        return self.position_from.x, self.position_from.y, self.position_to.x, self.position_to.y

    def dict(self):
        return {
            'x1': self.position_from.x,
            'y1': self.position_from.y,
            'x2': self.position_to.x,
            'y2': self.position_to.y
        }

    def __repr__(self):
        return f'[{self.position_from.x}, {self.position_from.y}] --> [{self.position_to.x}, {self.position_to.y}]'

    def __len__(self):
        return math.sqrt((self.position_to.x - self.position_from.x) ** 2 +
                         (self.position_to.y - self.position_from.y) ** 2)


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

    def __repr__(self):
        return f'[{self.width} x {self.height}]'


class Rectangle:
    def __init__(self, position: Point, size: Size):
        self.position = position
        self.size = size

    def pointOnRectangle(self, point: Point):
        return (self.position.x <= point.x <= self.position.x + self.size.width) and \
               (self.position.y <= point.y <= self.position.y + self.size.height)

    def onRectangle(self, x, y):
        return (self.position.x <= x <= self.position.x + self.size.width) and \
               (self.position.y <= y <= self.position.y + self.size.height)

    def list(self):
        return [self.position.x, self.position.y, self.size.width, self.size.height]

    def tuple(self):
        return self.position.x, self.position.y, self.size.width, self.size.height

    def dict(self):
        return {
            'x': self.position.x,
            'y': self.position.y,
            'width': self.size.width,
            'height': self.size.height
        }

    def __repr__(self):
        return f'[{self.size.width} x {self.size.height}] at [{self.position.x}, {self.position.y}]'


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
        return self

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
        return self

    def set(self, key, item):
        self._data[key] = item
        return self

    def replace(self, key, item):
        if key in self._data:
            self._data[key] = item
        return self

    def remove(self, key):
        if key in self._data:
            del self._data[key]
        return self

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

    def __len__(self):
        return len(self._data)

    def length(self):
        return len(self._data)


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


class Files:
    @classmethod
    def all(cls, folder):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                result.append(os.path.join(root, name))
        return result

    @classmethod
    def allByExtension(cls, folder, extension):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                if name.endswith(f'.{extension}'):
                    result.append(os.path.join(root, name))
        return result

    @classmethod
    def allByExtensions(cls, folder, extensions):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                for extension in extensions:
                    if name.endswith(f'.{extension}'):
                        result.append(os.path.join(root, name))
                        break
        return result


class Sine:
    def __init__(self, left_bound=-1, right_bound=1, step=1, start=None):
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.value = left_bound
        if start is not None:
            self.value = start
        self.step = step
        self.rotation = 1

    def update(self, multiplier=1):
        self.value += self.step * multiplier * self.rotation
        if self.left_bound >= self.value:
            self.rotation = 1
            self.value = self.left_bound
        elif self.value >= self.right_bound:
            self.rotation = -1
            self.value = self.right_bound
        return self

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        if self.rotation == 1:
            arrow = '-->'
        else:
            arrow = '<--'
        return f'[{self.left_bound} {arrow} {self.right_bound} (+{self.step})] >> {self.value}'


class IDManager:
    id = -1

    @classmethod
    def get(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def initialized(cls):
        return cls.id != -1

    @classmethod
    def getLastID(cls):
        return cls.id
