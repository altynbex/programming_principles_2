n = int(input())

if n <= 0:
    print("NO")
else:
    while n % 2 == 0: #256 % 2 == 0, 128 % 2 == 0, 64 % 2 == 0, 32 % 2 == 0, 16 % 2 == 0, 8 % 2 == 0, 4 % 2 == 0, 2 % 2 == 0
        n //= 2 # n = 128, n = 64, n = 32, n = 16, n = 8, n = 4, n = 2, {n = 1}

    if n == 1:
        print("YES")
    else:
        print("NO")
