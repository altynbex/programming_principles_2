n = int(input())

arr = list(map(int, input().split()))

r = []

for i in range(n):
    if arr[i] >= 0:
        r.append(True)
    else:
        r.append(False)

if(all(r)):
    print('Yes')
else:
    print('No')