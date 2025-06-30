# sorting data
# sorting data in 1 column sort_values()
# df.sort_values(by='Column name', ascending=False, inplace=True)
import pandas as pd
# Sample DataFrame
data= {
    "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    "Age" : [25, 30, 35, 40, 28, 32, 45, 29, 38, 50, 27, 33],
    "Salary" : [70000, 80000, 120000, 90000, 95000, 110000, 105000, 115000, 85000, 95000, 100000, 75000]
}

df= pd.DataFrame(data)
df.sort_values(by='Age', ascending=True, inplace=True)  # Sort by 'Age' in ascending order
print("DataFrame sorted by Age in ascending order:")
print(df)