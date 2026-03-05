import re

text = input()
y = input()

if(re.search(y, text)):
    print('Yes')
else:
    print('No')