n = int(input())

a, b = 0, 1

for i in range(n):
    if i == n - 1:
        print(a)
    else:
        print(a, end=",")
    a, b = b, a + b








# def fib(b):
#     if b == 0:
#         return 0
#     if b == 1:
#         return 1
#     if b > 1:
#         return fib(b-1) + fib(b-2)

# n = int(input())
# if n == 0:
#     print()

# for i in range(n):
#     if i + 2 <= n:
#         print(fib(i), end=",")
#     else:
#         print(fib(i))
