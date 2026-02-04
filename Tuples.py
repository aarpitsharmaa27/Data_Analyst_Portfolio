a = 34,5435,443,43,54,543,45
b = ("Arpit", "Sahil", 34,324,34)
print(type(a))
print((type(b)))

print(a[1:5]) #Slicing in tuples
print(a[3:6])
print(a[::-1]) #Reversing a tuple


for i in a:
    print(i) #Iterating through a tuple



for i in range(len(b)):
    print(b[i]) #Iterating through a tuple using index



i = 0
while i < len(a):
    print(a[i]) #Iterating through a tuple using while loop
    i += 1


# Conversion of list to tuple and vice versa

c = ('Aru','Yo', 435, 34, 34, 42)
print(type(c))

d = list(c) #Converting tuple to list
print(type(d))

d.append(100)
print(d) #Now we can append to the list but not to the tuple 

a = tuple(d)
print(a) #Converting list back to tuple
print(type(a))