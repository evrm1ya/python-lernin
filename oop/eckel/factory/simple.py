from __future__ import generators
import random

class Shape(object):
    def factory(type):
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
        assert 0, 'Bad shape creation: ' + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self):
        print('Circle.draw')

    def erase(self):
        print('Circle.erase')

class Square(Shape):
    def draw(self):
        print('Square.draw')

    def erase(self):
        print('Square.erase')

# __subclasses__ produces a list of references to each
# subclass of Shape
# only works at first level of inheritance
def shameNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [Shape.factory(i) for i in shameNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()

