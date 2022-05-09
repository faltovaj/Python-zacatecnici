"""
Cykly - for cyklus
Ukazka pro retezec
- iterace pres jednotlive znaky
- iterace pres index
Generator rozsahu: range
"""
print("====== Iterace pres znaky ========")
mujRetezec = "ahoj"
print(f"Zadali jsme retezec: {mujRetezec}")
# Pruchod retezcem znak po znaku
for p in mujRetezec:
    print("Pismeno: ", p)

print("======= Iterace pomoci indexu ======")
# Budeme prochazet retezec pomoci indexu znaku
# - prvni znak ma index 0, druhy 1, ..., posledni ma index = delka retezce - 1
# Zjistime delku retezce
delka = len(mujRetezec)
# Pouzijeme generator rozsahu range
# range(0,4): vygeneruje cisla 0, 1, 2, 3
# - dolni mez do rozsahu patri, horni ne!
# range(0, delka): vygeneruje cisla 0, 1, ..., delka -1
# range(a, b): vygeneruje cisla a, a+1, ..., b-1
# range(delka) je stejne jako range(0, delka)
for i in range(0, delka):
    print(f"Pismeno na pozici {i} je {mujRetezec[i]}")

print("======== Uloha na for-cyklus ==========")
# Ukol: Zjistete, na jake pozici jsou cisla v retezci (pokud tam nejaka jsou)
dalsiRetezec = "ah1oj23"
print(f"Zadali jsme tento retezec: {dalsiRetezec}")
# Budeme prochazet retezec pomoci indexu
# range(delka) je kratsi zapis pro range(0,delka)
for i in range(len(dalsiRetezec)):
    # zkontrolujeme, jestli je znak cislo
    if dalsiRetezec[i].isdigit():
        # pokud ano, vypiseme pozici (i+1) a cislo
        print(f"Cislice na pozici {i+1} je {dalsiRetezec[i]}")