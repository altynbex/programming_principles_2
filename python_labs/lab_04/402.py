n = int(input())

if n == 0 or n == 1:
    print("0")
else:
    for i in range(0, n + 1, 2):
        if i + 2 <= n:
            print(i, end=",")
        else:
            print(i)