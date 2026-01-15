a = "hello"
b = "Hello123"
c = "12345"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.345"
h = "My Name Is Arpit Sharma"

#isalnum - Returns True if all characters in the string are alphanumeric
print(a, a.isalnum())
print(b, b.isalnum())
print(e, e.isalnum())
print(f, f.isalnum())  # False because it have special character
print(g, g.isalnum())   # False because of decimal

#isalpha - Returns True if all the characters in the string are alphabets
print(a, a.isalpha())
print(b, b.isalpha())
print(c, c.isalpha())

#isdecimal - Returns True if all characters in the string are decimals
print(d, d.isdecimal())
print(g, g.isdecimal())  # False because decimal is considered as string
print(a, a.isdecimal())
print(c, c.isdecimal())

#isdigit - Returns True if all characters in the string are digits

print(d, d.isdigit())
print(c, c.isdigit())
print(g, g.isdigit())  # False because of decimal

#isnumeric - Returns True if all characters in the string are numeric
print(a, a.isnumeric())
print(c, c.isnumeric())
print(g, g.isnumeric())

#islower - Check a string into lower case or not
print(a,a.islower())
print(c,c.islower())
print(d,d.islower())

#isupper - Returns True if all characters in the string are upper case
print(c,c.isupper())
print(d,d.isupper())
print(c,c.isupper())
print(f,f.isupper())

#isspace - Returns True if all characters in the string are whitespaces
print(g,g.isspace())
print(e,e.isspace())
print(f,f.isspace())
print(a,a.isspace())

#istitle - Returns True if the string follows the rules of a title
print(c,c.istitle())
print(a,a.istitle())
print(b,b.istitle())  #First letter capital
print(h,h.istitle())



