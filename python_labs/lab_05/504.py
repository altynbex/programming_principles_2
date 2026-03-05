import re

text = input()

# \d - кез келген цифрды білдіреді (0-9)
# re.findall барлық табылған цифрларды тізім (list) ретінде қайтарады
digits = re.findall(r'\d', text)

print(" ".join(digits))