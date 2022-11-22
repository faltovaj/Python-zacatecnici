"""
Ukazka knihovnu pandas na datech z CHMU Klementinum
"""
import pandas as pd
from matplotlib import pyplot as plt

sheets = pd.ExcelFile('PKLM_pro_portal.xlsx').sheet_names
print(sheets)

df = pd.read_excel('PKLM_pro_portal.xlsx', sheet_name='data')
# Vypis prvnich 10 radku
print(df.head(10))        # posledni radku: df.tail(10)

# Nazvy sloupcu
print('Nazvy sloupcu:', df.columns)
print(df['T-AVG'].tail(10))
print(df['T-AVG'].describe())
print('Prumerna teplota', df['T-AVG'].mean())
print('Teplota median', df['T-AVG'].median())

# Pocty hodnot
print('Mesic count', df['měsíc'].count())
print(df['měsíc'].value_counts())

# Vypis casti tabulky: TODO!!!

# Filter
filt = (df['rok']==2021) & (df['měsíc']==3)   # and, or in python -> &, | in Pandas
print(df.loc[filt])

plt.plot(df.loc[filt, 'den'], df.loc[filt, 'T-AVG'])
plt.xlabel('Den')
plt.ylabel('T-AVG')
plt.show()
plt.savefig('teplota.png')

# Rok 2021, 3. den v mesici: Zavislost min. teploty na mesici
filt = (df['rok']==2021) & (df['den']==3)   # and, or in python -> &, | in Pandas

plt.plot(df.loc[filt, 'měsíc'], df.loc[filt, 'TMI'])
plt.xlabel('Mesic')
plt.ylabel('TMI')
plt.show()
plt.savefig('teplotaTMI.png')

# 
df.loc[filt].to_excel('tabulka1.xlsx')