"""
Ukazka datoveho typu seznam (list)
- Operace s retezci
- Ukazka metod definovanych pro retezce
- Prochazeni retezce po znacich (for cyklus)
"""
# Seznam ma typicky nekolik polozek
# - zadava se do hranatych zavorek, polozky jsou oddelene carkou
# - polozky mohou byt ruznych typu
print("========= Seznamy =========")
# Nadefinujeme si seznam, ktery ma na zacatku 3 polozky
seznam = ["jablko","pomeranc","hruska"]
print("Mame tento seznam ", seznam)
# Pocet prvku seznamu - len
print(f"Pocet prvku seznamu je {len(seznam)}")
# Vypiseme druhou polozku (= polozka s indexem 1)
print(f"Polozka s indexem 1: {seznam[1]}")
# Pridani nove polozky na konec seznamu pomoci append
# V nasem pripade dostaneme seznam seznam = ["jablko","pomeranc","hruska", "banan"]
seznam.append("banan")
# Seznam si vypiseme
print("Pridani polozky", seznam)
# Zalozeni prazdneho seznamu (s tim se muzete casto setkat)
prazdnySeznam = []

print("======= Odebirani ze seznamu - remove, pop ========")
# Odebrani polozky: remove - odebere polozku podle nazvu
# Nas priklad: odebere se polozka "hruska", zustane ["jablko","pomeranc", "banan"]
seznam.remove("hruska")
print("Po odebrani polozky", seznam)
# Odebrani polozky: pop - odebere polozku s danym indexem
# Nas priklad: odebere se polozka s indexem 2, zustane ["jablko", "pomeranc"]
seznam.pop(2)
print("Po dalsim odebrani", seznam)

print("===== Pridani polozky doprostred seznamu ======== ")
# vkladani prvku: insert - vlozi polozka na misto s danym indexem,
# dalsi polozky se odsunou
# Nas priklad: na pozici s indexem 1 se vlozi "hrozny",
# budeme mit seznam ['jablko', 'hrozny', 'pomeranc']
seznam.insert(1, "hrozny")
print(seznam)

print("====== Razeni seznamu ======== ")
# Serazeni seznamu pomoci sorted
# - razeni jako ve slovniku
# - pro cisla podle velikosti (nesmite mit typ retezec)
print(f"Serazeny seznam: {sorted(seznam)}")

print("====== For cyklus pro seznamy ======== ")
# Obdobne jako pro retezce, i v seznamy muzeme prochazet po prvcich
# Cyklus pres index jde take pouzit - for i in range(len(seznam))
for prvek in seznam:
    print(f"Polozka: {prvek}")