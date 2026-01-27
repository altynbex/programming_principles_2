n = int(input())

a = list(map(int, input().split()))

max = a[0]
max_pos = 0
for i in range(n):
    if(a[i] > max):
        max = a[i]
        max_pos = i

print(max_pos+1)