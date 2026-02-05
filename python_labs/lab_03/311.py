class Pair():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, another_pair):
        global sum_list; sum_list = [self.a + another_pair.a, self.b + another_pair.b]
        return sum_list
    def cout(self):
        print("Result: ", *sum_list)

a1, b1, a2, b2 = map(int, input().split())
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)
p1.add(p2)
p1.cout()