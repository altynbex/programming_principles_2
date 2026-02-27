num = int(input())
g, n, l = 0, 0, 0
for i in range(num):
    oper, value = map(str, input().split())
    if oper == "global":
        g += int(value)
    elif oper == "nonlocal":
        n += int(value)
print(g, n, sep = " ")