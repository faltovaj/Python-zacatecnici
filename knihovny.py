""""
Prace s knihovnami (neboli moduly)
- math
- random
Tyto knihovny patri mezi tzv. standardni knihovny - neni treba je doinstalovavat,
stahnou se s instalaci Pythonu
"""
print("========= Math ==========")
# Math: knihovna se zakladnimi matematickymi funkcemi a konstantami
# Knihovnu musime nejprve nacist: klicove slovo import
import math
# Metody (funkce) nebo promenne z teto knihovny pak volame pres math.nazevCoChceme
print("Sinus ", math.sin(0))
# Dalsi moznosti importovani
# 1. Z modulu naimportujeme pouze nekolik funkci
#from math import sin, cos
# Pak volame funkci primo (bez math.)
#print(sin(0))
# 2. Naimportujeme si knihovnu math jako m - misto math.nazevCoChceme piseme m.nazevCoChceme
#import math as m
#print("Sinus ", m.sin(0))
#print("Pi ", m.pi)

print()
print("======= Random =======")
# Random: knihovna na generovani (pseudo)nahodnych cisel
# Knihovnu random si nacteme jako r (usetrime si psani - misto random. budeme psat r.)
import random as r
# Nahodne desetinne cislo z rozmezi 0 az 1
print(f'Nahodne cislo (mezi 0, 1): {r.random()}')
# Nahode desetinne cislo z rozmezi 2 az 5
print(f'Nahodne cislo: {r.uniform(2, 5)}')
# Nahodne cele cislo z rozmezi 2 az 5
print(f'Nahodne cele cislo: {r.randint(2, 5)}')
# Nahodne vybere jednu polozku ze seznamu
print(f'Nahodny vyber ze seznamu: {r.choice([1, 5, 10])}')

print()
print("===== Hody kostkou ====")
# Nagenerujte 1000 hodu kostkou, kolikrat padla sestka?
# Rozsireni: Kolikrat padlo kazde cislo?
pocet6 = 0               # Pocet sestek
# Do vysledek si ulozime pocty hodu jednotlivych cisel
# Pocty hodu jednicek bude ve vysledek[0], dvojek ve vysledek[1], atd.
vysledek = [0]*6         # vysledek = [0, 0, 0, 0, 0, 0]
# Nagenerujeme 1000 hodu (for cyklus)
for i in range(1000):
    # Nahodne cislo od 1 do 6
    hod = r.randint(1,6)
    if (hod == 6):
        pocet6 += 1     # pocet6 = pocet6 + 1
    index = hod - 1     # 6: index 5, 5: index 4, ...
    vysledek[index] += 1   # vysledek[index] = vysledek[index] + 1
print('Pocet 6:', pocet6)
print('Vysledek:', vysledek)
# Vysledek muzeme uvest i v procentech
# sum - vrati soucet vsech prvku seznamu
soucet = sum(vysledek)
print('Soucet', soucet)
procenta = []
for p in vysledek:
    procenta.append(p/soucet*100)
print(procenta)
