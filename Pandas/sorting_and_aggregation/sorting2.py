# Sorting a DataFrame by multiple columns with different orders
# df.sort_values(by=['Age', 'Salary'], ascending=[True, False], inplace=True)  # Sort by 'Age' ascending and 'Salary' descending

import pandas as pd
# Sample DataFrame
data= {
    "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    "Age" : [30, 30, 35, 40, 28, 32, 45, 29, 38, 50, 27, 33],
    "Salary" : [70000, 80000, 120000, 90000, 95000, 110000, 105000, 115000, 85000, 95000, 100000, 75000]
}

df= pd.DataFrame(data)
# Sort by 'Age' in ascending order and 'Salary' in descending order
df.sort_values(by=['Age', 'Salary'], ascending=[True, True], inplace=True)
print("DataFrame sorted by Age in ascending order and Salary in descending order:")
print(df)