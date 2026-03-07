n = int(input())
a = list(map(int, input().split()))

s = 0

for i in range(n):
    s += a[i]**2

print(s)