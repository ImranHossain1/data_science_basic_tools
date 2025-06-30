# 10, 20 , NaN, 40, 50, 60, 70, 80, 90, 100, 110, 120
# 1. preserve data integrity
# 2. smooth trends
# 3. avoid data loss
# interpolate()

import pandas as pd
data = {
    'Name': ['Alice', "Imran", 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
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

df.interpolate(method='linear',axis=0,inplace=True)  # Interpolate missing values using linear method
print("\nDataFrame after interpolation:")
print(df)