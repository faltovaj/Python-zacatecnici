"""
Priklad na seznamy: evidence skladu
1. Ulozte si nekolik polozek do promenne typu seznam
2. Pridejte dalsi polozku do seznamu (pokud tam jeste neni)
- nejprve zkontrolujte, jestli jeste polozka neni v seznamu
    - pokud je, tak vypiste, ze polozku uz mame
    - pokud neni, tak ji pridejte do seznamu
"""
# Naplnime promennou sklad nekolika polozkami
sklad = ["kladivo","hrebik","sroubovak"]
# Nacteme polozku, kterou chceme do skladu pridat
novaPolozka = input("Zadejte polozku, kterou chcete pridat ")

print("===== Prohledavani seznamu for-cyklem ========")
# Zkontrolujeme, jestli polozka v seznamu jeste neni
# Zavedeme pomocnou promennou typu Boolean
# nalezeno: False - polozku jsme (jeste) nenasli; True - polozku jsme nasli
nalezeno = False
# V cyklu prochazime jednotlive prvky seznamu sklad
for p in sklad:
    # Pokud je prvek roven nasi polozce, tak nalezeno zmenime na True
    if p == novaPolozka:
        nalezeno = True
# Po zkontrolovani vsech polozek ve skladu, vime, jestli polozka
# ve skladu je nebo neni
if nalezeno == False:       # ekvivaletni s vyrazem if not nalezeno
    sklad.append(novaPolozka)
    print(f"Polozku {novaPolozka} jsem pridali do skladu.")
else:
    print(f"Polozku {novaPolozka} uz ve skladu mame.")
print(f"Obsah skladu {sklad}")

print("===== Prohledavani seznamu pomoci in ========")
# Nacteme novou polozku k pridani
dalsiPolozka = input("Zadejte polozku, kterou chcete pridat ")
# Python ma prikaz, ktery umi prohledavat seznam: in
# Pomocna promenna nalezeno
nalezeno = dalsiPolozka in sklad
if nalezeno:
    print("Polozku uz ve skladu mame.")
else:
    sklad.append(dalsiPolozka)
print(sklad)