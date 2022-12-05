"""
Prace se soubory:
- otevreni souboru k zapisu/ke cteni
- cteni souboru po radcich
- zapis do souboru
- analyza poctu radku a znaku v souboru
"""

# Urcete pocet radku a pocet znaku v souboru
def projdiSoubor(filename):
    # Otevreni souboru, na konci prace se soubor automaticky zavre
    # 'r' - soubor otevreny ke cteni, 'w' - soubor otevreny k zapisu (prepis uz existujiciho)
    # 'a' - zapis na konec souboru
    with open(filename, 'r') as f:
        # Na zacatku vynulujeme pocty radku a znaku
        pocetRadku = 0
        pocetZnaku = 0

        # Soubor cteme radek po radku
        for radek in f:
            #print(radek)
            # Radek rozdelime na jednotliva slova (podle mezer)
            # slova jsou retezec slov na radce
            slova = radek.split()
            # Pokud neni radek prazdny, pricteme ho do poctu radku
            if len(slova) != 0:           #if slova != []:
                pocetRadku += 1
                # Projdeme seznam slov a spocitame delku jednotlivych polozek
                for p in slova:
                    pocetZnaku += len(p)
    # Vypis vysledku
    #print(f'Pocet radku v souboru {filename} je {pocetRadku}')
    #print(f'Pocet znaku v souboru {filename} je {pocetZnaku}')
    # Funkce vrati pocetRadku a pocetZnaku
    # Vraceni n-tice (tuple) - obdobna manipulace jako se seznamy
    # n-tice jsou vhodne, pokud dopredu zname pocet prvku a nebudeme prvky v prubehu menit
    # napr. mereni a jeho chyba, souradnice v 3D, vyrobek a jeho cena
    #return pocetRadku, pocetZnaku
    # Vraceni dvou hodnot pomoci seznamu
    return [pocetRadku, pocetZnaku]

if __name__ == '__main__':
    # Zavolame funkci projdiSoubor na soubor automat.py
    pocty = projdiSoubor('automat.py')
    # Jaky je typ promenne, kterou vraci nase funkce?
    print('Funkce vraci tento typ', type(pocty))
    # Vysledky vypiseme na obrazovku
    print(f'Pocet radku v souboru je {pocty[0]}')
    print(f'Pocet radku v souboru je {pocty[1]}')
    # Vysledky zapiseme do souboru zapis.txt
    # ('w' - zalozi novy nebo prepise soubor, 'a' - pripise na konec souboru)
    with open('zapis.txt', 'w') as f:
        # help: co muzeme delat se soubory, napoveda
        #help(f)
        f.write(f'Pocet radku v souboru je {pocty[0]}.\n')
        f.write(f'Pocet radku v souboru je {pocty[1]}.\n')
