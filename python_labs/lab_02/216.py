a = int(input())
b = list(map(int, input().split()))
c = []
for i in b:
    print("YES" if i not in c else "NO")
    c.append(i)


