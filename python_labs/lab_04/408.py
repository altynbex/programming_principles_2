def check_prime(a: int):
    result = True
    for i in range(2, a):
        if a % i == 0:
            result = False
    return result

a = int(input())

def print_prime(a: int):
    init_val = 2
    while init_val <= a:
        if check_prime(init_val) == True:
            yield init_val
        init_val +=1

gen = print_prime(a)

for x in gen:
    print(x, end = " ")