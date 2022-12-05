"""
Prace s adresari
Knihovny os, glob
"""

import os
import glob

# Aktualni adresar
print('Adresar, ve kterem pracuji:', os.getcwd())
# Vypis vsech souboru v adresari - dostaneme seznam jmen
print('Co mam v adresari:', os.listdir())

# Kolik je pythonvskych souboru v aktualnim adresari?
soubory = os.listdir()
# Pocet vsech souboru
print('Pocet souboru:', len(soubory))
# Spocteme vsechny soubory (bez tech zacinajicich na .) a pythonovske soubory
pocetSouboru = 0
pocetPythonSouboru = 0
# Cyklus pres vsechny polozky v seznamu soubory
for p in soubory:
    # Nechceme nazvy zacinajici .
    if p[0]!='.':
        pocetSouboru += 1
        # Zkontrolujeme posledni 3 znaky: pokud to je .py, pak mame pythonovsky soubor
        if len(p) > 3:
            poslTri = p[-3] + p[-2] + p[-1]
            if poslTri == '.py':
                pocetPythonSouboru += 1
print('Pocet Python souboru', pocetPythonSouboru)

# Vypis vsech souboru v adresari zacinajici na kl a koncici .py
# * nahrazuje libovolny pocet znaku
path = os.getcwd() + '/kl*.py'
print(path)
for file in glob.glob(path):
    print('Cesta', file)

# Rekursivni prohledavani: ** nahrazuje jeden nebo vice adresaru
# Hledame vsechny pythonovske soubory v podadresarich
path = '/home/jana/Programovani/Python/**/*.py'
for file in glob.glob(path, recursive = True):
    print('Cesta', file)

# Vytvoreni noveho adresare
os.mkdir('NovyAdresar')
# Prejmenovani adresare
os.rename('parse.py', 'parseNew.py')
