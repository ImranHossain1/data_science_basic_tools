# 1. select specific columns from a DataFrame
# 2. filter rows based on a condition
# 3. combine multiple conditions to filter rows

# 1. square brackets
# 2. boolean condition

# selecting columns
# 1. a series of columns
# 2. data frame multiple columns of a Data
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
    'Performance Score': [85, 90, 95, 80, 88, 92, 87, 93, 89, 91, 84, 86]
}

df = pd.DataFrame(data)
# display dataframe
print("Sample DataFrame:")
print(df)

print("Names (Single Column and return series):")
# selecting a single column returns a Series
print(df['Name'])

# selecting multiple columns returns a DataFrame
subset = df[['Name', 'Age', 'City']]
print("\nSubset of DataFrame (Multiple Columns):")
print(subset)

