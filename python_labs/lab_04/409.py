a = int(input())

gen = (pow(2, x) for x in range(0, a + 1))

print(*gen)