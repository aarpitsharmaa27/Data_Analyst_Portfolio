names = ["Arpit", "Brt", "Crt", "Drt", "Ert"]
print(names)  
print(type(names))

print(names[0])     #  First element
print(names[1]) #  Second element
print(names[2]) #  Third element

print(names[-1]) #  Last element

print(names[1:3]) # From index 1 to index 3 (excluding index 3)
print(names[:2])  # Every second name
print(names[::2]) # Every name from index 2 to end
print(names[-1:]) # Last name
print(names[-2::])

print(names[::-1]) # Reversing the list

print(names[-1:-6:-2]) # Starting from the last name, moving backwards, every second name