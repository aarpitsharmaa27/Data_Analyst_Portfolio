a = "My Name is Arpit Sharma. Iam from Palampur"

print(a)

# To find length of string
print(len(a))

# To find the number of times a character is occuring
print(a.count("a"))
print(a.count("m"))

# To convert each letter into upper case
print(a.upper())

# To convert each letter into lower case
print(a.lower())

# To find the index of any character
print(a.index("S"))
print(a.index("r"))
print(a.index("l"))
print(a.index("P",20,40))

# To convert first letter to capital
print(a.capitalize())

# To convert a string into lower case
print(a.casefold())

# To write variable into string
name = "Arpit Sharma"
age = 23
a = "My name is {}"
b = "{} is from Palampur"
c = "{} age is {}"
print(a.format(name))
print(b.format(name))
print(c.format(name,age))

# it fills the given characters and centralized a string

print(name.center(30,"*"))
