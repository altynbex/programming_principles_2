x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

a = b = c = 4

print(a, b, c, sep = " ") # a = 4, b = 4, c = 4

a, b, c = 5, 6, 7

print(a, b, c, sep = " ") # a = 5, b = 6, c = 7

a = 'Hello'
b = 'Noa'
print(a + b) # HelloNoa

print(a, b, sep = " ") # Hello Noa
print(a, b.replace("Noa", "Bobby")) # Hello Bobby

x = 'Bobby'

def praise_noa():
    x = "Noa" # now it is local
    print(x, " is great!")
praise_noa()
print(x, " is great!") 

x = 'Bobby'

def praise_bobby():
    global x
    x = 'Noa' # x is now global
    print(x, "is great")
praise_bobby()
print(x, "is great")





