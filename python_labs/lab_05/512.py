import re

text = input()

res = re.findall(r'\d{2,}', text)

print(" ".join(res))