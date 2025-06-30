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
# selecting rows based on a condition
print("\nRows where Salary is greater than 90000:")   
filtered_df = df[df['Salary'] > 90000]
print(filtered_df)

# combining multiple conditions to filter rows
print("\nRows where Age is greater than 30 and Salary is less than 100000:")
filtered_df_combined = df[(df['Age'] > 30) & (df['Salary'] < 100000)]
print(filtered_df_combined)

# using OR condition to filter rows
print("\nRows where Age is greater than 35 or Performance Score is greater than 90:")
filered_or = df[(df['Age'] > 35) | (df['Performance_Score'] > 90)]
print(filered_or)