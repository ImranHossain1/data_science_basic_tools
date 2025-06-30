import pandas as pd
data= {
    "Time": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Value": [10, 20, None, 40, 50, 60, 70, None, 90, 100]
    }
df= pd.DataFrame(data)
print("Before interpolation:\n", df)

print("\nAfter interpolation:")
df["Value"]= df["Value"].interpolate(method='linear')
print(df)


"""
1. timer series data
2. numeric data with trends
3. avoid dropping rows
4. preserve data integrity

"""