n = int(input())
a = list(map(int, input().split()))

freq = {}


for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_count = 0
answer = a[0]


for x in freq:
    if freq[x] > max_count:
        max_count = freq[x]
        answer = x
    elif freq[x] == max_count and x < answer:
        answer = x

print(answer)
