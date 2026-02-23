import pandas as pd

dict = {"Names" : ["Arpit", "Harsh", "Ashish", "Keshav"],
        "Houses": ["Black", "White", "Pink", "Brown"],
        "Grades" : ["9th", "10th", "12th", "4th"]}

df1 = pd.DataFrame(dict)
print(df1)


print(pd.melt(df1,id_vars= ["Names"], value_vars= ["Houses"]))
print(pd.melt(df1,id_vars= ["Names"], value_vars= ["Houses","Grades"]))