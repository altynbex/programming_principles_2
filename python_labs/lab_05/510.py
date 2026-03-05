import re

text = input()

r = re.search(r'cat|dog', text)

if(r):
    print('Yes')
else:
    print('No')