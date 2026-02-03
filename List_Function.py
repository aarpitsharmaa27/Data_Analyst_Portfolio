a = ["Arpit", "Harsh", "Keshav", "Ashish"]
print(a)

print(len(a))  # Length of the list

print(a.count("Harsh"))  # Count occurrences of "Harsh"

a.append("Sanjay")  # Adding an element to the end of the list
print(a)

a.insert(2,"Chirag")
print(a)  # Inserting "Chirag" at index 2

a.remove("Ashish")  # Removing "Ashish" from the list
print(a)

a.pop(1)
print(a)  # Removing element at index 1

b = []
print(b)
b = a.copy()  # Creating a copy of the list
print(b)

print(a.index("Keshav"))  # Finding index of "Keshav"

c = ["YOYO", "MOMO"]
a.extend(c)
print(a)  # Extending list 'a' with elements from list 'c'

a.reverse()
print(a)  # Reversing the list

a.sort()
print(a)  # Sorting the list in ascending order

a.clear()
print(a)  # Clearing all elements from the list