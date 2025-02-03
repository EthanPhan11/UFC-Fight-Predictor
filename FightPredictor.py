import pandas as pd

df = pd.read_csv('fighterstats.csv')

input_name = input('enter fighter name: ')

find_name = df.loc[df['name']== input_name]

print(find_name)