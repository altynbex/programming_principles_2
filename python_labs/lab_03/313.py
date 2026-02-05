def is_prime(number): # boolean
    result = True
    if number == 2:
        return number
    elif number == 1 or number == 0:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                result = False
                break
        return result

nums = list(map(int, input().split()))
filtered_list = list(filter(lambda x: is_prime(x), nums))

if len(filtered_list) == 0:
    print("No primes")
else:
    print(*filtered_list)