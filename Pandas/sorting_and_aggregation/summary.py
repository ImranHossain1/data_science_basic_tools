# df["Column_name"].mean()  # Calculate the mean of a specific column
# df["Column_name"].sum()  # Calculate the sum of a specific column
# df["Column_name"].max()  # Find the maximum value in a specific column
# df["Column_name"].min()  # Find the minimum value in a specific column
# df["Column_name"].count()  # Count the number of non-null values in a specific column
# df["Column_name"].std()  # Calculate the standard deviation of a specific column
# df["Column_name"].var()  # Calculate the variance of a specific column
import pandas as pd
# Sample DataFrame
data= {
    "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kathy', 'Laura'],
    "Age" : [30, 30, 35, 40, 28, 32, 45, 29, 38, 50, 27, 33],
    "Salary" : [70000, 80000, 120000, 90000, 95000, 110000, 105000, 115000, 85000, 95000, 100000, 75000]
}

df= pd.DataFrame(data)

avg_salary = df["Salary"].mean()  # Calculate the mean of the 'Salary' column
print("Average Salary:", avg_salary)