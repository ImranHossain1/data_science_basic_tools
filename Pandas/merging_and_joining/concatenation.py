"""
vertically (row-wise) 
horizontally (column-wise) using the `concat()` function.

pd.concat([df1, df2], axis=0, ignore_index=True)  # Concatenate vertically (row-wise)

"""

import pandas as pd
# Sample DataFrames
df_region1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
    })

df_region2 = pd.DataFrame({
    'CustomerID': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank']
    })
 # Concatenating DataFrames vertically (row-wise)
df_concat_vertical = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print("Concatenated DataFrame (vertical):") 
print(df_concat_vertical)

# Concatenating DataFrames horizontally (column-wise)
df_concat_horizontal = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print("\nConcatenated DataFrame (horizontal):")
print(df_concat_horizontal)

