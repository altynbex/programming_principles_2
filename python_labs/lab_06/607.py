n = int(input())

w = list(map(str, input().split()))

res = max(w, key = len)

print(res)