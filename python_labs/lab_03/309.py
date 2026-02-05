class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self, radius):
        return 3.14159 * radius * radius

r = int(input())
c1 = Circle(r)
area = c1.area(r)
print(f"{area:.2f}")