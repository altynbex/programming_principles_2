n = int(input())

m = list(map(int, input().split()))

cnt = 0

for i in m:
    if i != 0:
        cnt += 1

print(cnt)

n = int(input())

# 
# m = list(map(int, input().split()))

# map(bool, m)
# sum()
# result = sum(map(bool, m))

# print(result)