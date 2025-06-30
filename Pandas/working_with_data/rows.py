# head() tail() and sample() are used to view data in a DataFrame.
import pandas as pd
df = pd.read_json("D:\dataScience\Pandas\material\sample_Data.json")

print(df.head())  # Display the first 5 rows of the DataFrame

print(df.tail())  # Display the last 5 rows of the DataFrame