n = int(input())

a = [0]*n
for i in range(n):
    a[i] = int(input())

sum = 0
for i in range(n):
    sum += a[i]
print(sum)

