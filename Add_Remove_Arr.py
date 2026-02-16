import numpy as np

a= np.array([234,5235,256,700])
print(a)


# Append Function
print(np.append(a,100))

print(np.append(a,100000000))

b= np.array([[234,5235],[256,700]])
print(np.append(b,40000))

print(np.append(b,[90000,8000]))


# Insert Function
print(np.insert(b,1,30))   # It add in b variable , at 1 postion, 30 digit
print(np.insert(b,-1,900909))
print(np.insert(b,4,9000000))

f = np.array([[15,1357],[55,2]])
print(np.insert(f,2,[10,100]))

print(np.insert(f,2,[10,100], axis= 1))   # Horizontal Axis
print(np.insert(f,2,[10,100], axis= 0))    # Vertical Axis

g = np.array([[16,7],[2,66],[61,52]])
print(np.insert(g,0,[800,600],axis=0))


# Delete
a= np.array([[234,5235],[256,700]])
print(np.delete(a,1))
print(np.delete(a,1, axis=0))

