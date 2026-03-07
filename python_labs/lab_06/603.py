n = int(input())

a = list(map(str, input().split()))

for i in range(n):
    print(f"{i}:{a[i]} ", end = " ")