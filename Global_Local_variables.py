# Local Variable & Global Variable
# Local Variable are restricted to only one block of code and cannot be changed
#      changed throughout program whereas in global variables it can be changed


x = 45
print("First Variable is",x)
def hii():
    x = 324
    return x
print(hii())    # Local variable


print(x)         # value outside code


x = 34
def hello():
    global x
    x = 100
    return x
print(hello())

print(x)