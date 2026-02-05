import math
n = int(input())
nums = list(map(int, input().split()))
oper_quantity = int(input())

for i in range(oper_quantity):
    oper_info = list(map(str, input().split()))
    if oper_info[0] == "abs":
        nums = list(map(lambda num: abs(num), nums))
    elif oper_info[0] == "add":
        adding_const = int(oper_info[1])
        nums = list(map(lambda num: num + adding_const, nums))
    elif oper_info[0] == "multiply":
        coefficent = int(oper_info[1])
        nums = list(map(lambda num: num * coefficent, nums))
    elif oper_info[0] == "power":
        degree = int(oper_info[1])
        nums = list(map(lambda num: num ** degree, nums))


print(*nums)