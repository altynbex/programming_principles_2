n = int(input())

a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if 0 < a[i]:
        cnt += 1

print(cnt)