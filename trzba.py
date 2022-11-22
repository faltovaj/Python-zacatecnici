import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('trzba.xlsx')
print(df.columns)

print(df.info())

print("Kolik vyrobku: ", df['Polozka'].value_counts())
print("Zeme: ", df['Stat'].value_counts())

polozka = ['A1', 'A2', 'A3']
filt = df['Polozka'] == 'A1'

print(df.loc[filt])

group_polozka = df.groupby(['Polozka','Stat'])
#print('Group polozka: mean ', group_polozka['Cena'].mean())
print('Group polozka: soucet ', group_polozka['Cena'].sum())
print('Group polozka: pocet ', group_polozka['Pocet'].sum())
print('Group polozka: prumer ', group_polozka['Cena'].sum()/group_polozka['Pocet'].sum())

group_polozkaStat = df.groupby(['Polozka','Stat'])
#print('Group polozka: mean ', group_polozka['Cena'].mean())
print('Group polozkaStat: soucet ', group_polozkaStat['Cena'].sum())
print('Group polozkaStat: pocet ', group_polozkaStat['Pocet'].sum())
print('Group polozkaStat: prumer ', group_polozkaStat['Cena'].sum()/group_polozkaStat['Pocet'].sum())
