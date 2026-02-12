
# Functions is a set of code in pyhton which is used again and again once it is created

def hello():
    print("Hello Bhai Ji")
hello()

def add():
    a = int(input("Enter Any Number:"))
    b = int(input("Enter Any Number:")) 
    print(a + b)
add()

# Parameters and Arguments

#---- Parameters are the variables which are written inside the parenthese
# with the nme of function

#---- Arguments are the values passed to the parenthese while calling the function.

def multiply(x,y,z):  # x y z are parameters
    print(x*y*z)
multiply(3124,34,32434)  # These numbers are arguments
multiply(2,2,2)


def hello(name):
    print("My name is ", name)
    print(name,"is a good boy")
    print(name,"good friends name is Sanjay and Minakshi")
hello("Arpit")




def hiii(x,y):
    print(x**y)
hiii(2,900)