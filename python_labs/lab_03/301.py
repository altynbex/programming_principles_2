n = abs(int(input()))

res = True
while n > 0:
    if (n % 10) % 2 != 0:   # егер тақ цифр болса
        res = False
        break
    n //= 10

print("Valid" if res else "Not valid")
