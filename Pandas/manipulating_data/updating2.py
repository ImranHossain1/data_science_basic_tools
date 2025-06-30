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
print(df)

# increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print("\nDataFrame after increasing Salary by 5%:") 
print(df)