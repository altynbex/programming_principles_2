import re

text = input()

res = re.findall(r'\d{2}/\d{2}/\d{4}', text)

print(len(res))