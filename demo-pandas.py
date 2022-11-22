"""
Ukazka knihoven pandas a matplotlib
Data z CHMU Klementinum
"""
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('PKLM_pro_portal.csv', sep=",")

#print(df)
#print(df.info())
print(df.columns)
print(df['rok'])

print(df['T-AVG'].describe())

# Filter
filt = (df['rok']==2021) & (df['den']==2)
print(df.loc[filt])

mesic = df.loc[filt, 'měsíc']
teplota = df.loc[filt, 'T-AVG']

print(teplota)

plt.subplot(2,1,1)
plt.plot(mesic, teplota, label='průměr')
plt.plot(mesic, df.loc[filt, 'TMA'], label='maximum')
plt.title('ČHMÚ, Praha Klementinum \n Rok 2021, 2. den v měsíci')
plt.xlabel('Měsic')
plt.ylabel('Teplota [C]')
plt.legend()

mesic_prumer = df.groupby('měsíc').mean()
print(mesic_prumer)

plt.subplot(2,1,2)
plt.title('Průměr přes všechny roky')
plt.plot(mesic_prumer['T-AVG'])
plt.plot(mesic_prumer['TMA'])
plt.xlabel('Měsic')
plt.ylabel('Teplota [C]')
plt.tight_layout()

plt.show()

