import pandas as pd
from matplotlib import pyplot as plt

sheets = pd.ExcelFile("PKLM_pro_portal.xlsx").sheet_names
print(sheets)

df = pd.read_excel('PKLM_pro_portal.xlsx', sheet_name= 'data')

#print('Info: ', df.info())

print(df.columns)

#print(df['měsíc'])
#print(df['měsíc'].count())
#print(df['měsíc'].value_counts())
print('Info: ', df['T-AVG'].describe())
print('Mean: ', df['T-AVG'].mean())
print('Median: ', df['T-AVG'].median())

filt = df['rok'] == 2021
print(df.loc[filt, ['T-AVG', 'TMA', 'TMI']])

group_mesic = df.groupby('měsíc')

plt.subplot(2,1,2)
plt.title('Průměr přes všechny roky')
plt.plot(group_mesic['T-AVG'].mean())
plt.plot(group_mesic['TMA'].mean())
plt.xlabel('Měsic')
plt.ylabel('Teplota [C]')
plt.tight_layout()

plt.show()