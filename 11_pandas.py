"""
Analyza dat: ukazka knihoven Pandas a Matplotlib
- Pandas: knihovna na zpracovani velkych objemu dat
- Matplotlib: knihovna ke grafickemu znazorneni
- pandas a matplotlib si musime doinstalovat: v PyCharm "Python Packages" v leve casti spodni listy - vyhledat balik podle jmena - Install (vpravo na spodni liste)  

Data z CHMU Klementinum ve formatu csv (https://www.chmi.cz/historicka-data/pocasi/praha-klementinum - odkaz Denni data ze stanice Praha Klementinum)
"""

# Naimportujeme knihovny Pandas a pyplot z Matplotlib
import pandas as pd
from matplotlib import pyplot as plt

# Nacteme data ze csv souboru jako tzv. DataFrame
df = pd.read_csv('PKLM_pro_portal.csv')
# Pokud mate problemy s prectenim dat:
# - pridejte moznost sep=";" (znak, ktery pouziva csv jako separator)
# - pridejte moznost encoding="utf8" (kodovani souboru muze byt jine, nez je defaultni na vasem operacnim systemu)
#df = pd.read_csv('PKLM_pro_portal.csv', sep=';', encoding='utf8')

# Vypiseme si dat
print(df)
# Vypiseme informace o datech
print(df.info())
# Vypiseme nazvy sloupcu
print(df.columns)
# Vypiseme pouze sloupec 'rok' v zahlavi
print(df['rok'])

# Statisticke informace o datech ve sloupci 'T-AVG' (denni prumerna teplota)
print(df['T-AVG'].describe())

# Filtrovani dat: Pouze data z roku 2021 a druhy den v mesici
# &: logicke "a zaroven" / "and"
filt = (df['rok']==2021) & (df['den']==2)
# Vypiseme pouze radky odpovidajici filtru
print(df.loc[filt])

# Pouzijeme filtr a do promenne mesic dosadime informace ze sloupce 'mesic'
mesic = df.loc[filt, 'měsíc']
# Filtrujeme a do promenne teplota dosadime informace ze sloupce 'T-AVG'
teplota = df.loc[filt, 'T-AVG']
# Vypiseme, co je v promenne teplota
print(teplota)

# Data sdruzime do skupiny podle hodnot ve sloupci 'mesic' (groupby) a urcime jejich prumer (mean)
# - dostaneme prumer pres vsechny roky a vsechny dny v mesici
mesic_prumer = df.groupby('měsíc').mean()
# Vypiseme prumerne hodnoty pro 12 mesicu
print(mesic_prumer)

# Data vykreslime pomoci knihovny Matplotlib
# subplot(2, 1, 1): rozdeli vykreslovaci okno na 2 radky a 1 sloupec, vykresli 1. obrazek (1)
plt.subplot(2,1,1)
# Graf zavislosti prumerne teploty 2. dne v mesici roku 2021 na mesici
# label: co se zobrazi v legende (nepovinny parametr)
plt.plot(mesic, teplota, label='prumer')
# Zavislost pro maximalni denni teplotu (sloupec 'TMA')
plt.plot(mesic, df.loc[filt, 'TMA'], label='maximum')
# Grafu priradime nazev
plt.title('Graf teploty')
# Oznacime osy
plt.xlabel('Mesic')
plt.ylabel('Teplota')
# Vykreslime legendu
plt.legend()

# Vykresleni prumerne a maximalni teploty - prumer pres vsechny roky a vsechny dny v mesici, zavislost na mesici
plt.subplot(2,1,2)
plt.plot(mesic_prumer['T-AVG'])
plt.plot(mesic_prumer['TMA'])
# tight_layout pro lepsi prostorove umisteni
plt.tight_layout()
# Obrazek ulozime
plt.savefig("fig.pdf")

# show: obrazek vykresli na obrazovku!!!
plt.show()
