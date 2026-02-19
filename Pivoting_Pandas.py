import pandas as pd

dict = {"Keys": ["K1","K2", "K3", "K4"],
        "Names" : ["Arpit", "Harsh", "Ashish", "Keshav"],
        "Houses": ["Black", "White", "Pink", "Brown"],
        "Grades" : ["9th", "10th", "12th", "4th"]}

df1 = pd.DataFrame(dict)
print(df1)

print(df1.pivot(index ="Keys", columns = "Names", values =["Houses","Grades"] ))
