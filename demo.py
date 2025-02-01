import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df)

# sort = df.sort_values('Name')

# print(sort)
# print(df.iloc[1])

# print(df.iloc[2,1])

# iterarting through each rows

# for index, row in df.iterrows():
#     print (index, row['Name'])

# Fire type pokemon
# fire_type = df.loc[df['Type 1'] == 'Fire']
# print(fire_type)

# sort_t = df.sort_values(['Type 1', 'HP'], ascending= [1,0])
# print(sort_t)

# Adding a new coloumn 

# df['Total'] = df.iloc[:, 4:10].sum(axis = 1)

# cols = list(df.columns.values)
# df = df[cols[0:10] + [cols[-1]] + cols[10:]]

# print(df)

# Saving and extracting the Data.

# df.to_csv('New_pokemon_data.csv')


# Print all pokemon which are not mega

# No_mega = df.loc[~df['Name'].str.contains('Mega')]
# print(No_mega)

# Print all pokemon name starts with Pi.
import re

pi = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(pi)