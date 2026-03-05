import re

text = input()

pattern = r'^[a-zA-Z].*\d$'

if re.match(pattern, text):
    print("Yes")
else:
    print("No")