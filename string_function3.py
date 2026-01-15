#endswith() - Returns True if the string ends with the specified value

a = "Arpit Sharma"
print(a.endswith("r"))
print(a.endswith("a"))
print(a.endswith("h",2,8))

#startswith() - Returns True if the string starts with the specified value

a = "Arpit Sharma"
print(a.startswith("r"))
print(a.startswith("A"))
print(a.startswith("S",6,9))

#swapcase() - Swaps case, lower case becomes upper case and vice versa

a = "aRPIT sHARMA"
print(a.swapcase())

#strip() - returns a trimmed version of string

a = "      Arpit Sharma    "
b = ".........Arpit Sharma********"
print(a)
print(a.strip())
print(b)
print(b.strip("*,."))

#split() - Splits the string at the specified separator, and returns a list

a = "#Apple#Banana#Grapes#Arpit"
b = '.waao.haao.maao.gaao.kaao'
print(a.split("#"))
print(b.split("."))

#ijust() - Returns a left justified version of the string

a = "Arpit Sharma"
x = a.ljust(20,"-")
print(x, "is my name")

#rjust - Returns a right justified version of the string

a = "Arpit Sharma"
x = a.rjust(30,"*")
print("You know me ", x)

#replace() - returns a string where a specified value is replaced with a specified value
a ="My name is Arpit"
print(a)
print(a.replace("Arpit","Arpit Sharma"))

#rindex() - Searches the string for a specified value and returns
#the last position of where it was found

a = "Arpit Sharma is a good boy"
print(a.rindex("good"))

#rfind() - Searches the string for a specified value and returns
# the last position of where it was found

a = "Arpit Sharma is a good boy"
print(a.rfind("is"))
print(a.rfind("r",3,20))
