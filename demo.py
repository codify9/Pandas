import pandas as pd

df = pd.read_csv('pokemon_data.csv')

sort = df.sort_values('Name')

# print(sort)
print(df.iloc[:5])