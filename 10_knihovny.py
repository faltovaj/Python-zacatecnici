"""
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
# 1. Z modulu naimportujeme pouze dve funkce
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
print("===== Hody sestkou ====")
# Uloha Hody kostkou: Nagenerujte hody kostkou a spoctete, kolikrat padla sestka
# (nebo kolikrat padlo ktere cislo)
# pocitadlo: promenna, kam si ulozime pocet padnutych sestek. Na zacatku mame 0 sestek.
pocitadlo = 0
# pocty: seznam delky 6: pocty[0] - pocet jednicek, pocty[1] - pocet dvojek, ..., pocty[5] - pocet sestek
pocty = [0]*6  # pocty = [0,0,0,0,0,0]
N = int(input("Kolikrat chcete hazet "))
# Cyklus bezi N-krat (N-krat vygenerujeme nahodne cislo mezi 1 a 6
for i in range(N):
    # hod: nahodne cele cislo mezi 1 a 6
    hod = r.randint(1,6)
    # Pokud padla sestka, zvysime pocet sestek o 1
    if hod == 6:
        pocitadlo += 1    # pocitadlo = pocitadlo + 1
    # Ted zapocitame vsechny hody: Cislo, ktere padlo, prevedeme na index v seznamu pocty
    index = hod - 1       # jednicka - index 0, dvojka - index 1, ...
    pocty[index] += 1     # prislusnou polozku v seznamu zvetsime o 1
print("Sestka padla ", pocitadlo, "krat")
print("Kolikrat co padlo: ", pocty)
