# NaN (not a number)
# None (for object data types)

# isnull() and notnull() methods
# true= NaN is missing
# false= value is present

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
# Display the DataFrame
print("Sample DataFrame with Missing Values:")
print(df.isnull().sum())  # Display boolean DataFrame indicating missing values