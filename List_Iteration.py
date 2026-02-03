a = ["Arpit", "Harsh", "Keshav", "Ashish"]
for i in a:
    print(i)  # Iteration using loop


#Iteration using range and len function 
for i in range(len(a)):
    print(a[i])



# Iteration using while loop
i = 0
while i < len(a):
    print(a[i])
    i += 1


#Using short hand for loop
[print (i) for i in a]