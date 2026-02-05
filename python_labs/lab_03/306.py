class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
l, w = map(int, input().split())
r1 = Rectangle(l, w)

print(r1.area())