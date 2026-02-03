def count(list_name, value):
    result = 0
    for i in list_name:
        if i == value:
            result += 1
    return result

a = int(input())
b = list()
for i in range(a):
    number = input()
    b.append(number)
c = set(b)

triplet_count = 0
for i in c:
    if count(b, i) == 3:
        triplet_count += 1
print(triplet_count)
