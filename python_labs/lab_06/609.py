n = int(input())

w = list(map(str, input().split()))
d = list(map(str, input().split()))

char = input()

if char in w:
    for x, y in zip(w, d):
        if x == char:
            print(y)
else:
    print('Not found')