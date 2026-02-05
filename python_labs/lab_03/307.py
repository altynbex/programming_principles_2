import math
class Point():
    def __init__(self, x1, y1, new_x1, new_y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.new_x1 = new_x1
        self.new_y1 = new_y1
        self.x2 = x2
        self.y2 = y2
    def show(self, x1, y1):
        return x1, y1
    def move(self, new_x1, new_y1):
        x1 = new_x1
        y1 = new_y1
        return x1, y1
    def dist(self, x1, y1, x2, y2):
        return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

x1, y1 = map(int, input().split())
new_x1, new_y1 = map(int, input().split())
x2, y2 = map(int, input().split())

p1 = Point(x1, y1, new_x1, new_y1, x2, y2)
print(p1.show(x1, y1))
print(p1.move(new_x1, new_y1))
distance = p1.dist(new_x1, new_y1, x2, y2)
print(f"{distance:.2f}")