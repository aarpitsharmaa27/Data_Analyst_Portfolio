import numpy as np 

a = np.array([223,4324,324551,32])  # Array print as list but without commas
print(a)
print(type(a))

b = np.array([[3214,13,513],[513,35125,321],[134,314,513]])
print(b)

v = np.array([[234,424,234,23],
             [41355,513,3,34],
             [46,62,62,45]])
print(v)


#Slicing in array

a = np.array([234,35,151,515])
print(a[0:2])
print((a[::-1]))       #Reverse
print(a[2::])
print(a[:3])


print("hii")


i = np.array([[52,515,15,3],[351,5153,335,35]])

print(i[::-1,::2])  # firstly it reverse the arrays than take 0 and 2 index
                            # element of both the arrays
print(i[0:2,0:2])
print(i[0:4,-1::])
print(i[1,1:2])


i = np.array([[52,515,15,3],[351,5153,335,35],[41,541,5431,5321]])
print(i[2,2:3])
print(i[0:4,0:1])

print(np.shape(i))  #Shape
print(np.size(i))   #Size or array
print(np.ndim(i))   # Dimensions of array
print(i.dtype)
