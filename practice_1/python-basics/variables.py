x = 3

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





