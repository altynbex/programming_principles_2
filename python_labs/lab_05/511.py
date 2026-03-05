import re

text = input()

res = re.findall(r'[A-Z]', text)

print(len(res))