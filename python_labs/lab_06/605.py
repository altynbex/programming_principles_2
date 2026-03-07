s = input()
vowels = "aeiouAEIOU"


results = []

for char in s:
    if char in vowels:
        results.append(True)
    else:
        results.append(False) 

if any(results):
    print("Yes")
else:
    print("No")