"""
Automat na mince verze 2 s vyuzitim funkci a datoveho typu seznam
"""

# Funkce deleni mi rekne (vrati),
# kolik maximalne minci o nominalni hodnote hodnota se vejde do sumy castka
def deleni(castka, hodnota):
    pocet = castka//hodnota
    return pocet

# Funkce zbytek mi rekne (vrati),
# kolik bude zbytek po odecteni minci hodnoty hodnota z castky
def zbytek(castka, hodnota):
    vracime = castka%hodnota
    return vracime

# Do promenne penize si ulozim castku na rozdeleni
penize = int(input('Zadejte castku: '))

# Hodnoty minci si ulozim do seznamu (od nejvetsi po nejmensi)
# Pred seznam muzu snadno iterovat pomoci for cyklu
mince = [50, 20, 10, 5, 2, 1]
# Do vysledku si budu ukladat kolik minci ktere hodnoty budu potrebovat
# (vysledek[0] - kolik 50-ti Kc, vysledek[1] - kolik 20-ti Kc, atd.
# index v seznamu vysledek odpovida prislusne minci v seznamu mince se stejnym indexem
vysledek = [0, 0, 0, 0, 0, 0]

# Iterace pres jednotlive hodnoty minci
for i in range(len(mince)):
    # Vyuziji funkci deleni s parametry penize a mince[i]
    pocet = deleni(penize, mince[i])
    vysledek[i] = pocet
    print('Pocet', mince[i], 'je', vysledek[i])
    # Pro dalsi iteraci musim promennou penize snizit o uz vyplacenou hodnotu
    penize = zbytek(penize, mince[i])

