import pandas as pd

df = pd.read_csv('pokemon_data.csv')

sort = df.sort_values('Name')

# print(sort)
# print(df.iloc[1])

# print(df.iloc[2,1])

# iterarting through each rows

# for index, row in df.iterrows():
#     print (index, row['Name'])

# Fire type pokemon
# fire_type = df.loc[df['Type 1'] == 'Fire']
# print(fire_type)

sort_t = df.sort_values(['Type 1', 'HP'], ascending= [1,0])
print(sort_t)


