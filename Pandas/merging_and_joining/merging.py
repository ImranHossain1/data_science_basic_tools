# pd.merge(df1, df2, on='column_name', how='type of join')  
import pandas as pd
# customer dataframe
data1 = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],    
})
# order dataframe
data2 = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 2, 5],
    'OrderAmount': [250, 150, 200, 300]
})



# merge the dataframes on CustomerID using an inner join
df_merged_inner = pd.merge(data1, data2, how='inner', on='CustomerID')
print("Merged DataFrame:")
print(df_merged_inner)

# merge the dataframes on CustomerID using a right join
df_merged_outer = pd.merge(data1, data2, how='outer', on='CustomerID')
print("Merged DataFrame:")
print(df_merged_outer)

# merge the dataframes on CustomerID using a left join
df_merged_left = pd.merge(data1, data2, how='left', on='CustomerID')
print("Merged DataFrame:")
print(df_merged_left)

# merge the dataframes on CustomerID using a right join
df_merged_right = pd.merge(data1, data2, how='right', on='CustomerID')
print("Merged DataFrame:")
print(df_merged_right)

# merge the dataframes on CustomerID using a cross join
df_merged_cross = pd.merge(data1, data2, how='cross')
print("Merged DataFrame:")
print(df_merged_cross)