## Return Keyword in python is used to exit a function and return
# the value of the function

def hello():
    return("hello Bhaiji")

print(hello())


def add(x,y):
    return("The addition of two numbers is", x+y)

print(add(900,322))



# Recursion means a function can call itslef



def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(-35353))


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(90))
