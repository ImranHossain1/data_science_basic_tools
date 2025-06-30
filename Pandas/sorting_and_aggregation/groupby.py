import pandas as pd
# Sample DataFrame
data= {
    "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    "Age" : [30, 30, 35, 40, 28, 32, 45, 28, 38, 50, 27, 35],
    "Salary" : [70000, 80000, 120000, 90000, 95000, 110000, 105000, 115000, 85000, 95000, 100000, 75000]
}

df= pd.DataFrame(data)

grouped= df.groupby('Age')["Salary"].mean()  # Group by 'Age' column
print("Grouped DataFrame by Age with sum of Salary:")
print(grouped)
