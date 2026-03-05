import re

text = input()

def double_digit(m):
    return m.group() * 2

result = re.sub(r'\d', double_digit, text)

print(result)