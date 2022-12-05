"""
Ukazka volani vlastni funkce z jineho souboru
"""

# Nacteme vse ze souboru funkce.py
from funkce import *

# Zavolame funkci sude:
# V tomto souboru zadna funkce tohoto jmena neni definovana,
# Python se podivam do importovanych knihoven, jestli ji najde tam
# -> Najde a zavola funkci sude ze souboru funkce.py
sude(int(input('Zadejte cislo: ')))
