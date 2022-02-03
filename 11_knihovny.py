"""
Ukazka prace s knihovnami
- modul math (matematicke operace)
- modul datetime (datum, cas)
- modul random (pseudonahodna cisla, vybery)
    - priklad: hody kostkou
"""
print("========= Modul math ==========")
# Nejprve musime knihovnu nacist: import
import math
# Volani metod knihovny pres nazevKnihovny.metoda()
print("Sinus: ", math.sin(0))       # argument funkce sin je v radianech
print("Pi: ", math.pi)              # hodnota konstanty pi
print("Mocnina: ", math.pow(2,4))   # dve na ctvrtou
# Dalsi moznosti volani knihoven
# import math as m          # pri volani metod z knihovny budeme psat m.metoda()
# print("Sinus: ", m.sin(0))
# from math import sin      # funkci sin volame bez math.
# print("Sinus: ", sin(0))
# from math import *        # zkopirovani obsahu cele knihovny - POZOR: pro
# print("Sinus: ", sin(0))  # velke knihovny muze zahltit pamet
# print("Pi: ", pi)         # pak volame vse bez math.

print("======== Modul datetime =========")
#import datetime
from datetime import datetime
from datetime import date
# Dnesni datum
datum = date.today()
# Cas prave ted
print("Cas: hodina ", datetime.now().hour, " minuta ", datetime.now().minute)
print("Datum: ", datum)
# strptime, strftime: datum v jinem formatu - najdete v dokumentaci, Google

print("====== Modul random =======")
import random
print(f"Nahodne cislo v rozsahu 0 - 1: {random.random()}")
print(f"Nahodne cislo v rozsahu 1 - 10: {random.uniform(1,10)}")
print(f"Nahodne cele cislo mezi 1 - 10: {random.randint(1,10)}")
print("Nahodny vyber ze seznamu:", random.choice(["a","b","c"]))

print("===== Hody kostkou (random) ======")
# Uloha: emulace hodu kostkou
# Nagenerujte hody kostkou a spoctete, kolikrat padlo ktere cislo
# Pocty: promenna typu seznam
# pocty[0] - kolikrat padla 1
# pocty[1] - kolikrat padla 2
# ... ,pocty[5] - kolikrat padlo 6
pocty = [0,0,0,0,0,0]
# Pocet hodu
pocetHodu = 10000
for i in range(pocetHodu):
    # Vygenerujeme nahodne cele cislo v rozsahu 1 az 6
    hod = random.randint(1,6)
    # hod prevedeme na index v promenne pocty: index = hod - 1
    pocty[hod-1] += 1
# Vypiseme, kolikrat padlo ktere cislo
for i in range(6):
    print(f"{i+1} padla {pocty[i]}-krat.")