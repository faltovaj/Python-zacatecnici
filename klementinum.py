"""
Ukazka analyzy dat s vyuzitim knihovny pandas
K uloze je potreba mit nainstalovane nasledujici knihovny
- pandas
- matplotlib
- xlwt
- openpyxl
- xlrd
Posledni 3 knihovny jsou potreba kvuli praci se soubory Excel

Analyzovana data jsou data z CHMU, stanice Klementinum
https://www.chmi.cz/historicka-data/pocasi/praha-klementinum
(Denní data ze stanice Praha Klementinum (soubor ke stažení).)
"""
# Nacteni knihoven
import pandas as pd
from matplotlib import pyplot as plt
# Vypiseme si nazvy listu v excelovskem souboru
sheets = pd.ExcelFile("PKLM_pro_portal.xlsx").sheet_names
print(sheets)

# Naceteme data z listu s nazvem data
df = pd.read_excel('PKLM_pro_portal.xlsx', sheet_name= 'data')

#print('Info: ', df.info())

# Vypiseme si nazvy
print(df.columns)

# Nazvy sloupcu
print('Nazvy sloupcu:', df.columns)
# tail(10): vypis poslednich 10-ti radku
# head(10): vypis prvnich 10-ti radku
print(df['T-AVG'].tail(10))
# Vypsani statistickych udaju o prumerne teplote
print(df['T-AVG'].describe())
# Prumerna hodnota ve sloupci 'T-AVG' (prumerna teplota)
print('Prumerna teplota', df['T-AVG'].mean())
# Median
print('Teplota median', df['T-AVG'].median())

# Pocty hodnot
print('Mesic count', df['měsíc'].count())
# Kolikrat je zastoupena kazda hodnota ve sloupci 'měsíc'
print(df['měsíc'].value_counts())

# Filter
filt = (df['rok']==2021) & (df['měsíc']==3)   # and, or in python -> &, | in Pandas
# Vypiseme data, co splnuji podminku (filter)
print(df.loc[filt])

# Vykresleni obrazku
# Vykreslime zavislost prumerne, minimalni a maximalni teploty na dnu
# v mesici breznu v roce 2021
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'T-AVG'])
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'TMI'])
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'TMA'])
# Legenda
plt.legend(['T-AVG', 'TMI', 'TMA'])     # legenda
# Popis os
plt.xlabel('Den')
plt.ylabel('T')
plt.show()
# Ulozeni obrazku
plt.savefig('teplota.png')

# Zapis vyfiltrovanych dat do Excelu
df.loc[filt].to_excel('tabulka1.xlsx')

# Novy filter: hodnoty z roku 2021
filt = df['rok'] == 2021
# Vypsani pouze sloupcu prumerna, maximalni a minimalni teplota v roce 2021
print(df.loc[filt, ['T-AVG', 'TMA', 'TMI']])

# Deleni po skupinach
group_mesic = df.groupby('měsíc')
# Prumerna teplota v kazdem mesici (nezavisle na roce a dnech)
print(group_mesic['T-AVG'].mean())
# Prumerna teplota v breznu - obsazeno v predeslem prikazu
filt = df['měsíc'] == 3
print('Prumerna teplota v 3. mesici: ', df.loc[filt, ['T-AVG']].mean())

# Vykresleni zavislosti mesicni prumerne teploty
#plt.plot(group_mesic['měsíc'].mean(), group_mesic['T-AVG'].mean())
plt.plot(group_mesic['T-AVG'].mean())
# Popisky os
plt.xlabel('Mesic')
plt.ylabel('T')
# Vykresleni
plt.show()

# Ukol: Prumerna rocni teplota
group_rok = df.groupby('rok')
print(group_rok['T-AVG'].mean())
# Test: Prumerna teplota v roce 2021
filt = df['rok'] == 2021
print('Prumerna teplota v roce 2021: ', df.loc[filt, ['T-AVG']].mean())

# Vykreslime zavislost prumerne rocni teploty
#plt.plot(group_mesic['měsíc'].mean(), group_mesic['T-AVG'].mean())
plt.plot(group_rok['T-AVG'].mean())
plt.title('Prumerna rocni teplota')
plt.xlabel('Rok')
plt.ylabel('T')
plt.show()
