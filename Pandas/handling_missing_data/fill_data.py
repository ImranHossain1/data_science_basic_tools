# fillna(value, inplace=True) method is used to fill missing values with a specified value.

import pandas as pd
data = {
    'Name': ['Alice', None, 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    'Age': [25, None, 35, 40, 28, 32, 45, 29, 38, 50, 27, 33],
    'City': ['New York', None, 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Seattle'],
    'Salary': [70000, None, 120000, 90000, 95000,
              110000, 105000, 115000, 85000, 95000, 100000, 75000],
    'Department': ['HR', None, 'IT', 'Marketing', 'Sales',
                   'Operations', 'IT', 'Finance', 'HR', 'Marketing', 'Sales', 'Operations'],
    'Performance_Score': [85, None, 95, 80, 88, 92, 87, 93, 89, 91, 84, 86]
}

df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace=True)  # Fill missing values with 0
# print("\nDataFrame after filling missing values with 0:")
# print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill missing 'Age' with mean
df["Salary"].fillna(df["Salary"].mean(), inplace=True)  # Fill missing 'Salary' with mean
df["Performance_Score"].fillna(df["Performance_Score"].mean(), inplace=True)  # Fill missing 'Performance_Score' with mean
print(df)