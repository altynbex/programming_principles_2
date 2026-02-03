def count(list_name, value):
    result = 0
    for i in list_name:
        if i == value:
            result += 1
    return result

a = int(input())
b = list()
for i in range(a):
    val = input()
    b.append(val)
c_unordered = list(set(b))
c = sorted(c_unordered)

for i in range(len(c)):
    print(c[i], b.index(c[i]) + 1, sep = " ", end = "\n")