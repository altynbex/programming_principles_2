l = list(map(str, input().split()))
cycles = int(input())

def multiply_list(l: list, c: int):
    init_val = 0
    while init_val < c:
        yield l
        init_val += 1

gen = multiply_list(l, cycles)

for l in gen:
    for values in l:
        print(values, end = " ")