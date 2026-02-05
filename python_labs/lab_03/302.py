a = int(input())

def isUsual(a):
    while (a % 2 == 0):
        a /= 2
    while (a % 3 == 0):
        a /= 3
    while (a % 5 == 0):
        a /= 5
    print("Yes" if a == 1 else "No")

isUsual(a)