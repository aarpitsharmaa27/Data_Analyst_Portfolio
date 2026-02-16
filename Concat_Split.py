import numpy as np

a = [3462,6,724,67,2]
b = [62,72,7231,57,6]
print(a + b)            # List merge

c = np.array([38,24,6,8,56])
d = np.array([4362,2,21,1,615])
print(a + b)            # List merge

print(np.concatenate([c,d]))      # Array Merge


# Types of Concatenation --- Horizontal & Vertical

print(np.concatenate([c,d], axis= 0))  # axis = 0 because array have single line values (Horizontal)

e = np.array([[324,52352,35],[23,23562,46]])
f = np.array([[346,32,1],[6,1,64]])
print(np.concatenate([e,f], axis= 1))  #axis = 1 because it has multiple arrays (Vertical)

print(np.hstack([e,f]))  # Horizontal

print(np.vstack([e,f]))    # Vertical


# Splliting of Array

a = np.array([512,61,351,6,343,5])
print(np.array_split(a,3))
print(np.array_split(a,2))

print(np.array_split(a,4))
print(np.array_split(a,5))
print(np.array_split(a,10))


e = np.array([[324,52352,35],[23,23562,46]])
print(np.array_split(e,3))
print(np.array_split(e,8))
print(np.array_split(e,2))