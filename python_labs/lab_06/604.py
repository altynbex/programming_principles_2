n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dot_prod = 0

for i in range(n):
    dot_prod += a[i]*b[i]

print(dot_prod)


# with zip()

# for x, y in zip(a, b):
#     dot_prod += x * y

# print(dot_prod)