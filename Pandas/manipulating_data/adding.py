import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    'Age': [25, 30, 35, 40, 28, 32, 45, 29, 38, 50, 27, 33],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Seattle'],
    'Salary': [70000, 80000, 120000, 90000, 95000,
              110000, 105000, 115000, 85000, 95000, 100000, 75000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales',
                   'Operations', 'IT', 'Finance', 'HR', 'Marketing', 'Sales', 'Operations'],
    'Performance_Score': [85, 90, 95, 80, 88, 92, 87, 93, 89, 91, 84, 86]
}

df = pd.DataFrame(data)

# display dataframe
print("Sample DataFrame:")  
print(df)

# adding a new column 
df["Bonus"]= df["Salary"] * 0.1
# display dataframe with new column
# print("\nDataFrame after adding Bonus column:")
# print(df)

# using insert() to add a new column at a specific position
# df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee_ID", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print(df)