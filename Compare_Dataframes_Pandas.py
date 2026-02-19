import pandas as pd

dict = {"Fruits" : ["Apple","Mango", "Papaya", "Banana"],
         "Price" : [100,200,150,300],
         "Quantity" : [2,5,6,3]}

df1 = pd.DataFrame(dict)
print(df1)

df2 = df1.copy()
print(df2)

df2.loc[0,"Price"] = 200  # Changing df2 values
df2.loc[1,"Price"] = 180
df2.loc[3, "Price"] = 100
print(df2)

df2.loc[0, "Quantity"] = 1
df2.loc[1, "Quantity"] = 3
df2.loc[2, "Quantity"] = 4
print(df2)


print(df1.compare(df2))     # Compare Changed and unchanged values

print(df1.compare(df2, align_axis= 0))

print(df1.compare(df2, align_axis= 1))