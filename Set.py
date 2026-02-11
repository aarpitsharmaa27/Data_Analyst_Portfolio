a = {"Arpit", "Harsh", "Ashish", "Keshav"}
print(a)
print(type(a))


# SET FUNCTIONS

a.add("Tarun")
print(a)

a.pop()
print(a)

a.remove("Ashish")
print(a)

a.discard('Keshav')
print(a)

b = a.copy
print(b)