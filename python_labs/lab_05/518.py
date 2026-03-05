import re

text = input()

p = input()

n = re.escape(p)

res = re.findall(n, text)

print(len(res))