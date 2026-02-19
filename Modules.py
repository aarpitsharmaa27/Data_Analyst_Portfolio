# Modules are the (.py), that contain set of funtions you want to include in your program


# In built modules 


import datetime    #Datetime module

x = datetime.datetime.now()     #Give live time and date
print(x)

y = datetime.datetime(2026,2,13)   
print(y.strftime("%A"))

y = datetime.datetime(2002,10,27)
print(y)
print(y.strftime("%A"))   # Shows Day
print(y.strftime("%a"))   # Shows Shimport demo

a = demo.add(334,324)
print(a)ort form of day
print(y.strftime("%B"))   # Shows Month
print(y.strftime("%m"))   # Shows Month in 1 -12
print(y.strftime("%Y"))   # Shows Year
print(y.strftime("%y"))   # Shows Last two digit of year


import random       # Random Module

x = random.randint(1,20)    # Give Random Value Everytime
print(x)

l = ["Heads", "Tails"]
x = random.choice(l)
print(x)

c = ["Stone","Paper","Scissor"]
y = random.choice(c)
print(y)

d = ["Deni", "Thane Jana"]
z = random.choice(d)
print(z)




import math       # Math Module

x = max(999,444,443)    # Highest Value
print(x)

x = min(421,513411,341)   # Minimum value
print(x)

x = pow(2,3)        # 2 raise to power 3
print(x)

x = math.sqrt(900)     #Square of 900 is 30
print(x)

x = abs(-234)       # Absolute value(- to +)
print(x)

x = math.ceil(20/3)     #Highest closest Number i.e 7
print(x)

x = math.ceil(234.4315)
print(x)

x = math.floor(20/3)       # Lowest closest Number i.e 6
print(x)

x = math.floor(152.341)
print(x)