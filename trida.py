"""
Procentualni zastoupeni devcat ve tride
Vstup:
- pocet chlapcu
- pocet devcat
Vystup:
- pocet devcat ve tride v %
"""

# Nacteme pocet chlapcu a devcat ve tride
pocetCh = int(input('Zadejte pocet chlapcu: '))
pocetD = int(input('Zadejte pocet devcat: '))

# Spocteme celkovy pocet zaku a pote procentualni zastoupeni
pocetZaku = pocetD + pocetCh
print('Devcata: ', pocetD/pocetZaku*100, '%')
# Ukazka vypisu pomoc fstring
# Co je uvedeno v {}, za to se dosadi
print(f'Devcata: {pocetD/pocetZaku} %')
# Vypis na 1 desetinne misto (.1f)
print(f'Devcata: {pocetD/pocetZaku*100:.1f} %')