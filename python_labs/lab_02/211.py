n, l, r = map(int, input().split())
a = list(map(int, input().split()))


s = a[:l-1]
s2 = a[l-1:r]
s3 = a[r:]

s2.reverse()

t = s + s2 + s3

for i in range(n):
    print(t[i], end = ' ')