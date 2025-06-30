import pandas as pd
import numpy as np

index = "r1 r2 r3 r4 r5 r6 r7 r8 r9 r10".split()
columns = "c1 c2 c3 c4 c5 c6 c7 c8 c9 c10".split()

print(index)
print(columns)

array_2d = np.arange(0, 100).reshape(10, 10)
df = pd.DataFrame(array_2d, index=index, columns=columns)
print(df[["c1", "c2", "c3"]])  # Display specific columns 

df["c11"] = df["c1"] + df["c2"]
print(df)

df.drop("c11", axis=1, inplace=True)  # Drop the column c11
print(df)