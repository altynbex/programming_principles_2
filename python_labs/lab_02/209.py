n = int(input())

a = list(map(int, input().split()))

max = a[0]
min = a[0]

for i in range(n):
    if(a[i] > max):
        max = a[i]
    if(a[i] < min):
        min = a[i]

for i in range(n):
    if(a[i] == max):
        a[i] = min

for i in range(n):
    print(a[i], end = ' ')