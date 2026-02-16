import numpy as np

a = np.array([[85,83,28,1,5,22,7],[2,5236,5,5237,3,7452,436]])
print(a)


# Sorting of Array
print(np.sort(a))


# Searching in Array
c = np.array([52,6,345,15])     # position of 15 element
b = np.where( c == 15)
print(b)

d = np.where( c % 2 == 0)  # Elements divisible by 2
print(d)

e = np.searchsorted(c,345)  # Search Element
print(e)        


# Filter in array


a = np.array([25,56,13,5,34,64])

b = [False, False, True,True,  False,False]    # True for values we need 
new = a[b]
print(new)

c = a > 30
print(c)    # Values Greater than 30

c = a > 30
d = a[c]
print(d)