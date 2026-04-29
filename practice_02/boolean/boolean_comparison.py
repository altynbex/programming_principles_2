print(5 > 1) # True
print(5 < 1) # False
print(5 == 1) # False
print(5 != 1) # True

a = 10
b = 7
print(a > b) # True
print(a != b) # False

a = "furina"
b = 5
try:
    print(a > b)
except TypeError:
    print("str and int cant be compared through > and < operators")
print(a != b) # but we can compare if they are equal

a = "furina"
b = "neuvilette"
print(a == b) # False

a = "7"
b = 7
print(a == b) # False