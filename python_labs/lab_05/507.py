import re

t = input()
p = input()
r = input()

res = re.sub(p, r, t)

print(res)