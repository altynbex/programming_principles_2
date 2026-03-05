import re

text = input()
pat = input()

cnt = list(re.finditer(re.escape(pat), text))

print(len(cnt))