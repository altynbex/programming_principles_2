a = 1
b = 2
if a > b:
    print("True")
elif a == b:
    print("Equal")
else:
    print("False")


a = 7
b = 9
if a > b:
    print("Greater")
else:
    print("Less")

# if a > b:
#     print("True")
# else:
#     print("False")
# elif a == b:
#     print("Equal")

temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")

username = "altynbex"
if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")