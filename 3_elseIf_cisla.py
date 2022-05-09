"""
Podminky: else-if, else-elif-if
1. Zjistete, zda je dane cislo sude
2. Porovnani dvou cisel
- Nactete dve cisla z klavesnice
- Urcete, jestli je prvni cislo mensi, vetsi nebo rovno druhemu
"""

print("======== SUDE NEBO LICHE CISLO? ===========")
# Retezec ze vstupu pretypujeme na cele cislo (int)
cislo = int(input("Zadejte cislo: "))
# Podminka IF-ELSE:
# - Pokud podminka plati, provede se prvni vetev, pokud neplati, provede se druha
# - Znak == pro 'je rovno' (jedno = pro prirazeni hodnoty)
# Syntaxe: odsazeni je nutne!
# - K odsazeni pouzijte tabulator nebo nekolik mezer
# - POZOR: nemichejte tabulatory a mezery (problemy pri behu programu)
# Algoritmus: Pokud po deleni dvema neni zadny zbytek, pak je cislo sude
if cislo%2 == 0:
    # Vypis pomoci fstring
    print(f"Cislo {cislo} je sude.")
# V opacnem pripade jde o cislo liche
else:
    print(f"Cislo {cislo} je liche.")

print("======== POROVNANI DVOU CISEL ===========")
# Podminka IF-ELIF-IF
cisloA = int(input("Zadejte 1. cislo: "))
cisloB = int(input("Zadejte 2. cislo: "))
# Prvni vetev: pokud je cisloA vetsi nez cisloB
if cisloA>cisloB:
    print(f"Cislo {cisloA} je vetsi nez cislo {cisloB}.")
# Druha vetev: pokud cisloA neni vetsi nez cisloB, ale cisloA je rovno cislu B
elif cisloA==cisloB:
    print(f"Cislo {cisloA} je rovno cislu {cisloB}.")
# Treti vetev: pokud neplati prvni ani druha podminka, provede se treti vetev:
# cisloA je mensi nez cisloB
else:
    print(f"Cislo {cisloA} je mensi nez cislo {cisloB}.")